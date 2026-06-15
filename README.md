# Supply Chain Demand Forecasting & Inventory Optimization

<p align="center">
  <img src="images/M5_Forecasting Banner.png" alt="Supply Chain Demand Forecasting & Inventory Optimization">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-Forecasting-success?style=for-the-badge)
![LightGBM](https://img.shields.io/badge/LightGBM-Gradient%20Boosting-green?style=for-the-badge)
![Prophet](https://img.shields.io/badge/Prophet-Time%20Series-blueviolet?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)
![Supply Chain](https://img.shields.io/badge/Supply%20Chain-Analytics-00C853?style=for-the-badge)

</p>

---

## 📌 Executive Summary

This project demonstrates an end-to-end Supply Chain Analytics solution built using the **M5 Forecasting Dataset (Walmart)**.

The objective is to transform historical sales data into actionable business decisions through:

- Demand Forecasting
- Inventory Optimization
- Scenario Analysis
- Executive Decision Support

The solution simulates a real-world Data Science workflow used in Supply Chain organizations, connecting machine learning forecasts with operational inventory planning.

### Key Business Result

✅ **37% reduction in forecast error** compared to a baseline forecasting approach.

This improvement enables:

- Reduced stockouts
- Better inventory allocation
- Improved replenishment decisions
- Lower inventory holding costs

---

# 🎯 Business Problem

Demand forecasting is one of the most critical challenges in Supply Chain Management.

Inaccurate forecasts often lead to:

- Excess inventory
- Lost sales
- Poor service levels
- Inefficient replenishment planning

This project addresses these challenges by combining machine learning forecasting models with inventory optimization techniques.

---

# 🛠 Solution Architecture

```text
Raw Sales Data
       │
       ▼
EDA & Data Understanding
       │
       ▼
Feature Engineering
       │
       ▼
Forecasting Models
       │
       ▼
Inventory Optimization
       │
       ▼
Executive Dashboard
       │
       ▼
Business Decision Support
```

---

# 📊 Dataset

### M5 Forecasting Dataset (Walmart)

The M5 Forecasting dataset is one of the most recognized forecasting benchmarks in the Data Science community.

Main files used:

```text
calendar.csv
sales_train_validation.csv
sales_train_evaluation.csv
sell_prices.csv
```

The dataset contains:

- Historical sales
- Product hierarchy
- Store hierarchy
- Calendar information
- Price history

---

# Project Structure

```text
├── Notebook_01_EDA.ipynb
├── Notebook_02_Feature_Engineering.ipynb
├── Notebook_03_Forecasting.ipynb
├── Notebook_04_Inventory_Optimization.ipynb
├── Notebook_05_Executive_Dashboard.ipynb

├── streamlit_app.py

├── forecast_results.csv
├── model_metrics.csv

├── inventory_results.csv
├── inventory_projection.csv
├── forecast_scenarios.csv
├── inventory_kpis.csv

└── README.md
```

---

# Project Workflow

## Notebook 01 — Exploratory Data Analysis (EDA)

Objectives:

- Understand demand behavior
- Analyze seasonality
- Identify trends
- Evaluate calendar effects
- Assess data quality

Deliverables:

- Sales analysis
- Category analysis
- Store analysis
- Event analysis

---

## Notebook 02 — Feature Engineering

Features created:

### Lag Features

```python
lag_7
lag_28
```

### Rolling Features

```python
rolling_mean_7
rolling_mean_28

rolling_std_7
rolling_std_28
```

### Calendar Features

```python
day_of_week
month
week
quarter
```

Purpose:

Improve forecasting accuracy through temporal and demand-based patterns.

---

## Notebook 03 — Demand Forecasting

Models evaluated:

### Baseline

- Naive Forecast

### Statistical Model

- Prophet

### Machine Learning Models

- XGBoost
- LightGBM

### Evaluation Metrics

- MAE
- RMSE

### Results

| Model | MAE |
|---------|---------:|
| Naive | 530.57 |
| Prophet | 657.66 |
| XGBoost | **333.68** |
| LightGBM | 365.12 |

### Best Model

🏆 **XGBoost**

Forecast error reduction:

```text
37.1%
```

compared to the Naive Forecast baseline.

---

## Notebook 04 — Inventory Optimization

Forecast outputs were converted into operational inventory recommendations.

Techniques applied:

- Safety Stock
- Reorder Point (ROP)
- Economic Order Quantity (EOQ)
- Inventory Coverage
- Scenario Planning

Outputs generated:

```text
inventory_results.csv

inventory_projection.csv

forecast_scenarios.csv

inventory_kpis.csv
```

---

## Notebook 05 — Executive Dashboard

An executive dashboard was developed to communicate business insights.

Dashboard Components:

- Executive KPIs
- Forecast vs Actual
- Inventory Projection
- Scenario Analysis
- Model Performance
- Inventory Recommendations

---

# Technologies

## Programming

- Python
- SQL

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-Learn
- XGBoost
- LightGBM
- Prophet

## Visualization

- Plotly
- Matplotlib

## Dashboard

- Streamlit

---

# Business Impact

### Forecast Accuracy Improvement

| Metric | Result |
|----------|----------:|
| Baseline MAE | 530.57 |
| XGBoost MAE | 333.68 |
| Improvement | **37.1%** |

### 💡 Operational Benefits

- Reduced stockout risk
- Better replenishment decisions
- Improved inventory coverage
- Lower inventory costs
- Enhanced demand visibility

---

# Executive Dashboard

The final solution includes a Streamlit dashboard integrating forecasting and inventory planning into a single decision-support interface.

Main capabilities:

- Forecast monitoring
- Inventory tracking
- Scenario simulation
- Inventory KPI monitoring
- Automated insights

---

# Future Enhancements

Potential next steps:

- Multi-store forecasting
- Multi-category forecasting
- Service level optimization
- Supply chain network optimization
- AWS deployment
- MLOps pipeline
- Automated retraining
- Real-time forecasting

---

# Author

## Luis Felipe Vendramim

Data Science | Machine Learning | Forecasting | Supply Chain Analytics

LinkedIn: *https://www.linkedin.com/in/luís-felipe-vendramim-msc-17b67736/*

GitHub: *https://github.com/luisfelipevendramim*

---

⭐ If you found this project interesting, feel free to star the repository.