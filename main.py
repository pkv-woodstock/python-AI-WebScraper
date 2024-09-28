# Step 1: Create a very simple streamlit user interface
import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    print(result)
# Step 2: Grab data from the website that we want to scrape