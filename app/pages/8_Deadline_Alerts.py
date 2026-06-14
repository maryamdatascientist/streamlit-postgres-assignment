from auth import require_login
import streamlit as st
import pandas as pd
from queries import fetch_all_opportunities

st.set_page_config(
    page_title="Deadline Alerts",
    page_icon="⏰",
    layout="wide"
)

require_login()


st.title("Deadline Alerts")

st.info("This page shows opportunities closing within 7 days and opportunities that are already expired.")

try:
    df = fetch_all_opportunities()

    if df.empty:
        st.warning("No opportunities found.")
        st.stop()

    df["application_deadline"] = pd.to_datetime(df["application_deadline"], errors="coerce")
    today = pd.Timestamp.today().normalize()
    next_7_days = today + pd.Timedelta(days=7)

    closing_soon_df = df[
        (df["application_deadline"] >= today)
        & (df["application_deadline"] <= next_7_days)
    ].sort_values(by="application_deadline")

    expired_by_date_df = df[
        df["application_deadline"] < today
    ].sort_values(by="application_deadline")

    status_expired_df = df[
        df["status"] == "Expired"
    ].sort_values(by="application_deadline")

    col1, col2, col3 = st.columns(3)
    col1.metric("Closing Within 7 Days", len(closing_soon_df))
    col2.metric("Expired by Deadline", len(expired_by_date_df))
    col3.metric("Status Marked Expired", len(status_expired_df))

    st.divider()

    st.subheader("Opportunities Closing Within 7 Days")

    if closing_soon_df.empty:
        st.success("No opportunities are closing within the next 7 days.")
    else:
        st.warning(f"{len(closing_soon_df)} opportunities are closing soon.")
        st.dataframe(
            closing_soon_df[
                [
                    "opportunity_id",
                    "company_name",
                    "job_title",
                    "category",
                    "city",
                    "work_mode",
                    "application_deadline",
                    "status",
                    "source_link"
                ]
            ],
            use_container_width=True
        )

    st.divider()

    st.subheader("Expired Opportunities Based on Deadline")

    if expired_by_date_df.empty:
        st.success("No opportunities are expired based on deadline.")
    else:
        st.error(f"{len(expired_by_date_df)} opportunities have passed their deadline.")
        st.dataframe(
            expired_by_date_df[
                [
                    "opportunity_id",
                    "company_name",
                    "job_title",
                    "category",
                    "city",
                    "application_deadline",
                    "status",
                    "source_link"
                ]
            ],
            use_container_width=True
        )

    st.divider()

    st.subheader("Opportunities Marked as Expired Status")

    if status_expired_df.empty:
        st.success("No opportunities are marked as Expired.")
    else:
        st.error(f"{len(status_expired_df)} opportunities are marked as Expired.")
        st.dataframe(
            status_expired_df[
                [
                    "opportunity_id",
                    "company_name",
                    "job_title",
                    "category",
                    "city",
                    "application_deadline",
                    "status",
                    "source_link"
                ]
            ],
            use_container_width=True
        )

except Exception as error:
    st.error("Failed to load deadline alerts.")
    st.code(str(error))
