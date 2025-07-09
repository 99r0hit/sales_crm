# pages/1_Dashboard.py
import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Your Opportunities")

conn = sqlite3.connect("data/crm.db")
df = pd.read_sql_query(f"SELECT * FROM opportunities WHERE created_by='{st.session_state.username}'", conn)
st.dataframe(df)
