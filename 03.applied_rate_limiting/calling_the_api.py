import requests

url = 'http://127.0.0.1:5000/check-prime'
headers = {'Authorization': '12345'}
data = {'number': 172983479832623897492387592384682937659382477}

response = requests.post(url, json=data, headers=headers)
print(response.json())
