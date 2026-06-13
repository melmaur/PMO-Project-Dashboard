import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="PMO Dashboard",
    layout="wide"
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "project_tasks.xlsx"

# debugging output

# st.write("PROJECT_ROOT:", PROJECT_ROOT)
# st.write("DATA_FILE:", DATA_FILE)
# st.write("FILE EXISTS:", DATA_FILE.exists())

df = pd.read_excel(DATA_FILE)

# convderts to proper dates
df["Start Date"] = pd.to_datetime(df["Start Date"])
df["End Date"] = pd.to_datetime(df["End Date"])

df_display = df.copy()

df_display["Start Date"] = df_display["Start Date"].dt.strftime("%d-%b-%Y")
df_display["End Date"] = df_display["End Date"].dt.strftime("%d-%b-%Y")


st.set_page_config(
    page_title="PMO Dashboard",
    layout="wide"
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

st.dataframe(df_display)