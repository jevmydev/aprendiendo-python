###
# 02 - Request

# Como hacer peticiones a APIs con Python
# Con y sin dependencias
###
import os
os.system("clear")

# Sin dependencias (Larga / Manual):
import urllib.request
import json

api_posts = "https://jsonplacehasolder.typicode.com/posts"

try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode("utf-8"))

    # print(json_data)

    response.close()

except urllib.error.URLError as e: # type: ignore
    print(f"Error en la solicitud: {e}")

# Con dependencias (request)
import requests

print("\nGET: ")

api_posts = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts)
print(response.json())