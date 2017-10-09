# Flask RESTFul

Effecient REST development

`pip install flask-restful`

- Extend `Resource`

```python

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)

```

- Define verbs - GET, POST etc

```python

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'messgae': "An item with name {} already exists.".format(name)}, 400  # Bad Request
        requestData = request.get_json(silent=True)  # Content-Type overridden - Force=True, no error with silent
        item = {'name': name, 'price': requestData['price']}
        items.append(item)
        return item, 201
```

- Authentication with `Flask-JWT` - 
`pip install flask-jwt`

```python
from flask import Flask
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, Api, reqparse

from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

```

Add ` @jwt_required()`

```python

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}
        
```

- Request Parsing

```python
    from flask_restful import Resource, Api, reqparse
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
```