import requests

endpoint = "http://localhost:8000/api/products/51/update/"

data = {
    'title' : 'Fifty one',
    'content' : 'This is product number fifty one.',
    'price' : 51.01
}

get_response = requests.put(endpoint, json=data) 

print(get_response.json())