import requests

GENDER = 'male'
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 19

APP_ID = '7d6499d3'
API_KEY = 'b9caacd1920d702b280fc11ff79df37d'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


#******************************************* SETTING UP SHEETY API **********************************************************
from datetime import datetime

username = 'Anubrata Mallick'
projectName = 'My workout [Python]'
sheetName = 'My workout [Python]'

sheet_endpoint = "https://api.sheety.co/7a5c2eaffe30cc6d05e9bc9ea744c777/myWorkout [python]/sheet1"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    print(exercise["name"].title())
    print(exercise["duration_min"])
    print(exercise["nf_calories"])
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
******************************************************************************************************************************

******************************************************************************************************************************

nutritionix Api = https://www.nutritionix.com/business/api
sheety API = https://sheety.co/
