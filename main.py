# Step 1: Create a very simple streamlit user interface
import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_content
    # Expander textbook - allows us to expland it to view more content
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", clean_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)