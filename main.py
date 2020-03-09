from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime
import sys

app = Flask(__name__)
client = MongoClient('mongodb://db:27017')
db = client['transactions']


def charge_card():
    #This function does nothing it should probably charge the card
    pass


def start_transaction(uuid, content):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    str_date_today = today.strftime("%d-%m-%Y")
    str_date_yesterday = today.strftime("%d-%m-%Y") 
    collection_today = db[str_date_today]
    collection_yesterday = db[str_date_yesterday]

    print("Checking dbs", file=sys.stderr)
    if collection_today.count_documents({ 'uuid': uuid }, limit = 1) != 0:
        # No transactions with this id today
        return False
    if collection_yesterday.count_documents({ 'uuid': uuid }, limit = 1) != 0:
        # No transactions with this id yesterday
        return False

    #Charge the card
    charge_card()

    print("Inserting in db", file=sys.stderr)
    #Add transaction to db
    collection_today.insert_one(content)
    return True

    

@app.route("/transaction/<uuid>", methods=['POST'])
def transaction(uuid):
    content = request.json
    content['uuid'] = uuid
    result = start_transaction(uuid, content)
    return jsonify({'uuid': uuid,
                    'result': result})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
