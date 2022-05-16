#from wsgiref import headers
import requests
from flask import Flask,jsonify,request
import pandas as pd
import json
from urllib.request import urlopen
import numpy as np
import joblib


app = Flask(__name__)

def retrieve_model(path):
    try:
        trained_model=joblib.load(path)
        return trained_model
    except:
        print("You need to retrieve the trained model!")



@app.route('/car_price_prediction', methods=['POST'])
def returnOne():
    params=request.get_json()
    model_test_input = params.get('model_test_input')
    lgbr_cars = retrieve_model("lgbr_cars.model")
    a=lgbr_cars.predict(np.array(model_test_input).reshape(1,-1))
    return jsonify({'predicted' : float(a)})

if __name__ == '__main__':
    app.run(debug=True,port=2000)
