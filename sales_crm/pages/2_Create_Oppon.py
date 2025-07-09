# pages/2_Create_Oppon.py
import streamlit as st
import sqlite3

st.title("📝 Create New Opportunity")

with st.form("oppon_form"):
    company = st.text_input("Company Name")
    product = st.text_input("Product")
    industry = st.text_input("Industry")
    interest = st.text_input("Interest")
    description = st.text_area("Details (Description)")
    qty = st.number_input("Quantity", step=1)
    price = st.number_input("Price per Unit")
    sop_stage = st.selectbox("Stage of Progress", [0,1,2,3,4,5,6,7,8])

    submitted = st.form_submit_button("Submit")
    if submitted:
        conn = sqlite3.connect("data/crm.db")
        c = conn.cursor()
        c.execute("""
            INSERT INTO opportunities (company, product, industry, interest, description, qty, price, sop_stage, created_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (company, product, industry, interest, description, qty, price, sop_stage, st.session_state.username))
        conn.commit()
        st.success("Opportunity created!")
