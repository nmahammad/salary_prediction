import flask,json

from flask import Flask, jsonify, request
import numpy as np
import pickle

app = Flask(__name__)
@app.route('/predict', methods = ['GET'])

def predict():
    response = json.dumps( {'response' : 'yeahh'} )
    return response , 200

if __name__ == '__main__' : 
    app.run(debug = True)