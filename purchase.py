import requests
import json
#customerId = '58e8664ca73e4942cdafd277'
apiKey = 'd3a4fbcc112ff3310de5014fae20e4be'
current_balance = 0
url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

def get_balance(_id):
	yy = "http://api.reimaginebanking.com/accounts/"
	yy = yy +"?key={}".format(apiKey)
	payload = {"_id":_id}
	account = requests.get(yy,data = json.dumps(payload), headers = {"content-type":"application/json"})
	print "here"
	oo = ""
	for u in account:
		oo = oo + u
		#print "\n\n\n"
	yp = json.loads(oo)
	for rr in yp:
		if rr['customer_id'] in _id:
			current_balance = float(rr['balance'])
			return (rr['balance'])
			
first_name = "james"
last_name = "bond"
street_number = "12345"
street_name = "Washington Avenue"
City = "Dallas"
State = "TN"
Zip = "34524"

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
yy = "http://api.reimaginebanking.com/accounts/"
yy = yy +"?key={}".format(apiKey)
#yy = yy +"/"
payload = {"_id":_id}
account = requests.get(yy,data = json.dumps(payload), headers = {"content-type":"application/json"})
print "here"
oo = ""
for u in account:
	oo = oo + u
	print "\n\n\n"
	#print u
yp = json.loads(oo)
for rr in yp:
	if rr['customer_id'] in _id:
		current_balance = float(rr['balance'])
		print "balance in the account = "+str(rr['balance'])
		

#payload = {"lat":0,"lng":0}
payload = {
  "merchant_id": "string",
  "medium": "balance",
  "purchase_date": "2017-04-09",
  "amount": 100,
  "description": "string"
}
try:
	url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey)
	merchant_id = '57cf75cea73e494d8675ec49'
	yy = "http://api.reimaginebanking.com/accounts/{" +_id+"}"
	y2 = yy+'/purchases?key={}'.format(apiKey)
	#yy = "http://api.reimaginebanking.com/accounts/{" +_id+'}/purchases?key={}'.format(_id,apiKey)
	#url = 'http://api.reimaginebanking.com/accounts/accounts?key={}'.format(_id,apiKey)
	payload = {
		"type": "Checking",
		"nickname" : first_name + last_name + "Checking",
		"balance" : current_balance,
		"rewards" : 0,
	}
	#debug this part
  uw = requests.post(y2, data = json.dumps(payload), headers = {"content-type":"application/json"})
	print uw
	if "404" in uw:
		print error
	else:
		print get_balance(_id)
except Exception as e:
	print "error"

