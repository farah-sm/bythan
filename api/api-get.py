import requests

API_URL="https://randomuser.me/api"
response = requests.get('https://randomuser.me/api')
print(response.json()['results'][0]['location']['city'])