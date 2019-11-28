
from be.pkg.usecase import IUsecaseOutputPort, IUsecaseInteractor

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

class ToDoOutputPort(IUsecaseOutputPort):
    def __init__(self, **kwargs):
        super(ToDoOutputPort,self).__init__(**kwargs)
        # To-Do: Do any operation additionally.


class ToDoCreateInteractor(IUsecaseInteractor):
    def operate(self):        
        # Get id from the controller's data. 
        todo_id = self.data["todo_id"]
        contents = self.data["contents"]

        # Store the data. 
        TODOS[todo_id] = contents

        # Link to output port
        return ToDoOutputPort(todo={todo_id:TODOS[todo_id]})


class ToDoReadInteractor(IUsecaseInteractor):
    def operate(self):
        # Get task ID
        todo_id = self.data["task_id"]

        # Link to output port
        return ToDoOutputPort(todo={todo_id:TODOS[todo_id]})


class ToDoDeleteInteractor(IUsecaseInteractor):
    def operate(self):
        id = self.data["to_do_id"]
        del TODOS[todo_id]
        return ToDoOutputPort(self)