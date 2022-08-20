from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/submit/image', methods=['POST'])

def submit_image():
    json_data = json.loads(request.data)
    camera_id = json_data['args'][0]
    filename = json_data['args'][1]
    print(f'filename: {filename}, camera_id: {camera_id}')

    return 'Uploaded', 200

app.run(host='0.0.0.0', port=3000)
