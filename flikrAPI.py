import requests
import json
parameters={'api_key':'84d44160ef70100a8b26965a9e64872a','method':'flickr.photos.search','format':'json','nojsoncallback':'1','tags':'rivers','media':'photos','per_page':'5'}
base_url='https://api.flickr.com/services/rest'
flikr_response=requests.get(base_url,params=parameters)
print(flikr_response.url)
print(flikr_response.status_code)
flikr_data=flikr_response.json()
print(json.dumps(flikr_data,indent=2))