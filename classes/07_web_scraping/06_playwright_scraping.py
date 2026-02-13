###
# 06 - Playwright scraping
#
# Usamos Playwright para hacer scraping de una página web.
# pip3 install pytest-playwright
# playwright install
###
import os
os.system("clear")

from urllib.parse import urljoin 
from playwright.sync_api import sync_playwright

url = "https://midu.dev"

with sync_playwright() as p:
    browser = p.chromium.launch() # headless=False, slow_mo=1000
    page = browser.new_page()
    page.goto(url)

    first_article = page.locator("article a").first
    first_article.click()

    page.wait_for_load_state()

    # first_image = page.locator("img").first
    # image_src = first_image.get_attribute("src")

    # print(f"La URL de la imagen es: {urljoin(url, image_src)}")

    first_image = page.locator("xpath=/html/body/div[1]/div/div[1]/img")
    image_src = first_image.get_attribute("src")
    print(f"La URL de la imagen es: {urljoin(url, image_src)}")

    content_of_course = page.locator("text='Contenido del curso'")
    print(content_of_course.inner_text())

    browser.close()