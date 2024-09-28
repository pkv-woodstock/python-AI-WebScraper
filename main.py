# Step 1: Create a very simple streamlit user interface
import streamlit as st

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
# Step 2: Grab data from the website that we want to scrape