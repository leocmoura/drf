import requests

endpoint = "http://localhost:8000/api/products/2/update/"

data = {
    'title' : 'Second',
    'content' : 'This is product number two.',
    'price' : 22.22
}

get_response = requests.put(endpoint, json=data) 

print(get_response.json())