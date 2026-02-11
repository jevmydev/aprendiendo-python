###
# 01 - Basic Web Scraping

# Veremos como hacer web scraping básico con Python
# El web scraping es el proceso de extraer información de sitios web. Es útil para recopilar datos, realizar análisis o automatizar tareas.
# ¡Es legal, siempre y cuando no maluses la información obtenida!

# pip3 install requests
###
import os
import requests # Importamos la dependencia para hacer peticiones
import re

os.system("clear")

url = "https://www.apple.com/es/shop/buy-mac/macbook-air"

response = requests.get(url) # Usado para consumo de API's y solicitar páginas web

if response.status_code == 200:
    print("La petición fue exitosa.")
    html_content = response.text

    prince_pattern = r'"amount":"(.*?)"' 
    match = re.search(prince_pattern, html_content)

    if match:
        print(f"El precio del producto es: {match.group(1)}") # Debe ser el grupo 1 que contiene el paréntesis (precio)