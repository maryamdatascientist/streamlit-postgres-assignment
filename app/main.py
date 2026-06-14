import streamlit as st
from auth import login_widget
from db import test_connection
from queries import get_total_records

st.set_page_config(
    page_title="Internship & Job Tracking Dashboard",
    page_icon="💼",
    layout="wide"
)

login_widget()

st.title("Internship & Job Tracking Dashboard")

st.markdown("""
This application helps faculty members manage internship and job opportunities using:

- Streamlit
- PostgreSQL
- pgAdmin
- Docker Compose
- GitHub
""")

st.header("Login Credentials")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Admin")
    st.code("Username: admin\nPassword: admin123")

with col2:
    st.subheader("Viewer")
    st.code("Username: viewer\nPassword: viewer123")

st.header("Database Status")

is_connected, message = test_connection()

if is_connected:
    st.success("Database connected successfully.")
    total_records = get_total_records()
    st.metric("Total Opportunities", total_records)
    st.info("PostgreSQL version detected successfully.")
    st.code(message)
else:
    st.error("Database connection failed.")
    st.code(message)

st.header("Application Guide")

st.write("""
Use the sidebar pages to add, view, update, delete, upload, export, analyze, and verify job opportunities.
""")
