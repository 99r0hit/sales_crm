import streamlit as st
import sqlite3
from datetime import date
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

# 🔒 Page protection
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must log in to access this page.")
    st.stop()

st.title("📅 Visit Plan Management")

# --- Visit Entry Form ---
with st.form("visit_form"):
    visit_date = st.date_input("🗓️ Select Visit Date", value=date.today())
    location = st.text_input("📍 Location")
    purpose = st.text_area("📝 Purpose of Visit", height=80)

    submitted = st.form_submit_button("➕ Add Visit")
    if submitted:
        conn = sqlite3.connect("data/crm.db")
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO visits (user, visit_date, purpose, location)
            VALUES (?, ?, ?, ?)
        """, (st.session_state.username, str(visit_date), purpose, location))
        conn.commit()
        conn.close()
        st.success("✅ Visit plan added!")

# --- Fetch All User Visits ---
conn = sqlite3.connect("data/crm.db")
df = pd.read_sql_query(f"""
    SELECT visit_date AS "Date", location AS "Location", purpose AS "Purpose"
    FROM visits 
    WHERE user='{st.session_state.username}'
    ORDER BY visit_date DESC
""", conn)
conn.close()

# --- Display with AgGrid Calendar Style ---
if not df.empty:
    st.subheader("📋 Your Visit Plans")
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(enabled=True)
    gb.configure_default_column(resizable=True, wrapText=True, autoHeight=True)
    grid_options = gb.build()
    AgGrid(df, gridOptions=grid_options, height=300, fit_columns_on_grid_load=True)
else:
    st.info("No visit plans yet. Use the form above to add one.")
