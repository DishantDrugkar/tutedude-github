from flask import Flask, jsonify
import json

app = Flask(__name__)

# /api route
@app.route('/api', methods=['GET'])
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)