from flask import Flask, render_template, redirect, url_for, request
import random
import requests
import json
import ast
from pymongo import MongoClient
from collections import OrderedDict
from geopy.geocoders import Nominatim
with open('keys.json') as data_file:
    keys=json.load(data_file)

app = Flask(__name__)

client = MongoClient("mongodb://104.237.144.218:27017")
db = client.database
data_response = requests.get(
url = "https://api.typeform.com/v1/form/{}?key={}&completed=true&limit=1&order_by[]=date_submit,desc".format(keys['APIs']['Typeform']['UID_User'],keys['APIs']['Typeform']['Key'])
)
valList = []
fieldList = OrderedDict()
ordered = OrderedDict()
for item in data_response.json()["questions"]:
    assocID = item['id']
    valList += [assocID]
    fieldList[assocID] = data_response.json()['responses'][0]['answers'][assocID]
#for key in fieldList:
    #print(fieldList[key])
def create_customer():
#Head / Director of the shelter will fill out information as well as potential users
#the shelter head will be expected to as


    apiKey = keys["APIs"]['Nessie']['Nessie_API_KEY']
    url = 'http://api.reimaginebanking.com/customers/?key={}'.format(apiKey)
    payload = {
      "first_name": fieldList[valList[0]].split(' ')[0],
      "last_name": fieldList[valList[0]].split(' ')[1],
      "address": {
        "street_number": fieldList[valList[2]].split(',')[0].split(' ')[0],
        "street_name": fieldList[valList[2]].split(',')[0].split(' ')[1] + " " + fieldList[valList[2]].split(',')[0].split(' ')[2] ,
        "city": fieldList[valList[2]].split(',')[1].strip(),
        "state": fieldList[valList[2]].split(',')[2].split(' ')[1],
        "zip": fieldList[valList[2]].split(',')[2].split(' ')[2]
        }

    }
    # Create a Savings Account
    response = requests.post(
    	url,
        data = json.dumps(payload),
    	headers={'content-type':'application/json'},
    	)

    if response.status_code == 201:
        print('customer created')
        payload['customer_id'] = response.json()['objectCreated']['_id']
        customer_id = payload['customer_id']
        payload['phone_number'] = fieldList[valList[5]]
        cust_info_id = db.customers.insert_one(payload)
        customer_information = {
        'cust_id':customer_id,
        'cust_info_id':cust_info_id
        }
    else:
        print(response.status_code)
        print(response.json())
    return customer_id


def create_shelter_account():
    data_response = requests.get(
    url = "https://api.typeform.com/v1/form/{}?key={}&completed=true&limit=1&order_by[]=date_submit,desc".format(keys['APIs']['Typeform']['UID_Shelter'],keys['APIs']['Typeform']['Key'])
    )
    fields = []
    shelter = OrderedDict()

    for item in data_response.json()["questions"]:
        someID = item['id']
        fields += [someID]
        shelter[someID] = data_response.json()['responses'][0]['answers'][someID]



    data = {
    "Shelter":shelter[fields[4]],
    "Shelter Director": {
        "Director_First_name" : shelter[fields[0]].split(' ')[0],
        "Director_Last_name" : shelter[fields[0]].split(' ')[1],
        "Director_Number" : shelter[fields[5]]
    },
    "Shelter Address": {
        "Shelter City": shelter[fields[5]].split(',')[1],
        "Shelter State": shelter[fields[5]].split(',')[2].split(' ')[0].strip(),
        "Shelter Zip": shelter[fields[5]].split(',')[2].split(' ')[1].strip()
        }
    }

    data['phone_number'] = shelter[fields[7]]
    data['userid'] = shelter[fields[2]]
    data['password'] = shelter[fields[3]]
    shelter_info_id = db.shelters.insert_one(data)

def create_account(nickname, customer_id):
    #customerId = client.customer.find("first_name":first_name,"last_name":last_name, "zip_code", zip_code)
    apiKey = keys["APIs"]['Nessie']['Nessie_API_KEY']

    url = 'http://api.reimaginebanking.com/customers/{}/accounts/?key={}'.format(customer_id,apiKey)
    payload = {

      "type": "Checking",
      "nickname": nickname,
      "rewards": 0,
      "balance": 500

    }
    # Create a Savings Account
    response = requests.post(
    	url,
        data = json.dumps(payload),
    	headers={'content-type':'application/json'},
    	)

    if response.status_code == 201:
        print('account created')
        account_id = response.json()['objectCreated']['_id']
    else:
        print(response.status_code)
        print(response.json())
    customers = db.customers.find({'customer_id':customer_id})
    print(customers[0])
    payload['account_id'] = account_id
    payload['phone_number']=fieldList[valList[5]]
    db.checking_accounts.insert_one(payload)

def welcome_customers():

    message = "Hello from Lyft4Humanity this is a test message, welcome to the service for crowdfunding lyft rides for the homeless!"
    people = db.customers.find({})
    #for x in people:
        #if x['address']['zip'] == '19104':
            #phone_number = '1'+x['phone_number']
        #if x['address']['zip'] == '19104':
            #phone_numbr = '1' + x['phone_number']
    response = requests.post(
    url = "https://rest.nexmo.com/sms/json?api_key={}&api_secret={}&to={}&from=12674055738&text={}".format(
    keys['APIs']['Nexmo']['Key'],keys['APIs']['Nexmo']['Secret'],'14132045213',message))
