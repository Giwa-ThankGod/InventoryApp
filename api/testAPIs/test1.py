import requests

base_url = 'http://127.0.0.1:8000/'
endpoint = 'api/'

try:
    response = requests.get(f'{base_url}{endpoint}')
    print(response.json())
except Exception as error:
    print(error)

