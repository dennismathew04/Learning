import requests
import json

vehicleType =int(input('enter integer value for vehicleType '))
gearbox =int(input('enter integer value for gearbox '))
powerPS =int(input('enter integer value for powerPS '))
model =int(input('enter integer value for model '))
kilometer =int(input('enter integer value for kilometer '))
monthOfRegistration =int(input('enter integer value for monthOfRegistration '))
fuelType =int(input('enter integer value for fuelType '))
brand =int(input('enter integer value for brand '))

url = "http://127.0.0.1:2000/test"
headers = {"Content-Type": "application/json"}

querystring={"model_test_input" : [vehicleType,gearbox,powerPS,model,kilometer,monthOfRegistration,fuelType,brand]}
response = requests.post(url,headers=headers,json=querystring)
response.json()

