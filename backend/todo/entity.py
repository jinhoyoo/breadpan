from breadpan.entity import Entity

class ToDoEntity(Entity):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task