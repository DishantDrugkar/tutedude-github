from flask import Flask, jsonify, request
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB connection
client = MongoClient(
    "mongodb+srv://dishantdrugkar1_db_user:bC7DXVUyuHEdx8mK@cluster0.jy5z4tk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
db = client.mongo_flask_db
collection = db.todos

# /api route
@app.route('/api', methods=['GET'])
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

# /submittodoitem route
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json
    itemName = data.get("itemName")
    itemDescription = data.get("itemDescription")
    if not itemName or not itemDescription:
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    # Insert into MongoDB
    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })
    return jsonify({"status": "success", "message": "Item added"}), 201

if __name__ == "__main__":
    app.run(debug=True)