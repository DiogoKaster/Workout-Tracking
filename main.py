import requests
import datetime as dt
import os

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = os.environ["APP_KEY"]
APP_ID = os.environ["APP_ID"]

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise = input("Tell me witch exercise you did: ")

EXERCISE_PARAMS = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 73,
    "height_cm": 173,
    "age": 19
}

response = requests.post(API_ENDPOINT, json=EXERCISE_PARAMS, headers=HEADERS)
result = response.json()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_HEADER = {
    "Authorization": os.environ["TOKEN"]
}


for exercise in result["exercises"]:
    SHEETY_PARAMS = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response1 = requests.post(SHEETY_ENDPOINT, json=SHEETY_PARAMS, headers=SHEETY_HEADER)
    print(response1.text)
