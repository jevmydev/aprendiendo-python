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

# Se pueden falsear User-Agents (firma del navegador) para falsear que eres Googlebot, por ejemplo,
# y así evitar bloqueos o restricciones en algunos sitios web.
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
}

url = "https://www.apple.com/es/macbook-pro/"
response = requests.get(url, headers=headers) 

if response.status_code == 200:
    print("La petición fue exitosa.")
    
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify()) # Imprime el HTML de forma legible

    title_tag = soup.title
    if title_tag:
        print("\nTítulo de la página:", title_tag.string)
    
    # # metas = soup.head.find_all("meta")
    # # print(metas)

    model = soup.find("h1")
    if model:
        print("Modelo:", model.text.strip())

    all_products = soup.find_all("li", class_="product-tile")

    for product in all_products:
        model = product.find(class_="product-tile-subheading")
        desc = product.find("p", class_="product-tile-positioning")

        if model and desc:
            print("\nModelo:", model.text)
            print("Descripción:", desc.text)

### Existen herramientas para saltarse el captcha:
# Pero una de dos, o te piden realizarlo manual y guardar el "permiso"
# O pueden usar user-agents y proxies para falsear

### Recomendación para evitar bloqueos y problemas por scraping:   
# Usar VPN para que no te puedan identificar por IP al farsear User-Agents.