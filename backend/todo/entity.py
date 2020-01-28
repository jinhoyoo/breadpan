from breadpan.entity import Entity

class ToDoEntity(Entity):
    """Example of data entity class for ToDo
    """
    def __init__(self, todo_id:str, task:dict):
        """Contructor 
        
        Arguments:
            Entity {[Entity]} -- Base entity class
            todo_id {str} -- ID of todo item. Linked to entity_key.
            task {dict} -- Contents of todo task.
        """
        self.entity_key = todo_id
        self.task = task