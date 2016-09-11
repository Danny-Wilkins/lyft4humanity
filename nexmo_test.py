import requests
import json
from pymongo import MongoClient
with open('keys.json') as data_file:
    keys=json.load(data_file)



response = requests.post(
    url = "https://rest.nexmo.com/sms/json?api_key={}&api_secret={}&to={}&from=12674055738&text=Hello+from+Lyft4Humanity".format(
    keys['APIs']['Nexmo']['Key'],keys['APIs']['Nexmo']['Secret'],15089308779))

if response.status_code == 201:
    print(response.json()['messages']['status'])
else:
    print(response.status_code)
    print(response.json())
