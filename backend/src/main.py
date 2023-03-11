# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS

# creating the Flask application
app = Flask(__name__)
CORS(app)

@app.route('/assessment', methods=['POST'])
def create_assessment():
    props = request.get_json()
    response = 'I hope this works'
    return jsonify(response), 200