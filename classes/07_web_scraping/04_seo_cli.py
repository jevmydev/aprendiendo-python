###
# 04 - Seo CLI

# CLI (líneas de comandos) para analizar el SEO de una página web. 
# El programa debe aceptar una URL como argumento
# pip3 install bs4
###

import os
import requests
import argparse

from bs4 import BeautifulSoup
from urllib.parse import urljoin 

os.system("clear")

headers = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/144.0.0.0 Safari/537.36"
}

parser = argparse.ArgumentParser(description="Analiza el SEO de una página web a través de web scraping.")
parser.add_argument("url", help="La URL de la página web a analizar.")
args = parser.parse_args()
url = args.url

response = requests.get(url) 

if response.status_code == 200:
    ###
        # Terminal colorida con código ANSI
        # https://en.wikipedia.org/wiki/ANSI_escape_code

        # Formato: \033[<CÓDIGO_DE_COLOR>m"..."\033[0m
    ###
    print("\033[32mLa petición fue exitosa.\033[0m\n")
    soup = BeautifulSoup(response.text, "html.parser")

    print(f"Revisando la página: \033[36m{url}\033[0m")
    print("\033[46mAnalizando el SEO...\033[0m\n")

    title = soup.title.string
    if title:
        if len(title) <= 60:
            print(f"Título: {title}\n")
            print("\033[32mEl título es adecuado para SEO. ✅\033[0m")
        else:
            print("\033[31mEl título es demasiado largo para SEO. ❌\033[0m")
    else:
        print("Advertencia: No se encontró un título en la página.")

    # Extraer títulos h1
    titles = [title.text for title in soup.find_all("h1")]
    if not titles:
        print("\033[31mAdvertencia: No se encontraron títulos h1 en la página. ❌\033[0m")
    elif len(titles) > 1:
        print("\033[31mAdvertencia: Se encontraron múltiples títulos h1 en la página. ❌\033[0m")
    else:
        print(f"\033[32mTítulo h1: {titles[0]} ✅\033[0m")