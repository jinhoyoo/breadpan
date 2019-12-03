from breadpan.interface import IController, IPresenter
from todo.usecase import TodoDataInMemory, ToDoCreateInteractor, ToDoUpdateInteractor, ToDoReadInteractor, ToDoDeleteInteractor, ToDoReadAllInteractor

class ToDoPresenter(IPresenter):
    pass


class ToDoController(IController):

    def __init__(self):
        self.__data = TodoDataInMemory() # Use memory DB.

    def create(self, todo_id, contents):
        i = ToDoCreateInteractor()
        i.input(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data))

    def read(self, todo_id):
        i = ToDoReadInteractor()
        i.input(todo_id=todo_id)
        return ToDoPresenter(i.run(self.__data))

    def read_all_data(self):
        i = ToDoReadAllInteractor()
        return ToDoPresenter(i.run(self.__data))

    def delete(self, todo_id):
        i = ToDoDeleteInteractor()
        i.input(todo_id=todo_id)
        return ToDoPresenter(i.run(self.__data))

    def update(self, todo_id, contents):
        i = ToDoUpdateInteractor()
        i.input(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data))
