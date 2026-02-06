###
# 02 - Requests

# Como hacer peticiones a APIs con Python
# Con y sin dependencias
###
import os
os.system("clear")

api_posts = "https://jsonplaceholder.typicode.com/posts"

# Sin dependencias (Larga / Manual):
import urllib.request
import json

print("\nGET (sin dependencias): ")

try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode("utf-8"))

    print(json_data[0])

    response.close()

except urllib.error.URLError as e: # type: ignore
    print(f"Error en la solicitud: {e}")

# Con dependencias (request)
import requests

print("\nGET: ")

try:
    response = requests.get(api_posts)
    # print(response.json())
    json_data = response.json()
    print(json_data[0])

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

print("\nPOST: ")

try: 
    input_data = {
        "title": "Jeremy",
        "body": "Hi",
        "userId": 5
    }

    response = requests.post(api_posts, json=input_data)

    print(f"Código: {response.status_code}")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

print("\nPUT: ")

try: 
    input_data = {
        "title": "Jeremy",
        "body": "Hi",
        "userId": 1
    }

    response = requests.put(api_posts + "/1", json=input_data)

    print(f"Código: {response.status_code}")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# Diferencias entre PUT y PATCH:
# PUT: debemos pasarle todo el objeto (actualización)
# PATCH: le pasamos algunos datos del objeto a modificar (mucho más seguro)

# Métodos HTTP: Combina el GET con el POST, permitiendo mandar jsons en vez de query params