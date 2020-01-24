from breadpan.interface import Controller, Presenter
from todo.entity import ToDoEntity
from todo.usecase import DataAccessGateway, ToDoCreateInteractor, ToDoUpdateInteractor, ToDoReadInteractor, ToDoDeleteInteractor, ToDoReadAllInteractor


class TodoDataInMemory(DataAccessGateway):
    """ TodoDataInMemory
    Store ToDoEntity as {key, value}:=>{todo_id, task}.
    """
    def __init__(self):
        self.TODOS = {}

    def create(self, entity: ToDoEntity):
        self.TODOS[entity.todo_id] = entity.task
        return

    def read(self, entity_id) -> ToDoEntity:
        return ToDoEntity(entity_id, self.TODOS[entity_id])

    def read_all(self):
        return [ ToDoEntity(key, value) for key, value in self.TODOS.items() ]

    def update(self, entity: ToDoEntity, **kwargs):
        self.TODOS[entity.todo_id] = entity.task
        return

    def delete(self, entity_id: str):
        del self.TODOS[entity_id]
        return


class ToDoPresenter(Presenter):
    """ToDoPresenter
    
    Convert ToDoEntity to {todo.id : {'task': todo.task}} for RESTful response as view. 
    """
    def show(self):
        todo_entry = self.output['todo']
        return { todo_entry.todo_id : {'task':todo_entry.task}  }

class ToDosPresenter(Presenter):
    """ToDosPresenter
    
    Convert list of ToDoEntity to the list of {todo.id : {'task': todo.task}} for RESTful response as view. 
    """
    def show(self):
        todo_entry_list = self.output['todo']
        new_list = [ { 'key':x.todo_id, 'task':x.task } for x in todo_entry_list ]
        return new_list
         


class ToDoController(Controller):

    def __init__(self):
        self.__data = TodoDataInMemory() # Use memory DB.

    def create(self, todo_id, contents):
        i = ToDoCreateInteractor(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data)).show()

    def read(self, todo_id):
        i = ToDoReadInteractor(todo_id=todo_id)
        return ToDoPresenter(i.run(self.__data)).show()

    def read_all_data(self):
        i = ToDoReadAllInteractor()
        return ToDosPresenter(i.run(self.__data)).show()

    def delete(self, todo_id):
        i = ToDoDeleteInteractor(todo_id=todo_id)
        return ToDoPresenter(i.run(self.__data)).show()

    def update(self, todo_id, contents):
        i = ToDoUpdateInteractor(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.run(self.__data)).show()
