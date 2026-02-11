###
# 02 - Beautiful Soup

# Es un módulo de Python para extraer datos de archivos HTML y XML. 
# Proporciona métodos para navegar por la estructura del documento, buscar elementos específicos y extraer información de ellos.

# pip3 install bs4
###

import os
from bs4 import BeautifulSoup
import requests

os.system("clear")

url = "https://www.apple.com/es/shop/buy-mac/macbook-air"
response = requests.get(url)

if response.status_code == 200:
    print("La petición fue exitosa.")
    
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify()) # Imprime el HTML de forma legible

    title_tag = soup.title
    if title_tag:
        print("Título de la página:", title_tag.string)
    
    metas = soup.head.find_all("meta")
    print(metas)
