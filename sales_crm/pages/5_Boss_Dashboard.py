# pages/5_Boss_Dashboard.py
import streamlit as st
import pandas as pd
import sqlite3

st.title("📋 Boss Dashboard")

conn = sqlite3.connect("data/crm.db")
df = pd.read_sql_query("SELECT * FROM opportunities", conn)
visit_df = pd.read_sql_query("SELECT * FROM visits", conn)

st.subheader("All Opportunities")
st.dataframe(df)

st.subheader("Visit Plans")
st.dataframe(visit_df)
