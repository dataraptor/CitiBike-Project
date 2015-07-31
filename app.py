from flask import Flask
from flask import render_template
import json
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
import heatmap

app = Flask(__name__)

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
