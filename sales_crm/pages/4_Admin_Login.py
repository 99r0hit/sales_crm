import streamlit as st
import sqlite3
import bcrypt
import pandas as pd

# 🔒 Only allow admin
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must log in to access this page.")
    st.stop()

if st.session_state.role != "admin":
    st.error("⛔ You are not authorized to view this page.")
    st.stop()

st.title("🛠 Admin Panel - User Management")

# Connect to DB
conn = sqlite3.connect("data/crm.db")
cur = conn.cursor()

# --- View Existing Users ---
st.subheader("👥 Existing Users")

user_df = pd.read_sql_query("SELECT id, username, role FROM users", conn)
st.dataframe(user_df)

st.markdown("---")

# --- Add New User Form ---
st.subheader("➕ Add New User")

with st.form("add_user_form"):
    new_username = st.text_input("👤 Username")
    new_password = st.text_input("🔑 Password", type="password")
    role = st.selectbox("🎚️ Role", options=["user", "admin", "boss"])
    submit_user = st.form_submit_button("Add User")

    if submit_user:
        if new_username and new_password:
            hashed_pw = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
            try:
                cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                            (new_username, hashed_pw, role))
                conn.commit()
                st.success(f"✅ User '{new_username}' added.")
                st.rerun()
            except sqlite3.IntegrityError:
                st.error("❌ Username already exists.")
        else:
            st.warning("All fields are required.")

conn.close()
