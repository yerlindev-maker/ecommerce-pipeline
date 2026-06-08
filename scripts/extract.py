import requests
import pandas as pd
import json

URL = "https://fakestoreapi.com/products"

response = requests.get(URL)

response.raise_for_status()

data = response.json()

with open("/home/yerlin/projects/ecommerce-data/data/raw_products.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"Productos extraídos: {len(data)}")
print(f"Columnas disponibles: {list(data[0].keys())}")