import requests
import pprint

url = 'https://41a9v8ivkj.execute-api.us-east-1.amazonaws.com/dev/person'

ret = requests.get(url)
print ('Checking if status code is 200: ', ret.status_code)
print ('Response headers: ', ret.headers)
