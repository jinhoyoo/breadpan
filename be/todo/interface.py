from breadpan.interface import IController, IPresenter
from breadpan.usecase import IUsecaseOutputPort, IUsecaseInteractor, IDataAccessGateway
from todo.usecase import ToDoCreateInteractor, ToDoUpdateInteractor, ToDoReadInteractor, ToDoDeleteInteractor, ToDoReadAllInteractor

class ToDoPresenter(IPresenter):
    pass

class ToDoController(IController):
    def create(self, todo_id, contents):
        i = ToDoCreateInteractor()
        i.input(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run())

    def read(self, todo_id):
        i = ToDoReadInteractor()
        i.input(todo_id=todo_id)
        return ToDoPresenter(i.run())

    def read_all_data(self):
        i = ToDoReadAllInteractor()
        return ToDoPresenter(i.run())

    def delete(self, todo_id):
        i = ToDoDeleteInteractor()
        i.input(todo_id=todo_id)
        return ToDoPresenter(i.run())

    def update(self, todo_id, contents):
        i = ToDoUpdateInteractor()
        i.input(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run())



class ToDoDataAccess(IDataAccessGateway):

    __model = None

    def create(self, **kwargs):
        return self.__model.create(**kwargs)

    def read(self,  **kwargs):
        return self.__model.read(**kwargs)

    def update(self,  **kwargs):
        return self.__model.update(**kwargs)

    def delete(self,  **kwargs):
        return self.__model.delete(**kwargs)
