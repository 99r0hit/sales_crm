import streamlit as st
import sqlite3

st.title("➕ Create New Opportunity")

# Connect to DB
conn = sqlite3.connect("data/crm.db")
cur = conn.cursor()

# -- Fetch existing companies
cur.execute("SELECT name FROM companies")
existing_companies = [row[0] for row in cur.fetchall()]

st.markdown("### 🏢 Company")

company_mode = st.radio("Choose Option:", ["Select existing", "Add new"])

# Placeholder to store company name (used below in opportunity)
final_company_name = ""

if company_mode == "Select existing":
    selected_company = st.selectbox("Select Company", existing_companies)
    final_company_name = selected_company

else:
    st.markdown("#### ✏️ New Company Profile")
    company_name = st.text_input("Company Name")
    turnover = st.text_input("Turnover (e.g. ₹10 Cr or $5M)")
    industry = st.text_input("Industry")
    generic_info = st.text_area("Generic Information")
    hq_location = st.text_input("Headquarters")
    purchase_office = st.text_input("Purchase Office Location")
    r_and_d_location = st.text_input("R&D Location(s)")
    design_location = st.text_input("Design Office(s)")
    manufacturing_location = st.text_input("Manufacturing Location(s)")
    website = st.text_input("Website")
    country = st.text_input("Country of Origin")

    if company_name:
        final_company_name = company_name

# Divider
st.markdown("---")
st.markdown("### 🎯 Opportunity Details")

product = st.text_input("Product")
interest = st.text_input("Interest / Category")
description = st.text_area("Details / Description")
qty = st.number_input("Quantity", min_value=0, step=1)
price = st.number_input("Expected Price", min_value=0.0, step=100.0)

sop_stage = st.selectbox("Stage of Progress (SOP)", [
    "0 - Email Campaign",
    "1 - Cold Call",
    "2 - Demo",
    "3 - Negotiation",
    "4 - Sample Sent",
    "5 - Technical Approval",
    "6 - Price Discussion",
    "7 - Final Discussion",
    "8 - Project Close"
])
sop_value = int(sop_stage.split(" - ")[0])

# Submit Button
if st.button("📥 Submit Opportunity"):
    if not final_company_name:
        st.error("❗ Company name is required.")
    else:
        # -- If "Add new", insert into companies table first
        if company_mode == "Add new":
            try:
                cur.execute("""
                    INSERT INTO companies (
                        name, turnover, industry, generic_info, hq_location,
                        purchase_office, r_and_d_location, design_location,
                        manufacturing_location, website, country
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    company_name, turnover, industry, generic_info, hq_location,
                    purchase_office, r_and_d_location, design_location,
                    manufacturing_location, website, country
                ))
                conn.commit()
                st.success(f"✅ New company '{company_name}' added.")
            except sqlite3.IntegrityError:
                st.warning("⚠️ Company already exists.")

        # -- Insert Opportunity
        created_by = st.session_state.get("username", "unknown")
        cur.execute("""
            INSERT INTO opportunities (
                company, product, industry, interest, description,
                qty, price, sop_stage, created_by
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            final_company_name, product, industry, interest, description,
            qty, price, sop_value, created_by
        ))
        conn.commit()
        st.success("🎯 Opportunity submitted successfully.")

conn.close()
