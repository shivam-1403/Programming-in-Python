import requests
from datetime import datetime


APP_ID = "YOUR_API_ID"
API_KEY = "YOUR_API_KEY"
EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/221ce289ffd4462f4f899ab22887bf16/myWorkouts/workouts"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

parameters = {
    "query" : input("Tell me which exercises you did ?")
}

response = requests.post(url=EXERCISE_URL, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

authorization_header = (
    "ABC",
    "XYZ"
)

for exercise in result["exercises"]:
    sheet_input = {
        "workout" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }
sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_input, auth=authorization_header)
print(sheet_response.text)