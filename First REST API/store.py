from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


stores = [

    {
        'name': 'My Store',
        'items': {
            'name': 'My Item',
            'price': 12.45
        }
    }
]


# What Req it will understand
@app.route("/store", methods=['POST'])
def createStore():
    requestData = request.get_json()
    new_store = {
        'name': requestData['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def getStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'error': 'store not found'})


@app.route('/store')
def getStores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    requestData = request.get_json()
    for store in stores:
        if store['name'] == name:
            store['items'].append({'name': requestData['name'],
                                   'price': requestData['price']})
            return jsonify(requestData)
    return jsonify({'error': 'store not found'})


@app.route('/store/<string:name>/item')
def getItemInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'error': 'store not found'})


app.run(port=5000)
