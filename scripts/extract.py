import requests

def fetch_products():
    URL = "https://fakestoreapi.com/products"
    response = requests.get(URL)
    response.raise_for_status()
    return response

