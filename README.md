\# 🛡️ GraphSentinel



\### Graph-Based Cybersecurity Investigation with FalkorDB



\*\*GraphSentinel transforms connected security records into an interactive graph to help investigators explore relationships between users, devices, and IP addresses.\*\*



\## 🎯 Problem Statement



Security events often appear across separate logs, making it difficult to understand how users, devices, and IP addresses are connected. Graph relationships can make these connections easier to investigate.



\## 💡 Our Solution



GraphSentinel uses \*\*FalkorDB\*\* to represent security entities and their relationships, with a \*\*Streamlit dashboard\*\* for exploring records, reviewing risk labels, and visualizing connections.



\## ✨ Key Features



\* \*\*CSV Ingestion:\*\* Import security records from a CSV file.

\* \*\*Graph-Based Data Model:\*\* Connect users, devices, and IP addresses.

\* \*\*Risk Overview:\*\* View users grouped by assigned risk levels.

\* \*\*User Investigation:\*\* Inspect a user's associated device and IP.

\* \*\*Relationship Visualization:\*\* Explore connections through a graph.

\* \*\*Investigation Guidance:\*\* Display suggested review actions based on risk labels.



\## 🏗️ Architecture



```text

Security CSV

&#x20;    |

&#x20;    v

import\_logs.py

&#x20;    |

&#x20;    v

&#x20;  FalkorDB

&#x20;    |

&#x20;    v

&#x20; app.py

&#x20;    |

&#x20;    v

Streamlit Dashboard

```



\### Graph Data Model



```text

(User)-\[:USED]->(Device)-\[:CONNECTED\_FROM]->(IP)

```



This model allows investigators to explore connected entities using graph queries.



\## 🧰 Technology Stack



\* \*\*Python\*\* — application logic

\* \*\*FalkorDB\*\* — graph database

\* \*\*Cypher\*\* — graph queries

\* \*\*Streamlit\*\* — interactive dashboard

\* \*\*Pandas\*\* — CSV processing and tabular data

\* \*\*NetworkX \& Matplotlib\*\* — relationship visualization



\## 📂 Project Structure



| File                | Purpose                                 |

| ------------------- | --------------------------------------- |

| `app.py`            | Interactive investigation dashboard     |

| `graph\_db.py`       | Database connection and test operations |

| `import\_logs.py`    | Imports CSV records into FalkorDB       |

| `investigator.py`   | Command-line risk investigation         |

| `seed\_data.py`      | Creates sample graph records            |

| `security\_logs.csv` | Sample input data                       |



\## 🚀 Run Locally



\### Prerequisites



Install Python and Docker Desktop.



\### 1. Start FalkorDB



Ensure Docker Desktop is running:



```powershell

docker start falkordb

```



\### 2. Set Up Python



Run these commands from the project directory:



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

pip install falkordb streamlit pandas networkx matplotlib

```



\### 3. Import Sample Records



```powershell

python import\_logs.py

```



The CSV must contain these columns:



```csv

user,device,ip,risk

```



\### 4. Launch the Dashboard



```powershell

streamlit run app.py

```



Open \*\*http://localhost:8501\*\* in your browser.



\## 🔎 Example Investigation Workflow



1\. Load security records from CSV.

2\. Explore the user-device-IP connections.

3\. Select a user in the dashboard.

4\. Review the assigned risk level and related entities.

5\. Use the displayed guidance to decide what activity needs further investigation.



\## 🔐 Responsible Use and Limitations



GraphSentinel is a \*\*hackathon prototype\*\*, not a production security detection system. Its current risk labels and scores are demonstration values and are not independently validated threat intelligence. An IP address or risk label alone does not prove malicious activity.



Production use would require authorized log integrations, evidence-based scoring, validated detection rules, access controls, and security testing.



\## 🛣️ Future Roadmap



\* Automated ingestion from authorized security sources

\* Evidence-based risk scoring

\* Threat-intelligence integrations

\* Detection of unusual graph patterns

\* Investigation history and alerting



\## 🤖 AI Assistance Disclosure



AI assistance was used for coding guidance, debugging, and documentation. The implementation should be reviewed and tested by the developer.



\## 👨‍💻 Project



\*\*Repository:\*\* https://github.com/shreem-bhargava36/GraphSentinel



