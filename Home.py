import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("Dashboard Excel_SNA.csv")

# Streamlit App Title
st.title("📊 State-wise Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_states = st.sidebar.multiselect("Select State(s)", df["Name of State"].unique(), default=df["Name of State"].unique())

# Filter Data
filtered_df = df[df["Name of State"].isin(selected_states)]

# Create Visualizations
st.subheader("Total SLSs by State")
fig_bar = px.bar(filtered_df, x='Name of State', y='Total SLSs', title='Total SLSs by State', color='Total SLSs')
st.plotly_chart(fig_bar)

st.subheader("Accounts Opened Distribution")
fig_pie = px.pie(filtered_df, names='Name of State', values='Accounts opened', title='Accounts Opened Distribution')
st.plotly_chart(fig_pie)

st.subheader("SLSs vs Accounts Opened")
fig_line = px.line(filtered_df, x='Name of State', y=['Total SLSs', 'Accounts opened'], title='SLSs vs Accounts Opened')
st.plotly_chart(fig_line)

# Show Data Table
st.subheader("📋 Data Table")
st.dataframe(filtered_df)

# Run the app with: streamlit run app.py
