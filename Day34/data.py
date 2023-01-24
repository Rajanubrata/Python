import requests

parameter = {
    'amount': 10,
    'type': 'boolean',
}
response = requests.get(url="https://opentdb.com/api.php", params=parameter)
question_data = response.json()['results']
