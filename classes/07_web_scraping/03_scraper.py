###
# 03 - Scraper

# En este ejercicio, vamos a realizar web scraping como función de una URL dada.
# pip3 install bs4
###

import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin 
import requests

os.system("clear")

headers = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/144.0.0.0 Safari/537.36"
}

def scrape_url(url):
    response = requests.get(url) 

    if response.status_code == 200:
        print("La petición fue exitosa.")
        soup = BeautifulSoup(response.text, "html.parser")

        # Obtener todos los títulos <h1>
        titles_h1 = soup.find_all("h1")

        print("\nTítulos <h1> encontrados:" )
        for title in titles_h1: print(title.string)

        # Obtener todos los enlaces absolutos 
        links = soup.find_all("a")

        print("\nEnlaces <a> encontrados:" )
        for link in links:
            print("Enlace encontrado: ", urljoin(url, link.get("href")))
            # scrape_url(link)  # Llamada recursiva para scrapear cada enlace encontrado
        
        # Obtener el texto de la página
        page_text = soup.find("section", class_="main-content").get_text()

        print("\nTexto de la página:")
        print(page_text)
        
        # Obtener imagen de la página
        print("\nImagen encontrada:")
        image = soup.find("meta", {"property": "og:image"})
        if image:
            print("URL de la imagen: ", image.get("content"))



scrape_url("https://www.python.org/")