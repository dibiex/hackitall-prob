from flask import Flask, request, jsonify
from pymongo import MongoClient
app = Flask(__name__)
#client = MongoClient()

def start_transaction():
    pass

def add_transaction():
    pass

@app.route("/")
def hello():
    return 'Hello world!'
    
@app.route("/transaction/<uuid>", methods=['POST'])
def transaction(uuid):
    content = request.json
    #result = start_transaction(uuid, content)
    return jsonify({'uuid': uuid,
                    'result': 42})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
