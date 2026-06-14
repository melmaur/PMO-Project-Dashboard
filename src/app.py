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


# Sidebar filters
st.sidebar.header("Filters")

owner_filter = st.sidebar.selectbox(
    "Owner",
    ["All"] + sorted(df["Owner"].unique().tolist())
)

status_filter = st.sidebar.selectbox(
    "Status",
    ["All"] + sorted(df["Status"].unique().tolist())
)

filtered_df = df.copy()

if owner_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Owner"] == owner_filter
    ]

if status_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Status"] == status_filter
    ]

# create display dataframe
df_display = filtered_df.copy()

df_display["Start Date"] = (
    df_display["Start Date"]
    .dt.strftime("%d-%b-%Y")
)

df_display["End Date"] = (
    df_display["End Date"]
    .dt.strftime("%d-%b-%Y")
)

# KPIs
avg_progress = round(
    filtered_df["Progress %"].mean(),
    1
)

completed = len(
    filtered_df[filtered_df["Status"] == "Completed"]
)

in_progress = len(
    filtered_df[filtered_df["Status"] == "In Progress"]
)

not_started = len(
    filtered_df[filtered_df["Status"] == "Not Started"]
)

# Summary variables
remaining_tasks = len(
    filtered_df[
        filtered_df["Status"] != "Completed"
    ]
)

active_tasks = len(
    filtered_df[
        filtered_df["Status"] == "In Progress"
    ]
)

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Overview",
        "Schedule",
        "Tasks",
        "RAID Log"
    ]
)


# tab 1 Overview

with tab1:

    st.title("CRM Transformation Program")

    st.subheader("Executive Summary")

    st.info(
       f"""
      Project completion is currently {avg_progress:.1f}%.

      There are {active_tasks} active task(s) in progress and
     {remaining_tasks} task(s) remaining before project completion.
     """
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
      "Project Progress",
      f"{avg_progress:.1f}%"
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

    status_counts = filtered_df["Status"].value_counts()

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

    st.plotly_chart(fig, use_container_width=True)


# tab2 - Schedule tab - Gantt Chart
with tab2:

    st.subheader("Project Timeline (Gantt View)")

    fig_gantt = px.timeline(
        filtered_df,
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


# tab3 - Tasks 
with tab3:

    st.subheader("Project Tasks")

    st.dataframe(df_display)



# the RAID tab (developed in Dashboard_V4)

with tab4:

    st.subheader("RAID Overview")

    # open file raid_log.xlsx

    RAID_FILE = PROJECT_ROOT / "data" / "raid_log.xlsx"

    raid_df = pd.read_excel(RAID_FILE)
    
  

    raid_type_filter = st.selectbox(
        "RAID Type",
        ["All"] + sorted(raid_df["Type"].unique().tolist())
    )
    
    raid_filtered = raid_df.copy()

    if raid_type_filter != "All":
         raid_filtered = raid_filtered[
            raid_filtered["Type"] == raid_type_filter
        ]

# debugging output

# st.write("PROJECT_ROOT:", PROJECT_ROOT)
# st.write("RAID_FILE:", RAID_FILE)
# st.write("FILE EXISTS:", RAID_FILE.exists())

    
    
    # this info box was for dashboard_V3 
    #    st.info(
    #    """
    #    RAID management module coming in the next release.

    #    Planned features:
    #    - Open Risks
    #    - Open Issues
    #    - Dependencies
    #    - Assumptions
    #    """
    #)

    # KPIs for RAID

    open_risks = len(
        raid_df[
            (raid_df["Type"] == "Risk") &
            (raid_df["Status"] == "Open")
            ]
    )

    
    open_issues = len(
        raid_df[
            (raid_df["Type"] == "Issue") &
            (raid_df["Status"] == "Open")
            ]
    )
    
    
    assumptions = len(
        raid_df[raid_df["Type"] == "Assumption"]
    )

    

    dependencies = len(
        raid_df[raid_df["Type"] == "Dependency"]
    )

# table

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Open Risks",
        open_risks
    )

    col2.metric(
        "Open Issues",
        open_issues
    )

    col3.metric(
        "Assumptions",
        assumptions
    )

    col4.metric(
        "Dependencies",
        dependencies
    )

    st.subheader("RAID Register")

    st.dataframe(
        raid_filtered,
        use_container_width=True
    )

    st.caption(
        f"Showing {len(raid_filtered)} RAID item(s)"
    )
