import urllib.request
import json

base_url = 'https://opentdb.com/'
endpoint = 'api.php?amount=10'

try:
    response = urllib.request.urlopen(f'{base_url}{endpoint}')
    read_data = response.read()
    string_data_representation = read_data.decode('utf8')

    json_data_representation = json.loads(string_data_representation)
    print(json_data_representation['results'][0])
except Exception as error:
    print(error)

