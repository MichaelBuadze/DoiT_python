import requests

API_URL = "https://api.everrest.educata.dev/products"

def fetch_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []
