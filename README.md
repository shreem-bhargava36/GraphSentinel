\# GraphSentinel 🛡️

\### Graph-Based Security Threat Investigation



\## Overview

GraphSentinel is a cybersecurity prototype built with FalkorDB that investigates relationships between users, devices, and IP addresses. Its interactive dashboard helps security analysts explore connected entities and identify potentially high-risk users.



\## Problem

Traditional security logs can make it difficult to discover relationships between users, devices, and IP addresses.



\## Solution

GraphSentinel represents security records as a graph, enabling relationship-based investigation through an interactive dashboard.



\## Features

\- CSV-based security log ingestion

\- Graph storage using FalkorDB

\- Interactive Streamlit dashboard

\- User, device, and IP relationship visualization

\- Risk-level filtering and investigation

\- Recommended actions for reviewing suspicious activity



\## Technology Stack

\- Python

\- FalkorDB

\- Cypher

\- Streamlit

\- Pandas

\- NetworkX

\- Matplotlib



\## Graph Data Model

(User)-\[:USED]->(Device)-\[:CONNECTED\_FROM]->(IP)



\## Project Structure

\- app.py — Interactive dashboard

\- graph\_db.py — Database connection

\- import\_logs.py — CSV ingestion

\- investigator.py — User risk investigation

\- seed\_data.py — Sample graph data

\- security\_logs.csv — Sample security records



\## Installation and Setup



\### 1. Prerequisites

Install Python and Docker Desktop.



\### 2. Start FalkorDB

Ensure Docker Desktop is running, then execute:



&#x20;   docker start falkordb



\### 3. Install Dependencies

From the project directory, execute:



&#x20;   python -m venv .venv

&#x20;   .\\.venv\\Scripts\\Activate.ps1

&#x20;   pip install falkordb streamlit pandas networkx matplotlib



\### 4. Import Security Records



&#x20;   python import\_logs.py



The CSV file must contain these columns:



&#x20;   user,device,ip,risk



Example:



&#x20;   Alice,Unknown Laptop,185.220.101.5,high

&#x20;   David,Office Computer,192.168.1.50,medium

&#x20;   Priya,Work Laptop,10.0.0.25,low

&#x20;   Rahul,Unknown Phone,45.155.205.233,high



\### 5. Launch the Dashboard



&#x20;   streamlit run app.py



Open http://localhost:8501 in your browser.



\## Investigation Workflow

1\. Import security records from CSV.

2\. Explore user-device-IP relationships.

3\. Review assigned risk levels.

4\. Visualize connections in the graph.

5\. Investigate suspicious activity before taking action.



\## Limitations

This is a hackathon prototype. Risk labels and scores are demonstration values, not verified threat intelligence. The application does not independently prove that any user or IP address is malicious.



Production deployment would require authorized security-log integrations, evidence-based risk scoring, validated detection rules, and security testing.



\## Future Improvements

\- Automated security-log ingestion

\- Evidence-based risk scoring

\- IP reputation integrations

\- Unusual connection detection

\- Investigation history and alerting



\## AI Disclosure

AI assistance was used for coding guidance, debugging, and documentation. The developer should review and test the project before deployment.



