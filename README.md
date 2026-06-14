# PMO-Project-Dashboard (Streamlit)
PMO governance and reporting package for a CRM implementation project including planning artifacts, risk management, and Python-based dashboard analytics.
A Python-based interactive dashboard simulating a PMO reporting environment for a CRM implementation project.
Built to demonstrate project tracking, governance reporting, and executive-level visibility using real-world PMO concepts.

# Project Overview

This project simulates a PMO (Project Management Office) reporting system for a CRM transformation initiative.

It was built progressively to replicate how PMO teams track:

Project progress
Task delivery
Schedule adherence
Risks, issues, assumptions, and dependencies (RAID)
Executive reporting

-> The solution transforms a simple Excel project plan into an interactive analytics dashboard using Streamlit.

# Objectives

Simulate a real PMO reporting environment
Transform Excel-based project tracking into a dashboard
Build executive-level KPIs and visual reporting
Introduce RAID governance tracking
Practice data analysis and dashboard design in Python

# Tech Stack

Python
Streamlit
Pandas
Plotly
Excel (data source)

# 📂 Project Structure
```
PMO-Project-Dashboard/
│
├── data/
│   ├── project_tasks.xlsx
│   ├── raid_log.xlsx
│
├── src/
│   └── app.py
│
├── images/
│   ├── dashboard_v1.png
│   ├── dashboard_v2.png
│   ├── dashboard_v4.png
│
├── requirements.txt
└── README.md
```

# 📈 Project Evolution

🟢 V1 – Basic Reporting Dashboard

Initial version focused on transforming Excel data into simple KPIs and a table view.

📸 Screenshot:


🔵 V2 – Visual Analytics Layer

Added:

Task status distribution (pie chart)
Project timeline (Gantt chart)
Improved KPI visualization

📸 Screenshot:


🟣 V3 – Multi-Tab Interface

Introduced structured navigation using Streamlit tabs:

Overview
Schedule
Task Register
RAID placeholder

This improved usability and mirrored real PMO reporting tools.

🔴 V4 – RAID Governance Module

Final version includes a full RAID log system:

RAID Tracking:
Risks
Issues
Assumptions
Dependencies
Features:
KPI summary of RAID items
Interactive filtering
Structured governance view

📸 Screenshot:


📊 Key Features
📌 Executive Overview
Project completion tracking
KPI cards (progress, status breakdown)
High-level summary insights
📅 Schedule Management
Gantt chart timeline
Task-level visibility
Status-based color coding
📋 Task Register
Full project task list
Filtering by owner and status
Excel-backed data model
⚠️ RAID Log
Risk & issue tracking
Dependency mapping
Governance reporting structure
🧠 Key Learning Outcomes

This project demonstrates:

Data transformation from Excel to analytics dashboard
PMO reporting structure design
KPI definition for project tracking
Interactive dashboard development
RAID governance concepts
Real-world project storytelling
▶️ How to Run
pip install -r requirements.txt
streamlit run src/app.py

Then open:  http://localhost:8501

📌 Ideas for Future Improvements

Executive automated status report (V5 concept)
Export to PDF for steering committee reports
Database integration (optional)
Cloud deployment (Streamlit Cloud)


👤 Author

Mauro
Aspiring PMO / Project Analyst
Focus: Project governance, reporting & data analytics

⭐ Why this project matters

This is not just a dashboard.

It simulates how PMOs:

track delivery
monitor risk
communicate status to stakeholders
support decision-making



