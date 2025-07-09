import streamlit as st
from backend.auth import check_login, get_user_role

st.set_page_config(page_title="Sales CRM", layout="wide")

# Session states
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'role' not in st.session_state:
    st.session_state.role = ""

# Login section
if not st.session_state.logged_in:
    st.title("🔐 Login to Sales CRM")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if check_login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = get_user_role(username)
            st.success(f"Welcome, {username}!")
            st.rerun()
        else:
            st.error("Invalid credentials. Please try again.")
else:
    # Already logged in
    st.sidebar.title(f"🧭 Navigation - {st.session_state.role.capitalize()}")
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    st.sidebar.page_link("pages/1_Dashboard.py", label="📊 Dashboard")
    st.sidebar.page_link("pages/2_Create_Oppon.py", label="➕ Add Opportunity")
    st.sidebar.page_link("pages/3_Visit_Plans.py", label="📅 Visit Plans")

    if st.session_state.role == "admin":
        st.sidebar.page_link("pages/4_Admin_Login.py", label="🛠 Admin Panel")
    if st.session_state.role == "boss":
        st.sidebar.page_link("pages/5_Boss_Dashboard.py", label="📋 Boss Dashboard")

    # Logout button
    if st.sidebar.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.rerun()
