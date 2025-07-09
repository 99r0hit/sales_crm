import streamlit as st
import sqlite3
import pandas as pd

# 🔒 Protect the page
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must log in to access this page.")
    st.stop()

st.title("📊 Your Opportunities Dashboard")

conn = sqlite3.connect("data/crm.db")

# Show data based on role
if st.session_state.role == "boss":
    df = pd.read_sql_query("SELECT * FROM opportunities", conn)
else:
    df = pd.read_sql_query(f"""
        SELECT * FROM opportunities 
        WHERE created_by='{st.session_state.username}'
    """, conn)

conn.close()

# Optional Filters
with st.expander("🔍 Filters", expanded=False):
    sop_filter = st.multiselect("Filter by SOP Stage", options=range(9))
    if sop_filter:
        df = df[df["sop_stage"].isin(sop_filter)]

# Display Data
if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No opportunities found.")

