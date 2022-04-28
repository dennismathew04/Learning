#from wsgiref import headers
'''import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def train():
    url="http://127.0.0.1:5000//"
    querystring={"Name":"Dennis","Age":"30"}
    header={"Accept":"application/json"}
    response=requests.request("GET",url,headers=headers,params=querystring)
    return response

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run()

import requests 
from flask import Flask
app = Flask(__name__)

url = "https://apis.alkemics.com/auth/v2/organization"
querystring={"organization_type":"1","offset":"0","limit":"20"}
headers={"Accept":"application/json"}
response=requests.request("GET",url,headers=headers,params=querystring)
print(response.text) 

def retrieve_model(path):
    try:
        trained_model=joblib.load(path)
        return trained_model
    except:
        print("You need to retrieve the trained model!")
    

lgbr_cars = retrieve_model("lgbr_cars.model")
model_test_input = [[3,1,190,-1,125000,5,3,1]]
vehicleType=int(input('3'))
gearbox=int(input('1'))
powerPS=int(input('190'))
model=int(input('-1'))
kilometer= int(input('125000'))
monthOfRegistration= int(input('5'))
fuelType= int(input('3'))
brand=int(input('1'))

url = "https://apis.alkemics.com/auth/v2/organization"
querystring={"organization_type":"1","offset":"0","limit":"20"}
headers={"Accept":"application/json"}
response=requests.request("GET",url,headers=headers,params=querystring)
print(response.text) 

#a=lgbr_cars.predict(model_test_input)'''

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



@app.route('/test', methods=['POST'])
def returnOne():
    params=request.get_json()
    model_test_input = params.get('model_test_input')
    lgbr_cars = retrieve_model("lgbr_cars.model")
    a=lgbr_cars.predict(np.array(model_test_input).reshape(1,-1))
    return jsonify({'predicted' : float(a)})

if __name__ == '__main__':
    app.run(debug=True,port=2000)
