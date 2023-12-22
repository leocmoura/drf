import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'This is product crete by mixinsview'
}
get_response = requests.post(endpoint, json=data) 

print('--------------------')
print(get_response.json())
print('--------------------')
# print(get_response.body)