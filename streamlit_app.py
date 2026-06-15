import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Supply Chain Forecasting",
    page_icon="📦",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

DATA_PATH = Path(".")

REQUIRED_FILES = {
    "forecast": "forecast_results.csv",
    "metrics": "model_metrics.csv",
    "inventory": "inventory_results.csv",
    "projection": "inventory_projection.csv",
    "scenarios": "forecast_scenarios.csv",
    "kpis": "inventory_kpis.csv"
}


@st.cache_data
def load_data():

    data = {}

    missing = []

    for key, file in REQUIRED_FILES.items():

        path = DATA_PATH / file

        if path.exists():

            data[key] = pd.read_csv(path)

        else:

            missing.append(file)

    return data, missing


data, missing_files = load_data()

# ==========================================================
# HEADER
# ==========================================================

st.title(
    "📦 Supply Chain Demand Forecasting & Inventory Optimization"
)

st.markdown(
    """
    Executive dashboard developed using the
    M5 Forecasting dataset.

    Forecasting → Inventory Planning → Operational Decisions
    """
)

# ==========================================================
# FILE VALIDATION
# ==========================================================

if missing_files:

    st.error(
        f"Missing files: {', '.join(missing_files)}"
    )

    st.stop()

# ==========================================================
# DATAFRAMES
# ==========================================================

forecast = data["forecast"]
metrics = data["metrics"]

inventory = data["inventory"]
projection = data["projection"]

scenarios = data["scenarios"]
kpis = data["kpis"]

# ==========================================================
# DATE
# ==========================================================

if "Date" in forecast.columns:

    forecast["Date"] = pd.to_datetime(
        forecast["Date"]
    )

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("Dashboard Controls")

selected_metric = st.sidebar.selectbox(
    "Performance Metric",
    ["MAE", "RMSE"]
)

# ==========================================================
# EXECUTIVE KPIS
# ==========================================================

st.subheader("Executive Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Mean Demand",
    f"{inventory['Mean_Demand'].iloc[0]:,.0f}"
)

col2.metric(
    "Safety Stock",
    f"{inventory['Safety_Stock'].iloc[0]:,.0f}"
)

col3.metric(
    "Reorder Point",
    f"{inventory['ROP'].iloc[0]:,.0f}"
)

col4.metric(
    "EOQ",
    f"{inventory['EOQ'].iloc[0]:,.0f}"
)

# ==========================================================
# FORECAST
# ==========================================================

st.subheader("Demand Forecast")

fig_forecast = go.Figure()

if "Date" in forecast.columns:

    x_axis = forecast["Date"]

else:

    x_axis = forecast.index

fig_forecast.add_trace(
    go.Scatter(
        x=x_axis,
        y=forecast["Actual"],
        name="Actual"
    )
)

fig_forecast.add_trace(
    go.Scatter(
        x=x_axis,
        y=forecast["XGBoost"],
        name="XGBoost"
    )
)

fig_forecast.add_trace(
    go.Scatter(
        x=x_axis,
        y=forecast["LightGBM"],
        name="LightGBM"
    )
)

fig_forecast.add_trace(
    go.Scatter(
        x=x_axis,
        y=forecast["Prophet"],
        name="Prophet"
    )
)

fig_forecast.update_layout(
    height=550,
    xaxis_title="Date",
    yaxis_title="Demand"
)

st.plotly_chart(
    fig_forecast,
    use_container_width=True
)

# ==========================================================
# INVENTORY PROJECTION
# ==========================================================

st.subheader("Inventory Projection")

fig_inventory = go.Figure()

fig_inventory.add_trace(
    go.Scatter(
        y=projection["inventory"],
        name="Inventory Level"
    )
)

fig_inventory.add_hline(
    y=inventory["ROP"].iloc[0],
    line_dash="dash",
    annotation_text="Reorder Point"
)

fig_inventory.update_layout(
    title="Inventory Projection",
    xaxis_title="Forecast Horizon (Days)",
    yaxis_title="Inventory Units",
    height=500
)

st.plotly_chart(
    fig_inventory,
    use_container_width=True
)

# ==========================================================
# SCENARIO ANALYSIS
# ==========================================================

st.subheader("Scenario Analysis")

scenario_columns = [
    c for c in scenarios.columns
    if c.lower() in [
        "optimistic",
        "base",
        "pessimistic"
    ]
]

if len(scenario_columns) > 0:

    fig_scenario = go.Figure()

    for col in scenario_columns:

        fig_scenario.add_trace(
            go.Scatter(
                y=scenarios[col],
                name=col
            )
        )

    fig_scenario.update_layout(
        title="Demand Forecast Scenarios",
        xaxis_title="Forecast Horizon (Days)",
        yaxis_title="Demand Units",
        legend_title="Scenario",
        height=500
    )

    st.plotly_chart(
        fig_scenario,
        use_container_width=True
    )

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

st.subheader("Model Performance")

fig_perf = px.bar(
    metrics,
    x="Model",
    y=selected_metric,
    text=selected_metric
)

fig_perf.update_layout(
    height=500
)

st.plotly_chart(
    fig_perf,
    use_container_width=True
)

st.dataframe(
    metrics,
    use_container_width=True
)

# ==========================================================
# KPI TABLE
# ==========================================================

st.subheader("Inventory KPIs")

st.dataframe(
    kpis,
    use_container_width=True
)

# ==========================================================
# INSIGHTS
# ==========================================================

st.subheader("Automated Insights")

best_model = (
    metrics
    .sort_values("MAE")
    .iloc[0]["Model"]
)

coverage = inventory["Coverage"].iloc[0]

rop = inventory["ROP"].iloc[0]

eoq = inventory["EOQ"].iloc[0]

st.success(
    f"""
    Best Forecast Model: {best_model}

    Inventory Coverage: {coverage:.1f} days

    Recommended Reorder Point: {rop:,.0f}

    Recommended EOQ: {eoq:,.0f}
    """
)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    """
    Supply Chain Analytics Project

    Demand Forecasting + Inventory Optimization

    Models: Prophet, XGBoost, LightGBM
    """
)