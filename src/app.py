import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PMO Dashboard",
    layout="wide"
)

df = pd.read_excel(
    "../data/project_tasks.xlsx"
)

# KPIs
avg_progress = round(
    df["Progress %"].mean(),
    1
)

completed = len(
    df[df["Status"] == "Completed"]
)

in_progress = len(
    df[df["Status"] == "In Progress"]
)

not_started = len(
    df[df["Status"] == "Not Started"]
)

st.title("CRM Transformation Program")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Project Progress",
    f"{avg_progress}%"
)

col2.metric(
    "Completed Tasks",
    completed
)

col3.metric(
    "In Progress",
    in_progress
)

col4.metric(
    "Not Started",
    not_started
)

st.subheader("Project Tasks")

st.dataframe(df)