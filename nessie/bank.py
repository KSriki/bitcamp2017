# api.reimaginebanking.com/customers?key=0b2011ac5f42ea4fd1eebad7a0859110
#
# 0b2011ac5f42ea4fd1eebad7a0859110


import requests
import json

customerId = '58e8664ca73e4942cdafd277'
apiKey = '0b2011ac5f42ea4fd1eebad7a0859110'

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,
}
# Create a Savings Account
response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
    print('account created')
