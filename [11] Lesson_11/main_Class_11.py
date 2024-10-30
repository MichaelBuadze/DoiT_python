import requests

response = requests.get('https://www.example.com')

if response.status_code == 200:
    print(response.text)
else:
    print('Request failed with status code:', response.status_code)