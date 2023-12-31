import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
GENDER = "female"
AGE = 20
WEIGHT_KG = 51
HEIGHT_CM = 150
USERNAME = os.environ["SHEETY_USERNAME"]
PASSWORD = os.environ["SHEETY_PASSWORD"]

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
body = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM
}
response = requests.post(url=nutritionix_endpoint, headers=headers, json=body)
response.raise_for_status()
nutritionix_response = response.json()

today = datetime.now()
sheety_endpoint = "https://api.sheety.co/b864df17c1c3de9cd0e9ec42ec556e7f/workoutTracking/workouts"
# response = requests.get(url=sheety_endpoint)
# print(response.json())
for data in nutritionix_response["exercises"]:
    data_to_load = {
        "workout": {
            "date":  today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"],
        }
    }
    response = requests.post(url=sheety_endpoint, json=data_to_load, auth=(USERNAME, PASSWORD))
    response.raise_for_status()
