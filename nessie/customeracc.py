# api.reimaginebanking.com/customers?key=0b2011ac5f42ea4fd1eebad7a0859110
#
# 0b2011ac5f42ea4fd1eebad7a0859110


import requests
import json

#customerId = '58e8664ca73e4942cdafd277'
apiKey = '0b2011ac5f42ea4fd1eebad7a0859110'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

customers = request.get(url)


payload = {
    "first_name": "james",
    "last_name": "bond",
    "address": {
        "street_number": "12345",
        "street_name": "Washington Avenue",
        "city": "dallas",
        "state": "tn",
        "zip": "34524"
    }
}

# Create a Savings Account
response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)


print (response)
if response.status_code == 201:
    print('account created')
