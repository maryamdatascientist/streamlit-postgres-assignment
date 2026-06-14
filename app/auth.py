import streamlit as st


USERS = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "viewer": {
        "password": "viewer123",
        "role": "Viewer"
    }
}


def init_auth_state():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if "username" not in st.session_state:
        st.session_state.username = None

    if "role" not in st.session_state:
        st.session_state.role = None


def login_widget():
    init_auth_state()

    st.sidebar.divider()
    st.sidebar.subheader("Login")

    if st.session_state.authenticated:
        st.sidebar.success(f"Logged in as: {st.session_state.username}")
        st.sidebar.info(f"Role: {st.session_state.role}")

        if st.sidebar.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.session_state.role = None
            st.rerun()

        return st.session_state.role

    with st.sidebar.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        user = USERS.get(username)

        if user and user["password"] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.role = user["role"]
            st.sidebar.success("Login successful.")
            st.rerun()
        else:
            st.sidebar.error("Invalid username or password.")

    return None


def require_login():
    role = login_widget()

    if not st.session_state.authenticated:
        st.warning("Please login from the sidebar to access this page.")
        st.stop()

    return role


def require_admin():
    role = require_login()

    if role != "Admin":
        st.error("Admin access required for this page.")
        st.stop()

    return role
