import pandas as pd
import streamlit as st

st.set_page_config(page_title="Lead Scoring Dashboard", layout="wide")
st.title("Lead Conversion Scoring - Open Pipeline")
st.caption("Win probability for open (Engaging / Prospecting) deals, "
           "from a model trained on closed Won/Lost deals.")

df = pd.read_csv("dashboard/scored_leads.csv")

# Filters
c1, c2, c3 = st.columns(3)
region = c1.multiselect("Regional office", sorted(df["regional_office"].dropna().unique()))
manager = c2.multiselect("Manager", sorted(df["manager"].dropna().unique()))
priority = c3.multiselect("Priority", ["High", "Medium", "Low"])
if region:
    df = df[df["regional_office"].isin(region)]
if manager:
    df = df[df["manager"].isin(manager)]
if priority:
    df = df[df["priority"].isin(priority)]

m1, m2, m3 = st.columns(3)
m1.metric("Open deals", len(df))
m2.metric("Avg win probability", f"{df['conversion_probability'].mean():.1%}" if len(df) else "-")
m3.metric("High-priority deals", int((df["priority"] == "High").sum()))

st.subheader("Deals by priority")
st.bar_chart(df["priority"].value_counts().reindex(["High", "Medium", "Low"]).fillna(0))

st.subheader("Average win probability by sales agent")
st.bar_chart(df.groupby("sales_agent")["conversion_probability"].mean().sort_values(ascending=False))

st.subheader("Top deals to work first")
st.dataframe(df.head(50), use_container_width=True)
