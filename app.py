import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

st.set_page_config(
    page_title="Open Source Maintainer's First Mate",
    layout="wide"
)

st.title("🏴‍☠️ Open Source Maintainer's First Mate")

st.markdown("""
Coral-inspired repository analysis assistant for open-source maintainers.
Analyze repository issues, detect problem patterns, and explore SQL-style workflows.
""")

repo = st.text_input(
    "Enter GitHub Repository (example: meshery/meshery)"
)

if st.button("Analyze Repository"):

    url = f"https://api.github.com/repos/{repo}/issues"

    headers = {
        "Authorization": f"token {github_token}"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    if isinstance(data, dict) and data.get("message"):
        st.error("Invalid repository or GitHub API issue.")
    else:

        issue_titles = []

        st.subheader("📌 Latest Issues")

        for issue in data[:5]:
            title = issue["title"]
            issue_titles.append(title)
            st.write("•", title)

        ui_issues = 0
        server_issues = 0
        fix_issues = 0
        ai_issues = 0

        for title in issue_titles:

            lower_title = title.lower()

            if "ui" in lower_title:
                ui_issues += 1

            if "server" in lower_title:
                server_issues += 1

            if "fix" in lower_title:
                fix_issues += 1

            if "ai" in lower_title:
                ai_issues += 1

        st.subheader("📊 Maintainer Insights")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("UI Issues", ui_issues)
        col2.metric("Server Issues", server_issues)
        col3.metric("Fix Requests", fix_issues)
        col4.metric("AI-related", ai_issues)

        st.subheader("⚠️ Repository Health Analysis")

        if ui_issues > 0:
            st.warning(
                "Frontend/UI instability detected."
            )

        if server_issues > 0:
            st.warning(
                "Server-side reliability issues detected."
            )

        if fix_issues >= 2:
            st.error(
                "Repository currently handling multiple fixes."
            )

        if ai_issues > 0:
            st.info(
                "AI-related development activity detected."
            )

        st.success(
            "Repository analysis completed successfully."
        )

        st.subheader("🪸 Coral-style SQL Queries")

        st.code("""
SELECT *
FROM github.issues
WHERE type = 'bug'
ORDER BY created_at DESC;
""", language="sql")

        st.code("""
SELECT *
FROM github.pull_requests
WHERE status = 'open';
""", language="sql")

        st.code("""
SELECT *
FROM github.issues
WHERE title LIKE '%ui%';
""", language="sql")

        st.code("""
SELECT *
FROM github.issues
WHERE title LIKE '%server%';
""", language="sql")

        st.subheader("🚀 Why This Matters")

        st.markdown("""
This project demonstrates a Coral-inspired workflow where repository data
can be explored using SQL-style querying patterns for maintainers,
contributors, and engineering teams.
""")
