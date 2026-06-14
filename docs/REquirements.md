# Requirements Document  

## PMO Project Dashboard – CRM Transformation Reporting Tool

---

## 1. Overview  

This document defines the functional requirements for a PMO reporting dashboard built using Python and Streamlit. The tool supports project tracking, visualization, and governance reporting.

---

## 2. Functional Requirements  

### FR1 – Project Data Loading  
- The system shall load project task data from an Excel file  
- The system shall load RAID log data from a separate Excel file  

---

### FR2 – KPI Dashboard  
- The system shall calculate and display:
  - Overall project progress
  - Number of completed tasks
  - Number of tasks in progress
  - Number of not started tasks  

---

### FR3 – Task Visualization  
- The system shall display all project tasks in a table format  
- The system shall allow filtering by:
  - Owner  
  - Status  

---

### FR4 – Project Timeline (Gantt View)  
- The system shall display tasks on a timeline  
- Each task shall have a start and end date  
- Tasks shall be color-coded by status  

---

### FR5 – RAID Log Module  
- The system shall display RAID items categorized as:
  - Risks  
  - Issues  
  - Assumptions  
  - Dependencies  
- The system shall allow filtering by RAID type  
- The system shall display KPI counts for each category  

---

### FR6 – Executive Summary  
- The system shall generate a text-based summary of:
  - Project progress  
  - Active tasks  
  - Remaining tasks  

---

### FR7 – Multi-Tab Navigation  
- The system shall provide navigation tabs for:
  - Overview  
  - Schedule  
  - Tasks  
  - RAID Log  

---

## 3. Non-Functional Requirements  

- The system shall run locally using Streamlit  
- The system shall load data from Excel files  
- The system shall respond interactively to user filters  
- The system shall support small-to-medium datasets efficiently  

---

## 4. Data Requirements  

### Project Task Dataset:
- Task ID  
- WBS Level  
- Task Name  
- Owner  
- Status  
- Start Date  
- End Date  
- Progress %  
- Dependency  

### RAID Dataset:
- ID  
- Type (Risk / Issue / Assumption / Dependency)  
- Description  
- Owner  
- Impact  
- Status  

---

## 5. Out of Scope  

- Database systems  
- Cloud infrastructure  
- Authentication and user roles  
- API integrations  

---

## 6. Acceptance Criteria  

The solution is considered acceptable if:

- All dashboards load without errors  
- KPIs reflect correct calculations  
- Gantt chart displays correctly  
- RAID module is functional and filterable  
- Documentation is complete and reproducible  