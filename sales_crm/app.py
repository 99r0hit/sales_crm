import streamlit as st
from backend.auth import check_login, get_user_role

st.set_page_config(page_title="Sales CRM", layout="wide")
st.title("🔗 Sales CRM Platform")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")
else:
    st.success(f"Welcome, {st.session_state.username}!")
    st.sidebar.success("Use the sidebar to navigate pages.")
