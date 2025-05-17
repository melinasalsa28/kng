import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from login_app import show_login 
from home_app import show_home 

st.set_page_config(page_title="Sistem Akuntansi Kelinci", page_icon="🐇", layout="wide")

# Inisialisasi session state
def init_session_state():
    defaults = {
        "login_status": False,
        "username": "",
        "role": ""
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()


def main():
    if st.session_state.login_status:
        show_home()  # Logika halaman utama
        # Sidebar link setelah login
        st.sidebar.success(f"Login sebagai {st.session_state.username} ({st.session_state.role})")
        if st.session_state.role == "umum":
            st.sidebar.page_link("pages/umum.py", label="Dashboard Umum")
        elif st.session_state.role == "khusus":
            st.sidebar.page_link("pages/khusus.py", label="Dashboard Khusus")
    else:
        show_login()  

if __name__ == "__main__":
    main()