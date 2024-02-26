import requests

url = 'http://localhost:5000/get-current-time'
api_key = '12345'

headers = {
  'Authorization': api_key,
  'Content-Type': 'application/json',
}

try:
  response = requests.post(url, headers=headers)

  if response.status_code == 200:
    response_data = response.json()
    current_time = response_data.get('currentTime')
    print("Current time received from the API:", current_time)
  else:
    print("Error:", response.status_code, response.text)  # Include response text
except requests.exceptions.RequestException as e:
  print("Error On request:", e)
