
from breadpan.usecase import IUsecaseOutputPort, IUsecaseInteractor, IDataAccessGateway
from todo.entiry import ToDoEntity

class TodoDataAccessWithMem(IDataAccessGateway):

    def __init__(self):
        self.TODOS = {
        'todo1': {'task': 'build an API'},
        'todo2': {'task': '?????'},
        'todo3': {'task': 'profit!'},
    }

    def create(self, entity: ToDoEntity):
        self.TODOS[entity.todo_id] = entity.todo

    def read(self,  todo_id) -> ToDoEntity:
        return ToDoEntity(todo_id, self.TODOS[todo_id])

    def update(self, entity: ToDoEntity, **kwargs):
        pass

    def delete(self,  entity: IEntity):
        pass



class ToDoOutputPort(IUsecaseOutputPort):
    def __init__(self, **kwargs):
        super(ToDoOutputPort,self).__init__(**kwargs)
        # To-Do: Do any operation additionally.


class ToDoCreateInteractor(IUsecaseInteractor):
    def run(self):        
        # Get id from the controller's data. 
        todo_id = self.data["todo_id"]
        contents = self.data["contents"]

        # Store the data. 
        TODOS[todo_id] = contents

        # Link to output port
        return ToDoOutputPort(todo={todo_id:TODOS[todo_id]})

class ToDoUpdateInteractor(IUsecaseInteractor):
    def run(self):        
        # Get id from the controller's data. 
        todo_id = self.data["todo_id"]
        contents = self.data["contents"]

        # Store the data. 
        TODOS[todo_id] = contents

        # Link to output port
        return ToDoOutputPort(todo={todo_id:TODOS[todo_id]})


class ToDoReadInteractor(IUsecaseInteractor):
    def run(self):
        # Get task ID
        todo_id = self.data["todo_id"]

        # Link to output port
        return ToDoOutputPort(todo={todo_id:TODOS[todo_id]})


class ToDoReadAllInteractor(IUsecaseInteractor):
    def run(self):
        # Link to output port
        return ToDoOutputPort(todo=TODOS)


class ToDoDeleteInteractor(IUsecaseInteractor):
    def run(self):
        # Get task ID
        todo_id = self.data["todo_id"]
        del TODOS[todo_id]
        return ToDoOutputPort()