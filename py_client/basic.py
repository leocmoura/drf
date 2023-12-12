import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.ge t(endpoint, params={"abc": 123}, json={"query": "hello"}) 
# print(get_response.text)
# print(get_response.status_code)

print(get_response.json())
# print(get_response.status_code)