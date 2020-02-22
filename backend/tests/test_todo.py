from .context import todo
import unittest

class TestTodoApp(unittest.TestCase):

    todo_ctrl = None

    def setUp(self):
        self.todo_ctrl = todo.ToDoController()
        self.todo_ctrl.create('todo1', {'task':'build an API'} )
        self.todo_ctrl.create('todo2', {'task':'build a server'} )
        self.todo_ctrl.create('todo3', {'task':'build a client'} )

    def tearDown(self):
        del self.todo_ctrl

    def test_create(self):
        todo_id = "task312"
        contents = {'task': 'myid'}
        output = self.todo_ctrl.create(todo_id, contents)
        self.assertEqual(output ,{todo_id:contents} )

    def test_read(self):        
        output = self.todo_ctrl.read(todo_id='todo1')
        self.assertEqual(output,  {'todo1': {'task': 'build an API'} } )


    def test_read_all(self):        
        output = self.todo_ctrl.read_all_data()
        self.assertNotEqual( len(output), 0)

    def test_update(self):
        todo_id = "task312"
        contents = {'task': 'myid'}
        self.todo_ctrl.create(todo_id, contents)
        new_contents = {'task': 'read the books'}
        self.todo_ctrl.update(todo_id, new_contents)    

        t = self.todo_ctrl.read(todo_id)
        self.assertEqual(t[todo_id]['task'] ,'read the books' )


    def test_delete(self):
        self.todo_ctrl.delete(todo_id='todo2')
        try:
            self.todo_ctrl.read(todo_id='todo2')
        except:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
