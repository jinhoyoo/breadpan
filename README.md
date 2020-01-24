Bread pan
========

기본적인 웹서비스를 간단하게 만드는 프로젝트 틀. 이 프로젝트를 Clone해서 이름을 바꿔서 진행하기를 권장한다. 

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQf-dHcXXifrSmL6RBJG5hdggKjvlcko0Or4IZW2j-myy2kTUbD&s" width="500px" title="Bread pan" alt="BreadPan"/>



시작하기
-----

### 전체 구조

* 전체 시스템을 ```entity```, ```usecase```, ```interface``` 계층으로 구분했다.
* 이 규칙을 따라서 서비스를 구현한다. 이 계층들의 의미는 Clean architecture[[en](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)/[kr](https://blog.coderifleman.com/2017/12/18/the-clean-architecture/)]를 참조하면 된다.



각 기본 Class들의 구조는 이와 같이 되어 있다. 이 기본 구조들을 상속 받아서 맞게 구현하면 된다.


![README](https://www.plantuml.com/plantuml/png/0/TL4x3i8m3DrpYin8pGcg2iHFJB0mC9fW4A8abUq8LS3TIIWWFY7Zyylxs7qM80d7MYbR0xDU-K3pank1m1eOMQa6x05sgDU4i6d06NIobrQNvOJWY5Mbpqh7D-vWOogTVW-iHUOf29wWLTUCJc2qqU93wAwqx0OprmHPU19T6lEG_pE_HC8B5IImukcJ-qHrKVIUw3p8G-8FDrycSN_GBiJF-dB5zybW2nQ_ThWWP4opw7kfiY67tWdvkiOkMwxp6oLLVOccA7rqctZi6m00 "README")


<!-- ```plantuml
@startuml

class YourOwnDatabases

package breadpan.entity <<Frame>> {
    Entity ..> DataAccessGateway
}

package breadpan.usecase <<Frame>> {

    UsecaseInputPort <.. Entity
    UsecaseInputPort <|.. UsecaseInteractor
    UsecaseInteractor --* UsecaseOutputPort
    UsecaseInteractor ..> DataAccessGateway
    DataAccessGateway <|.. YourOwnDatabases
}

package breadpan.interface <<Frame>> {
  Presenter ..|> UsecaseOutputPort
  Controller ..> UsecaseInteractor
  Controller --* Presenter
}

@enduml
``` -->


이 구조에 따라서 실제 Application을 만드는 예제로 할 일 관리 시스템(To-Do management system)를 만든다고 가정하고 설명을 할 것이다. 

### Entity 계층 구현 

가장 Business의 기본이 되는 정보를 담고 있다. 이것은 아래와 같이 `Entity`라는 Interface를 상속받아 구현한다.  
```python
from breadpan.entity import Entity

class ToDoEntity(Entity):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
```

### Usecase들 계층 구현 

실제 데이터를 담아서 처리하는 `Interactor`를 구현해서 `UsecaseOutputPort`을 이용해서 원하는 이름의 데이터로 내보내게 된다.  

```python
from breadpan.entity import UsecaseInteractor, UsecaseOutputPort
from todo.entity import ToDoEntity

class ToDoCreateInteractor(UsecaseInteractor):
    def run(self,  data: DataAccessGateway):
        # Get id from the controller's data.
        todo_id = self.input["todo_id"]
        contents = self.input["contents"]
        t = ToDoEntity(todo_id, contents['task'])

        # Store the data. 
        data.create(t)

        # Link to output port
        return UsecaseOutputPort(todo=t) #Expose the data 't' with 'todo' as key.
```


### Interface 계층 구현 

#### DataAccessGateway
`DataAccessGateway`는 데이터 접근하는 Class들의 기본적인 인터페이스다. 예를 들어 dictionary로 데이터를 저장하는 구조를 짜면 아래와 같이 짤 수 있다. MySQL등의 외부 데이터베이스들에 접근해서 데이터를 기록하는 것도 이 인터페이스로 확장할 수 있다.  

```python
from todo.entity import ToDoEntity
from todo.usecase import DataAccessGateway

class TodoDataInMemory(DataAccessGateway):
    def __init__(self):
        self.TODOS = {}

    def create(self, entity: ToDoEntity):
        self.TODOS[entity.todo_id] = entity.task
        return

    def read(self,  todo_id) -> ToDoEntity:
        return ToDoEntity(todo_id, self.TODOS[todo_id])

    def read_all(self):
        return [ ToDoEntity(key, value) for key, value in self.TODOS.items() ]

    def update(self, entity: ToDoEntity, **kwargs):
        self.TODOS[entity.todo_id] = entity.task
        return

    def delete(self, todo_id):
        del self.TODOS[todo_id]
        return
```


#### Controller / Presenter

실제 외부의 interface와 연결되서 입력/출력을 총괄하는 모듈인 Controller와 Presenter는 아래와 같이 작성한다. 

```python
from breadpan.interface import Controller, Presenter
from todo.entity import ToDoEntity
from todo.usecase import DataAccessGateway, ToDoCreateInteractor


class ToDoPresenter(Presenter):
    def show(self):
        todo_entry = self.output['todo'] # Take the data with key 'todo' TodoController exposed.
        return { todo_entry.todo_id : {'task':todo_entry.task}  }


class ToDoController(Controller):
    def __init__(self):
        self.__data = TodoDataInMemory() # Memory를 이용하게 구현한 DB 모듈.

    def create(self, todo_id, contents):
        i = ToDoCreateInteractor(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data)).show()
    ......

```

실제 이를 가지고 Flask에 연결해서 사용한다면, 이렇게 쓰이게 된다.

```python

import todo
todoCtrl = todo.ToDoController()

class FlaskTodoListController(Resource):

    def post(self):
        args = parser.parse_args()
        all_data = todoCtrl.read_all_data()

        todo_id = len(all_data) + 1
        todo_id = 'todo%i' % todo_id
        task = {'task': args['task']} 

        todoCtrl.create(todo_id, task)
        return task, HTTPStatus.CREATED

.......

api.add_resource(FlaskTodoController, '/todos/<todo_id>')
```


#### View

현재는 Front-end / Back-end 따로 구현하고 그 사이를 RESTful API로 만드는 방식을 추천한다. 최대한 Front-end는 주어진 데이터를 시각적 구조에 보여주는 View에 대한 구조를 맞춰서 작업을 하고 데이터 형식의 변경이나 새로운 종합적인 데이터를 필요로 할 때는 무조건 Back-end에서 해서 보내주는 것을 원칙으로 한다. Presenter class가 있는 이유가 이런 용도다. 

Front-end의 경우에는 [Google optimize](https://optimize.google.com/)와 같은 A/B test 도구들을 지원해서 더 다양한 Business운영의 실험을 할 수 있게 하기를 권한다.

#### 자세한 내용
 [구현하는 방법](docs/how_to_implement.md)을 참조하기 바란다. 


Folder structure
-------


```
├── backend  : Back-end 프로젝트
│   ├── Makefile
│   ├── README.md
│   ├── breadpan  : 기본 Framework
│   ├── todo      : breadpan을 기반으로 만든 간단한 todo 예제
│   ├── tests     : Test code
│   └── apps      : todo 예제를 가지고 다양한 형태로 만든 예제. (현재는 Flask기반 WebApp)
│  
├── frontend
│   ├── Makefile
│   ├── README.md

```

그 외에 따를 원칙들
-----
* [12 Factors app](https://12factor.net/ko/)

다루거나 하지 않을 것
------
* Clean architecture의 엄격한 정의/적용 : 이 구조는 '해석한' 형태다. 
* 특정 Web framework에 맞춰서 코드를 재포장하지 않는다. 이러한 코드들은 'main' component안에 들어가야 한다.