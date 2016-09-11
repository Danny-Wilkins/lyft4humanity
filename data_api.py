import requests
import json
import pprint




pp = pprint.PrettyPrinter(indent=4)
with open('keys.json') as data_file:
    keys=json.load(data_file)
response = requests.get(
url = "https://api.typeform.com/v1/form/{}?key={}&completed=true&limit=2&order_by[]=date_submit,desc".format(keys['APIs']['Typeform']['UID_User'],keys['APIs']['Typeform']['Key'])
)

pp.pprint(response.json())
