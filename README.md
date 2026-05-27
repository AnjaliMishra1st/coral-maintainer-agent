# 🏴‍☠️ Open Source Maintainer's First Mate

A Coral-inspired repository analysis assistant built for the **Pirates of the Coral-bean Hackathon**.

This project helps open-source maintainers inspect repository health, analyze GitHub issues, detect recurring engineering problems, and explore SQL-style workflows inspired by Coral.

---

##  Features

- Fetches live GitHub repository issues
- Detects UI, server, fix, and AI-related issue patterns
- Generates maintainer insights dashboard
- Demonstrates Coral-inspired SQL-style querying
- Uses real-time GitHub API data

---

## Coral-style SQL Queries

```sql
SELECT *
FROM github.issues
WHERE type = 'bug';
```

```sql
SELECT *
FROM github.pull_requests
WHERE status = 'open';
```

```sql
SELECT *
FROM github.issues
WHERE title LIKE '%ui%';
```

---

## Screenshots

![Homepage](Screenshot%202026-05-27%20180357.png)

![Insights](Screenshot%202026-05-27%20180641.png)

![Project Demo](Screenshot%202026-05-27%20181701.png)

---

## ⚙️ Tech Stack

- Python
- Streamlit
- GitHub REST API
- Git & GitHub

---

## Run Locally

```bash
git clone https://github.com/AnjaliMishra1st/coral-maintainer-agent.git

cd coral-maintainer-agent

python -m venv venv

source venv/Scripts/activate

pip install streamlit requests python-dotenv

streamlit run app.py
```

---

## Hackathon Theme Alignment

This project demonstrates a Coral-inspired workflow where repository data can be explored using SQL-style querying concepts for maintainers and engineering teams.

---

##  Author

Anjali Mishra

GitHub: https://github.com/AnjaliMishra1st
