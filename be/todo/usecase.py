
from breadpan.usecase import IDataAccessGateway, IUsecaseInteractor,IUsecaseOutputPort
from todo.entity import ToDoEntity


class TodoDataInMemory(IDataAccessGateway):
    """ TodoDataInMemory
    Store ToDoEntity as {key, value}:=>{todo_id, task}.
    """
    def __init__(self):
        self.TODOS = {}

    def create(self, entity: ToDoEntity):
        self.TODOS[entity.todo_id] = entity.task
        return

    def read(self,  todo_id) -> ToDoEntity:
        return ToDoEntity(todo_id, self.TODOS[todo_id])

    def read_all(self):
        return [ ToDoEntity(x.todo_id, x.task) for x in self.TODOS ]

    def update(self, entity: ToDoEntity, **kwargs):
        self.TODOS[entity.todo_id] = entity.task
        return

    def delete(self, todo_id):
        del self.TODOS[todo_id]
        return


class ToDoOutputPort(IUsecaseOutputPort):
    def __init__(self, **kwargs):
        super(ToDoOutputPort,self).__init__(**kwargs)
        # To-Do: Do any operation additionally.


class ToDoCreateInteractor(IUsecaseInteractor):
    def run(self,  data: IDataAccessGateway):        
        # Get id from the controller's data. 
        todo_id = self.data["todo_id"]
        contents = self.data["contents"]
        t = ToDoEntity(todo_id, contents)

        # Store the data. 
        data.create(t)

        # Link to output port
        return ToDoOutputPort(todo=t)

class ToDoUpdateInteractor(IUsecaseInteractor):
    def run(self, data: IDataAccessGateway):        
        # Get id from the controller's data. 
        todo_id = self.data["todo_id"]
        contents = self.data["contents"]
        t = ToDoEntity(todo_id, contents)

        # Store the data. 
        data.update(t)

        # Link to output port
        return ToDoOutputPort(todo=t)


class ToDoReadInteractor(IUsecaseInteractor):
    def run(self, data: IDataAccessGateway):
        # Get task ID
        todo_id = self.data["todo_id"]

        # Read data.
        t = data.read(todo_id)

        return ToDoOutputPort(todo=t)


class ToDoReadAllInteractor(IUsecaseInteractor):
    def run(self, data: IDataAccessGateway):
        return ToDoOutputPort(todo=data.read_all())


class ToDoDeleteInteractor(IUsecaseInteractor):
    def run(self, data: IDataAccessGateway):
        # Get task ID
        todo_id = self.data["todo_id"]
        data.delete(todo_id)
        return ToDoOutputPort()
