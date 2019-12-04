from breadpan.interface import Controller, Presenter
from todo.usecase import TodoDataInMemory, ToDoCreateInteractor, ToDoUpdateInteractor, ToDoReadInteractor, ToDoDeleteInteractor, ToDoReadAllInteractor

class ToDoPresenter(Presenter):
    """ToDoPresenter
    
    Convert ToDoEntity to {todo.id : {'task': todo.task}} for RESTful response as view. 
    """
    def ouput(self):
        todo_entry = self.output['todo']
        return { todo_entry.todo_id : {'task':todo_entry.task}  }

class ToDosPresenter(Presenter):
    """ToDosPresenter
    
    Convert list of ToDoEntity to the list of {todo.id : {'task': todo.task}} for RESTful response as view. 
    """
    def ouput(self):
        todo_entry_list = self.output['todo']
        new_list = [ { x.todo_id : {'task':x.task} } for x in todo_entry_list ]
        return new_list
         


class ToDoController(Controller):

    def __init__(self):
        self.__data = TodoDataInMemory() # Use memory DB.

    def create(self, todo_id, contents):
        i = ToDoCreateInteractor(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data)).ouput()

    def read(self, todo_id):
        i = ToDoReadInteractor(todo_id=todo_id)
        return ToDoPresenter(i.run(self.__data)).ouput()

    def read_all_data(self):
        i = ToDoReadAllInteractor()
        return ToDosPresenter(i.run(self.__data)).ouput()

    def delete(self, todo_id):
        i = ToDoDeleteInteractor(todo_id=todo_id)
        return ToDoPresenter(i.run(self.__data)).ouput()

    def update(self, todo_id, contents):
        i = ToDoUpdateInteractor(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data)).ouput()
