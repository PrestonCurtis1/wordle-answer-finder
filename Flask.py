from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import solver

app = Flask(__name__)
CORS(app, origins=["http://localhost", "http://localhost:80", "http://192.168.1.142:80", "http://192.168.1.142"])
@app.route('/getWord', methods=['POST'])
def getWord():
    data = request.get_json()
    JSONData = data.get('JSONData')
    with open("data.json","w") as file:
        json.dump(JSONData,file)
    return jsonify({'Word': solver.chooseWord(solver.findWords())})

if __name__ == '__main__':
    app.run(debug=True)
