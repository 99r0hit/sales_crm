import streamlit as st
import sqlite3
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# 🔒 Only allow boss role
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must log in to access this page.")
    st.stop()

if st.session_state.role != "boss":
    st.error("⛔ You are not authorized to view this page.")
    st.stop()

st.title("📋 Boss Dashboard")

# Connect to DB
conn = sqlite3.connect("data/crm.db")

# --- Opportunities View ---
st.subheader("📦 All Opportunities")

op_df = pd.read_sql_query("""
    SELECT company, product, industry, interest, qty, price, sop_stage, created_by 
    FROM opportunities
    ORDER BY sop_stage ASC
""", conn)

if not op_df.empty:
    gb_op = GridOptionsBuilder.from_dataframe(op_df)
    gb_op.configure_pagination()
    gb_op.configure_default_column(resizable=True, wrapText=True, autoHeight=True)
    AgGrid(op_df, gridOptions=gb_op.build(), height=300, fit_columns_on_grid_load=True)
else:
    st.info("No opportunities found.")

st.markdown("---")

# --- Visit Plans View ---
st.subheader("📅 All Visit Plans")

visit_df = pd.read_sql_query("""
    SELECT visit_date AS "Date", user AS "User", location AS "Location", purpose AS "Purpose"
    FROM visits
    ORDER BY visit_date DESC
""", conn)

conn.close()

if not visit_df.empty:
    gb_visit = GridOptionsBuilder.from_dataframe(visit_df)
    gb_visit.configure_pagination()
    gb_visit.configure_default_column(resizable=True, wrapText=True, autoHeight=True)
    AgGrid(visit_df, gridOptions=gb_visit.build(), height=300, fit_columns_on_grid_load=True)
else:
    st.info("No visit plans found.")
