import requests
# import json

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
# endpoint = "http://localhost:8000/api/"
endpoint = "http://localhost:8000/api/post/"

get_response = requests.post(endpoint, json={'content': 'hello wooooooooooorld'}) 
# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)

print(get_response.json())
# print(get_response.status_code)