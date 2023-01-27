import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "Anubrata@l0g1n@098"
USERNAME = "anubrata"
GRAPHID = "graph1"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPHID,
    "name": "Habit Tracker",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

header_params = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=header_params)
# print(response.json())

value_to_the_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = datetime.now()

header_value = {
    "X-USER-TOKEN": TOKEN,
}

value_to_the_graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7.74",
}

# response = requests.post(url=value_to_the_graph, json=value_to_the_graph_params, headers=header_value)
# print(response.text)
