import time
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
# Step 2: Grab data from the website that we want to scrape
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


# Extracting only body content from the scraped website
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

# Clean the body content(no need of script and style tage)
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    # get all of the text and then separate it with a new line
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

# Split the content due to the token contraint in the LLM
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
