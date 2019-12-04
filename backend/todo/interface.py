from breadpan.interface import IController, IPresenter
from todo.usecase import TodoDataInMemory, ToDoCreateInteractor, ToDoUpdateInteractor, ToDoReadInteractor, ToDoDeleteInteractor, ToDoReadAllInteractor

class ToDoPresenter(IPresenter):
    """ToDoPresenter
    
    Convert ToDoEntity to {todo.id : {'task': todo.task}} for RESTful response as view. 
    """
    def ouput(self):
        todo_entry = self.data['todo']
        return { todo_entry.todo_id : {'task':todo_entry.task}  }

class ToDosPresenter(IPresenter):
    """ToDosPresenter
    
    Convert list of ToDoEntity to the list of {todo.id : {'task': todo.task}} for RESTful response as view. 
    """
    def ouput(self):
        todo_entry_list = self.data['todo']
        new_list = [ { x.todo_id : {'task':x.task} } for x in todo_entry_list ]
        return new_list
         


class ToDoController(IController):

    def __init__(self):
        self.__data = TodoDataInMemory() # Use memory DB.

    def create(self, todo_id, contents):
        i = ToDoCreateInteractor()
        i.input(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data)).ouput()

    def read(self, todo_id):
        i = ToDoReadInteractor()
        i.input(todo_id=todo_id)
        return ToDoPresenter(i.run(self.__data)).ouput()

    def read_all_data(self):
        i = ToDoReadAllInteractor()
        return ToDosPresenter(i.run(self.__data)).ouput()

    def delete(self, todo_id):
        i = ToDoDeleteInteractor()
        i.input(todo_id=todo_id)
        return ToDoPresenter(i.run(self.__data)).ouput()

    def update(self, todo_id, contents):
        i = ToDoUpdateInteractor()
        i.input(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data)).ouput()
