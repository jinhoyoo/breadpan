""" Resource packages

- Represents the resource to expose via HTTP.
- This layer is outterrior of software depending on the framework.
- So implements the resource class for 
"""

from http import HTTPStatus
from flask_restful import reqparse, abort, Resource
from .context import todo

todoCtrl = todo.ToDoController()
parser = reqparse.RequestParser()
parser.add_argument('task')


def abort_if_todo_doesnt_exist(todo_id):
    try:
        todoCtrl.read(todo_id)
    except:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class FlaskTodoController(Resource):

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return todoCtrl.read(todo_id), HTTPStatus.OK

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todoCtrl.delete(todo_id)
        return '',  HTTPStatus.NO_CONTENT

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        todoCtrl.update(todo_id, task)
        return task, HTTPStatus.CREATED
        

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class FlaskTodoListController(Resource):
    def get(self):
        return todoCtrl.read_all_data(), HTTPStatus.OK

    def post(self):
        args = parser.parse_args()
        all_data = todoCtrl.read_all_data()
        
        todo_id = len(all_data) + 1
        todo_id = 'todo%i' % todo_id
        task = {'task': args['task']}
        
        t = todoCtrl.create(todo_id, task)
        return t, HTTPStatus.CREATED
