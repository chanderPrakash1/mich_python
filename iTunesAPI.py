import requests
import json
parameters={'terms':'jack johnson'}
base_url='https://itunes.apple.com/search'
iTunes_response=requests.get(base_url,params=parameters)
print(iTunes_response.url)
print(iTunes_response.status_code)
print(iTunes_response.text)
iTunes_data=json.loads(iTunes_response.text)
print(iTunes_data)