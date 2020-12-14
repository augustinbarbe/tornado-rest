# Tornado REST

tornado_rest is a framework built for tornado.

## Installation :

You can install tornado_rest with pip :

```shell
pip install tornado_rest
```

## Quick start

```python
from tornado.web import Application
from tornado_rest import Api, Namespace, Resource
from marshmallow import Schema, fields, INCLUDE, ValidationError

app = Application()

api = Api()


class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    task = fields.Str()  


class TodoService:
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)

    def get_all(self):
        return self.todos


todo_service = TodoService()
todo_service.create({'task': 'Build an API'})
todo_servicce.create({'task': 'Build a REST FRAMEWORK'})

ns = Namespace("todo")

@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return todo_service.get_all()

    @ns.marshal_list_with(todo)
    def post(self):
        '''Create a new task'''
        return todo_service.create(api.payload), 201


@ns.route('/<int:id>')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return todo_service.get(id)


    def delete(self, id):
        '''Delete a task given its identifier'''
        todo_service.delete(id)
        return '', 204

    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return todo_service.update(id, api.payload)
```

## TODO :

- payload validation : add a resource decorator to validate the request payload against a schema

```python

@ns.route('/<int:id>')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''

    @ns.expect(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return todo_service.update(id, api.payload)

```

```


- error handling : define error handlers at Api level 