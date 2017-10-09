# Create first REST API with Flask

## Hello World!

```python
from flask import Flask

hello = Flask(__name__)


# What Req it will understand
@hello.route("/")  # http://www.google.com/ , Homepage
def home():
    return "Hello, world!"


hello.run(port=5000)
```

## Sample Store Backend

```python

from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
stores = [

    {
        'name': 'My Store',
        'items': {
            'name': 'My Item',
            'price': 12.45
        }
    }
]
@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    requestData = request.get_json()
    for store in stores:
        if store['name'] == name:
            store['items'].append({'name': requestData['name'],
                                   'price': requestData['price']})
            return jsonify(requestData)
    return jsonify({'error': 'store not found'})
    
```