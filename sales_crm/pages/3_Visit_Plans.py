# pages/3_Visit_Plans.py
import streamlit as st
import sqlite3
from datetime import date

st.title("📅 Weekly Visit Plan")

with st.form("visit_form"):
    visit_date = st.date_input("Select Date (Fri/Sat preferred)", value=date.today())
    purpose = st.text_area("Purpose of Visit")
    location = st.text_input("Location")

    submitted = st.form_submit_button("Save Visit")
    if submitted:
        conn = sqlite3.connect("data/crm.db")
        c = conn.cursor()
        c.execute("""
            INSERT INTO visits (user, visit_date, purpose, location)
            VALUES (?, ?, ?, ?)
        """, (st.session_state.username, str(visit_date), purpose, location))
        conn.commit()
        st.success("Visit added!")
