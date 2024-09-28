import time
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service


def scrape_website(website):
    print("Launching chrome driver...")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver1 = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver1.get(website)
        print("Page loaded...")
        html = driver1.page_source
        time.sleep(10)
        return html
    finally:
        driver1.quit()
