from breadpan.entity import IEntity

class ToDoEntity(IEntity):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task