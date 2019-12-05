
from breadpan.usecase import DataAccessGateway, UsecaseInteractor,UsecaseOutputPort
from todo.entity import ToDoEntity


class TodoDataInMemory(DataAccessGateway):
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
        return [ ToDoEntity(key, value) for key, value in self.TODOS.items() ]

    def update(self, entity: ToDoEntity, **kwargs):
        self.TODOS[entity.todo_id] = entity.task
        return

    def delete(self, todo_id):
        del self.TODOS[todo_id]
        return


class ToDoCreateInteractor(UsecaseInteractor):
    def run(self,  data: DataAccessGateway):        
        # Get id from the controller's data. 
        todo_id = self.input["todo_id"]
        contents = self.input["contents"]
        t = ToDoEntity(todo_id, contents['task'])

        # Store the data. 
        data.create(t)

        # Link to output port
        return UsecaseOutputPort(todo=t)

class ToDoUpdateInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):        
        # Get id from the controller's data. 
        todo_id = self.input["todo_id"]
        contents = self.input["contents"]
        t = ToDoEntity(todo_id, contents['task'])

        # Store the data. 
        data.update(t)

        # Link to output port
        return UsecaseOutputPort(todo=t)


class ToDoReadInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):
        # Get task ID
        todo_id = self.input["todo_id"]

        # Read data.
        t = data.read(todo_id)

        return UsecaseOutputPort(todo=t)


class ToDoReadAllInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):
        return UsecaseOutputPort(todo=data.read_all())


class ToDoDeleteInteractor(UsecaseInteractor):
    def run(self, data: DataAccessGateway):
        # Get task ID
        todo_id = self.input["todo_id"]
        data.delete(todo_id)
        return UsecaseOutputPort()
