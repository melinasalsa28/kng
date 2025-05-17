import streamlit as st
import os
from streamlit.runtime.scriptrunner import RerunData

# Cek apakah file users.json ada
def load_users():
    import json
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    else:
        return {}

def show_login():
    users = load_users()

# Inisialisasi sesi
    if "login_status" not in st.session_state:
        st.session_state.login_status = False
        st.session_state.username = ""
        st.session_state.role = ""

    st.title("Selamat Datang di Aplikasi")

# --- Form Login ---
    st.subheader("Login")

    login_mode = st.radio("Masuk sebagai:", ["Pengguna Umum", "Admin"])

    if login_mode == "Pengguna Umum":
        email = st.text_input("Email Anda")
        if st.button("Login Pengguna Umum"):
            if "@" in email and "." in email:
                st.session_state.login_status = True
                st.session_state.username = email
                st.session_state.role = "umum"
                st.success(f"Berhasil login sebagai {email}")
            else:
                st.error("Masukkan email yang valid.")

    elif login_mode == "Admin":
        email = st.text_input("Email Admin")
        password = st.text_input("Password", type="password")

        if st.button("Login Admin"):
            if email in users and users[email]["password"] == password:
                st.session_state.login_status = True
                st.session_state.username = email
                st.session_state.role = users[email]["role"]
                st.success(f"Login berhasil sebagai Admin: {email}")
            else:
                st.error("Email atau password salah.")

    # --- Navigasi setelah login ---
    if st.session_state.login_status:
        st.sidebar.success(f"Login sebagai: {st.session_state.username} ({st.session_state.role})")
        
        if st.sidebar.button("Logout"):
            st.session_state.login_status = False
            st.session_state.username = ""
            st.session_state.role = ""
            st.rerun()

        # Arahkan ke halaman yang sesuai
        if st.session_state.role == "umum":
            st.sidebar.page_link("pages/umum.py", label="🏠 Dashboard Umum")
        elif st.session_state.role == "khusus":
            st.sidebar.page_link("pages/khusus.py", label="🛠 Dashboard Khusus")