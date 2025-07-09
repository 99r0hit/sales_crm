import streamlit as st
import sqlite3

# 🔒 Protect page
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must log in to access this page.")
    st.stop()

st.title("➕ Create New Opportunity")

# Opportunity Form
with st.form("create_oppon_form"):
    company = st.text_input("🏢 Company Name")
    product = st.text_input("📦 Product")
    industry = st.text_input("🏭 Industry")
    interest = st.text_input("💡 Interest")
    description = st.text_area("📝 Description", height=100)
    qty = st.number_input("🔢 Quantity", min_value=1)
    price = st.number_input("💰 Price per Unit", min_value=0.0)
    sop_stage = st.selectbox("📈 Stage of Progress (SOP)", [
        "0 - Email Campaign",
        "1 - Cold Call",
        "2 - Product Discussion",
        "3 - Negotiation",
        "4 - Sample Approval",
        "5 - Tech Evaluation",
        "6 - Vendor Registration",
        "7 - PO Discussion",
        "8 - Project Close"
    ])
    submitted = st.form_submit_button("✅ Submit Opportunity")

    if submitted:
        sop_value = int(sop_stage.split(" ")[0])  # Get number from "0 - Email Campaign"
        conn = sqlite3.connect("data/crm.db")
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO opportunities 
            (company, product, industry, interest, description, qty, price, sop_stage, created_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (company, product, industry, interest, description, qty, price, sop_value, st.session_state.username))
        conn.commit()
        conn.close()
        st.success("🎉 Opportunity successfully added!")
