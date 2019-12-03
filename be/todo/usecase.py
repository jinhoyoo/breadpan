
from breadpan.usecase import IUsecaseOutputPort, IUsecaseInteractor, IDataAccessGateway
from todo.entity import ToDoEntity

class TodoDataAccessWithMem(IDataAccessGateway):

    def __init__(self):
        self.TODOS = {}

    def create(self, entity: ToDoEntity):
        self.TODOS[entity.todo_id] = entity.todo

    def read(self,  todo_id) -> ToDoEntity:
        return ToDoEntity(todo_id, self.TODOS[todo_id])

    def read_all(self):
        return self.TODOS

    def update(self, entity: ToDoEntity, **kwargs):
        self.TODOS[entity.todo_id] = entity.todo
        return

    def delete(self, todo_id):
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
        t = ToDoEntity(todo_id, contents)

        # Store the data. 
        self.__data_gateway.create(t)

        # Link to output port
        return ToDoOutputPort(todo=t.__dict__)

class ToDoUpdateInteractor(IUsecaseInteractor):
    def run(self):        
        # Get id from the controller's data. 
        todo_id = self.data["todo_id"]
        contents = self.data["contents"]
        t = ToDoEntity(todo_id, contents)

        # Store the data. 
        self.__data_gateway.update(t)

        # Link to output port
        return ToDoOutputPort(todo=t.__dict__)


class ToDoReadInteractor(IUsecaseInteractor):
    def run(self):
        # Get task ID
        todo_id = self.data["todo_id"]

        # Read data.
        t = self.__data_gateway.read(todo_id)

        return ToDoOutputPort(todo=t.__dict__)


class ToDoReadAllInteractor(IUsecaseInteractor):
    def run(self):
        # Link to output port
        return ToDoOutputPort(todo=self.__data_gateway.read_all().__dict__)


class ToDoDeleteInteractor(IUsecaseInteractor):
    def run(self):
        # Get task ID
        todo_id = self.data["todo_id"]
        del TODOS[todo_id]
        return ToDoOutputPort()