import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

st.title("Open Source Maintainer's First Mate")

repo = st.text_input("Enter GitHub Repo")

if st.button("Fetch Issues"):

    url = f"https://api.github.com/repos/{repo}/issues"

    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    for issue in data[:5]:
        st.write(issue["title"])
