import os
import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


def get_database_url():
    db_host = os.getenv("DB_HOST", "postgres_db")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "student_opportunities_db")
    db_user = os.getenv("DB_USER", "app_user")
    db_password = os.getenv("DB_PASSWORD", "app_password")

    return f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


@st.cache_resource
def get_engine():
    return create_engine(get_database_url())


def test_connection():
    try:
        engine = get_engine()
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            return True, result.scalar()
    except SQLAlchemyError as error:
        return False, str(error)
