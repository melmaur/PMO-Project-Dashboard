import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

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

# converts to proper dates
df["Start Date"] = pd.to_datetime(df["Start Date"])
df["End Date"] = pd.to_datetime(df["End Date"])

df_display = df.copy()

df_display["Start Date"] = df_display["Start Date"].dt.strftime("%d-%b-%Y")
df_display["End Date"] = df_display["End Date"].dt.strftime("%d-%b-%Y")


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
    f"{avg_progress: .1f}%"
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

st.subheader("Project Health Overview")

status_counts = df["Status"].value_counts()

# pie chart
fig = px.pie(
    values=status_counts.values,
    names=status_counts.index,
    title="Task Status Distribution",
    hole=0.4,
    color=status_counts.index,
    color_discrete_map={
        "Completed": "#2E7D32",
        "In Progress": "#1565C0",
        "Not Started": "#B0BEC5"
    }
)

fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(size=12)
)

fig.update_traces(
    textinfo="percent+label"
)

# Gantt Chart
st.subheader("Project Timeline (Gantt View)")

fig_gantt = px.timeline(
    df,
    x_start="Start Date",
    x_end="End Date",
    y="Task Name",
    color="Status",
    color_discrete_map={
        "Completed": "#2E7D32",     # dark green (professional)
        "In Progress": "#1565C0",   # deep blue
        "Not Started": "#B0BEC5"     # grey (neutral)
    }
)

fig_gantt.update_layout(
    title="CRM Implementation Timeline",
    font=dict(size=12),
    plot_bgcolor="white",
    paper_bgcolor="white",
)

fig_gantt.update_xaxes(
    showgrid=True,
    gridcolor="lightgrey"
)

fig_gantt.update_yaxes(
    autorange="reversed",
    showgrid=False
)

fig_gantt.update_layout(height=500)

fig_gantt.update_yaxes(autorange="reversed")

st.plotly_chart(fig_gantt, use_container_width=True)


st.plotly_chart(fig, use_container_width=True)

st.subheader("Project Tasks")

st.dataframe(df_display)