import streamlit as st
import pandas as pd

# Load Data
st.title("🔍 Lead Conversion Scoring Dashboard")
df = pd.read_csv("dashboard/scored_leads.csv")

# Show raw data
with st.expander("📂 View Raw Data"):
    st.dataframe(df)

# Summary stats
st.subheader("📈 Overall Stats")
col1, col2 = st.columns(2)
col1.metric("Total Leads", len(df))
col2.metric("Average Conversion Score", f"{df['conversion_score'].mean():.2f}")

# Score Distribution
st.subheader("📊 Lead Conversion Score Distribution")

# Categorize the scores into bins
bins = [0, 0.4, 0.7, 1.0]
labels = ['Low', 'Medium', 'High']
df['score_range'] = pd.cut(df['conversion_score'], bins=bins, labels=labels)

# Count how many leads fall into each range
score_counts = df['score_range'].value_counts().sort_index()

# Display bar chart
st.bar_chart(score_counts)
