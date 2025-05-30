#  Global Transport Trends Dashboard

An interactive Streamlit dashboard for exploring **international passenger and freight transport data** across Canada, USA, Germany, Singapore, Japan, and the UK.

Each country-indicator pair includes:
- 📈 Trend plots with automatic linear regression lines
- 📄 One-click PDF export for each chart
- 📊 Tabular data view

---

## Features

- Multi-country + multi-indicator support
- Auto-detected yearly trends
- Seaborn-enhanced visuals
- Linear regression trendline via `statsmodels`
- Exportable charts as PDF files

---

##  Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run multi_country_dashboard.py

📄 [Full Report in Markdown](Transport_Report_Markdown.md)

