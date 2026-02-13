###
# 05 - Playwright
#
# Playwright permite crear navegadores sin cabeza (headless) para automatizar tareas de navegación web, como la extracción de datos, testeo de aplicaciones web.
# pip3 install pytest-playwright
# playwright install
###
import os
os.system("clear")

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()