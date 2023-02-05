import pymongo
from flask import Flask, jsonify, request
import json
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD= os.getenv("PASSWORD")
DB_NAME= os.getenv("DB_NAME")
COLLECTION_NAME= os.getenv("COLLECTION_NAME")
HOST= os.getenv("HOST")

app = Flask(__name__)

uri = "mongodb+srv://{}:{}@{}".format("mrunmayi", PASSWORD, HOST)
client = pymongo.MongoClient(uri)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

@app.route("/")
def index():
    documents = collection.find()
    data = [doc for doc in documents]
    res = json.dumps(data, default=str)
    return json.loads(res), 200

if __name__ == "__main__":
    app.run(debug=False)
    app.run(host="0.0.0.0", port=5000)
