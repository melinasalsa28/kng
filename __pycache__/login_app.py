import streamlit as st
import json

st.set_page_config(page_title="Login", page_icon="🔐")

def show_login(USERNAME, PASSWORD):

# Load users
    def load_users():
        with open("users.json", "r") as f:
            return json.load(f)

    users = load_users()

    st.title("Halaman Login")

    if "login_status" not in st.session_state:
        st.session_state.login_status = False

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state.login_status = True
            st.session_state.username = username
            st.session_state.role = users[username]["role"]
            st.success("Login berhasil! Silakan lanjut ke sidebar.")
        else:
            st.error("Username atau password salah")

# Tampilkan info login
    if st.session_state.login_status:
        st.sidebar.success(f"Login sebagai {st.session_state.username} ({st.session_state.role})")
        if st.session_state.role == "umum":
            st.sidebar.page_link("pages/umum.py", label="Dashboard Umum")
        elif st.session_state.role == "khusus":
            st.sidebar.page_link("pages/khusus.py", label="Dashboard Khusus")