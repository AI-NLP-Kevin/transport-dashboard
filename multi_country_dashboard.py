
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import statsmodels.api as sm

# Load data
df = pd.read_csv("all_transport_data.csv")
df = df.dropna(subset=["Value"])
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

st.set_page_config(layout="wide")
st.title("🌍 Global Transport Trends Report")
st.markdown("This dashboard presents **passenger and freight transport indices** across countries and time. Each chart includes a trendline and downloadable PDF.")

# Function to add trendline using OLS
def add_trendline(ax, x, y):
    try:
        x_num = pd.factorize(x)[0]  # Encode years to integers
        model = sm.OLS(y, sm.add_constant(x_num)).fit()
        y_pred = model.predict(sm.add_constant(x_num))
        ax.plot(x, y_pred, linestyle='--', color='red', label='Trendline')
        ax.legend()
    except:
        pass

# Function to generate PDF download of each figure
def get_pdf_download_link(fig, filename):
    buf = BytesIO()
    fig.savefig(buf, format="pdf", bbox_inches="tight")
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">📄 Download PDF</a>'
    return href

# Group and plot
grouped = df.groupby(["Country", "Indicator"])

for (country, indicator), group in grouped:
    group = group.sort_values("Year")
    st.subheader(f"📊 {country} — {indicator}")

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=group, x="Year", y="Value", marker="o", ax=ax)
    add_trendline(ax, group["Year"], group["Value"])
    ax.set_title(f"{indicator} in {country}", fontsize=14)
    ax.set_xlabel("Year")
    ax.set_ylabel("Value")
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # PDF Download Link
    st.markdown(get_pdf_download_link(fig, f"{country}_{indicator}.pdf"), unsafe_allow_html=True)
    st.dataframe(group.reset_index(drop=True))
    st.markdown("---")

