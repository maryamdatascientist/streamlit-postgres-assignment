from auth import require_login
import streamlit as st
import pandas as pd
from sqlalchemy import text
from db import get_engine, test_connection

st.set_page_config(
    page_title="Database Health Check",
    page_icon="🩺",
    layout="wide"
)

require_login()


st.title("Database Health Check")

st.info("This page verifies PostgreSQL connection, table status, row count, latest record, and schema columns.")

try:
    is_connected, message = test_connection()

    if is_connected:
        st.success("Database connection successful.")
        st.subheader("PostgreSQL Version")
        st.code(message)
    else:
        st.error("Database connection failed.")
        st.code(message)
        st.stop()

    engine = get_engine()

    with engine.connect() as connection:
        database_name = connection.execute(text("SELECT current_database();")).scalar()
        current_user = connection.execute(text("SELECT current_user;")).scalar()
        total_rows = connection.execute(text("SELECT COUNT(*) FROM opportunities;")).scalar()
        table_exists = connection.execute(text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name = 'opportunities'
            );
        """)).scalar()

    st.subheader("Database Summary")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Database", database_name)
    col2.metric("User", current_user)
    col3.metric("Table Exists", "Yes" if table_exists else "No")
    col4.metric("Total Rows", total_rows)

    st.divider()

    st.subheader("Latest Record")

    latest_record_query = """
        SELECT *
        FROM opportunities
        ORDER BY opportunity_id DESC
        LIMIT 1;
    """

    latest_record_df = pd.read_sql(latest_record_query, engine)

    if latest_record_df.empty:
        st.warning("No latest record found.")
    else:
        st.dataframe(latest_record_df, use_container_width=True)

    st.divider()

    st.subheader("Table Columns")

    columns_query = """
        SELECT
            column_name,
            data_type,
            is_nullable,
            column_default
        FROM information_schema.columns
        WHERE table_schema = 'public'
        AND table_name = 'opportunities'
        ORDER BY ordinal_position;
    """

    columns_df = pd.read_sql(columns_query, engine)
    st.dataframe(columns_df, use_container_width=True)

    st.divider()

    st.subheader("Manual Verification Queries")

    st.code("""
SELECT * FROM opportunities;

SELECT COUNT(*) FROM opportunities;

SELECT category, COUNT(*)
FROM opportunities
GROUP BY category;

SELECT work_mode, COUNT(*)
FROM opportunities
GROUP BY work_mode;

SELECT *
FROM opportunities
WHERE status = 'Open';

SELECT *
FROM opportunities
WHERE application_deadline <= CURRENT_DATE + INTERVAL '7 days';
""", language="sql")

except Exception as error:
    st.error("Database health check failed.")
    st.code(str(error))
