###



from breadpan.entity import IEntity

class ToDoEntity(IEntity):
    def __init__(self):
        self.todo_id = ""
        self.todo = {
            'task':""
        }
    def __init__(self, todo_id, todo):
        self.todo_id = todo_id
        self.todo = todo