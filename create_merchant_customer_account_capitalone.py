import requests
import json
#customerId = '58e8664ca73e4942cdafd277'
apiKey = '0b2011ac5f42ea4fd1eebad7a0859110'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)


first_name = "james"
last_name = "bond"
street_number = "12345"
street_name = "Washington Avenue"
City = "Dallas"
State = "TN"
Zip = "34524"

payload = {
    "first_name": first_name,
    "last_name": last_name,
    "address": {
        "street_number": street_number,
        "street_name": street_name,
        "city": City,
        "state": State,
        "zip": Zip
    }
}

# Create a Savings Account
response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)


#print (response)
if response.status_code == 201:
    print('account created')
   

customers = requests.get(url)
#print type(customers)
customer1 = ""
for customer in customers:
	customer1 = customer1+customer
	#print customer
	#print "\n\n\n"
id = ""
for p in json.loads(customer1):
	if p['last_name'] in last_name:
		if p['first_name'] in first_name:
			if p['address']['street_number'] in street_number:
				if p['address']['city'] in City:
					_id = p['_id']
					break

print _id
message = "hello"
url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(_id,apiKey)
payload = {
		"type": "Checking",
		"nickname" : first_name + last_name + "Checking",
		"balance" : 10000,
		"rewards" : 0,
	}
response = requests.post(url, data = json.dumps(payload), headers = {"content-type":"application/json"})
if response.status_code == 201:
	print "account_created"
	#	print("account created")

url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey)
payload = {"name":"exterm", "category":["exterminator"], "address":{"street_number":"BITCAMP","street_name":"UMD","city":"College Park", "state":"Maryland", "zip":"01002"}, "geocode":{"lat":0,"lng":0}}
response = requests.post(url, data = json.dumps(payload), headers = {"content-type":"application/json"})
if response.status_code == 400:
	print "merchant_created"
