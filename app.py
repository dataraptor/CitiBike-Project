from flask import Flask
from flask import render_template
import json
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
import heatmap

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'CitiBike'
COLLECTION_NAME = 'historical'
FIELDS = {
    "tripduration" : 1,
    "starttime" : 1,
    "stoptime" : 1,
    "start station name" : 1,
    "start station latitude" : 1,
    "start station longitude" : 1,
    "end station name" : 1,
    "end station latitude" : 1,
    "end station longitude" : 1
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/citibike/heatmap")
def citibike_heatmap():
#    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
#    collection = connection[DB_NAME][COLLECTION_NAME]
#    data = collection.find(projection=FIELDS)
    return heatmap.heatmap_data()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000, debug = True)