def request_money_in_area(zipcode, name ):
    origin = geolocator(input("Enter origin: "))

    destination = geolocator(input("Enter destination: "))
    cost = request_info('cost', origin['lat'], origin['lng'],
                 destination['lat'], destination['lng'])
    people = db.customers.find({})
    message = "Would you like to donate"
    total = 0
    for x in people:
        if x['address']['zip'] == '{}'.format(zipcode):
            total+=1
    message = "Would you like to donate {} to help {} get to {}".format(float(cost)/total,name, destination)
    for x in people:
        if x['address']['zip'] == '{}'.format(zipcode):
            phone_number = '1'+x['phone_number']
    response = requests.post(
    url = "https://rest.nexmo.com/sms/json?api_key={}&api_secret={}&to={}&from=12674055738&text={}".format(
    keys['APIs']['Nexmo']['Key'],keys['APIs']['Nexmo']['Secret'],phone_number,message))

#def lyft_main():
def lyft_main():
    #Get a location thing to let you put in an address and do this for you

    #location = {'lat' : input("Latitude: "), 'lng' : input("Longitude: ")}

    origin = geolocator(input("Enter origin: "))

    destination = geolocator(input("Enter destination: "))

    #print(origin, destination)

    data_type = ''


    data_type = input("Enter a data type [ETA] [Drivers] [Cost] [Ridetypes]: ").lower()

    if data_type == 'cost':
        request_info(data_type, origin['lat'], origin['lng'],
        		 destination['lat'], destination['lng'])

    else:
        request_info(data_type, origin['lat'], origin['lng'])

    request_ride(origin['lat'], origin['lng'], destination['lat'], destination['lng'])

def geolocator(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    print(location.address)

    return {'lat':location.latitude, 'lng':location.longitude}

def request_info(data_type, beg_lat, beg_lng, end_lat=None, end_lng=None):
    header = {'Authorization' : 'Bearer {}'.format(gen_access_token(True))}

    if end_lat != None and end_lng != None:
        url = 'https://api.lyft.com/v1/cost?start_lat={}&start_lng={}\
        							   &end_lat={}&end_lng={}'.format(beg_lat, beg_lng,
        							   								  end_lat, end_lng)
    else:
        url = 'https://api.lyft.com/v1/{}?lat={}&lng={}'.format(data_type, beg_lat, beg_lng)

    r = requests.get(url, headers=header)

    #print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',':')))

    if data_type == 'cost':
        max_cost=''
    #I know there's a better way to do this

    max_cost = float(r.json()['cost_estimates'][0]['estimated_cost_cents_max'])/100
        #print("ES

    return max_cost

def request_ride(beg_lat, beg_lng, end_lat, end_lng):

    header = {'Authorization' : 'Bearer {}'.format(gen_access_token(True)),
      'Content-Type' : 'application/json'}

    url = 'https://api.lyft.com/v1/rides'

    data = {"ride_type" : "lyft", "origin" : {"lat" : 34.305658, "lng" : -118.8893667} }

    #orig = ['origin', {'beg_lat' : beg_lat, 'beg_lng' : beg_lng}]
    dest = ['destination', {'end_lat' : end_lat, 'end_lng' : end_lng}]

    print('Requesting ride...')

    try:
        r = requests.post(url, headers=header, data=data)
    except:
        print('Having difficulties right now. Try again later.')


#ride = requests.get(url, data={'string':'ride_id'}, status='pending')

#print(ride)

def gen_access_token(sandbox=False):

    header = {'Content-Type' : 'application/json'}

    #client_id : client_secret
    if sandbox == False:
        user = ('NVHuajSI1tA8', 'QUP4Fk8JC626anlN-uiZs3iW0qKCpLxu')
    else:
        user = ('NVHuajSI1tA8', 'SANDBOX-QUP4Fk8JC626anlN-uiZs3iW0qKCpLxu')

    data = json.dumps({'grant_type' : 'client_credentials', 'scope': 'public'})

    token_url = 'https://api.lyft.com/oauth/token'

    r = requests.post(token_url, data=data, headers=header, auth=user)

    access_token = r.json()['access_token']

    return access_token


def send_code(shelter_number):
    pass
def update_account(customer_id, valueToSub):
    pass
def main():
    #cust_id = create_customer()
    #print(cust_id)
    #create_account(fieldList[valList[1]],cust_id)
    #create_shelter_account()
    request_money_in_area(19104,'Mark')
    #lyft_main()


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('ride_request'))
    return render_template('login.html', error=error)
@app.route('/request', methods=['GET', 'POST'])
def ride_request():
    bal = 10
    if request.method == 'POST' and bal>0: #check balance here
        return redirect(url_for('redeem'))
    else:
        request_money_in_area(19104,'Mark')
    return render_template('request.html')
@app.route('/redeem', methods=['GET', 'POST'])
def redeem_ride():
    error = None

    randNum = "%.8d" % random.randrange(1000000,99999999)
    return render_template('success.html').format(code=randNum)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/users', methods = ['GET', 'POST'])
def users():
    if request.method == 'POST':
        cust_id = create_customer()
        create_account(fieldList[valList[1]], cust_id)
    return render_template('users.html')
@app.route('/shelter', methods = ['GET', 'POST'])
def shelter():
    if requests.method == 'POST':
        create_shelter_account()
    return render_template('shelter.html')

app.run(debug=True, host='0.0.0.0', port = 9000)
