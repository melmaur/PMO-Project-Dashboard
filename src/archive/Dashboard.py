import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Load data
df = pd.read_excel("../data/project_tasks.xlsx")

# KPIs
avg_progress = round(df["Progress %"].mean(), 1)

status_counts = (
    df["Status"]
    .value_counts()
    .reset_index()
)

status_counts.columns = ["Status", "Count"]

# Create layout
fig = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "pie"}, {"type": "indicator"}]],
    subplot_titles=("Task Status", "Overall Progress")
)

# Pie chart
fig.add_trace(
    go.Pie(
        labels=status_counts["Status"],
        values=status_counts["Count"]
    ),
    row=1,
    col=1
)

# Gauge
fig.add_trace(
    go.Indicator(
        mode="gauge+number",
        value=avg_progress,
        title={"text": "Project Progress"}
    ),
    row=1,
    col=2
)

fig.update_layout(
    title="CRM Transformation Program Dashboard",
    height=600
)

fig.write_html(
    "../dashboards/plotly_dashboard.html"
)

print("Plotly dashboard created.")