import requests

endpoint = "http://localhost:8000/api/products/"
# login
# http://localhost:8000/admin/
# session -> post data
# selenion

data = {
    'title': 'This is product number ten create by mixinsview',
    'content': ''
}
get_response = requests.post(endpoint, json=data) 

print('--------------------')
print(get_response.json())
print('--------------------')
# print(get_response.body)