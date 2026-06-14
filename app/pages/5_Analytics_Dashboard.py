from auth import require_login
import streamlit as st
import pandas as pd
import plotly.express as px
from queries import fetch_all_opportunities

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

require_login()


st.title("Analytics Dashboard")

try:
    df = fetch_all_opportunities()

    if df.empty:
        st.warning("No data available for analytics.")
        st.stop()

    df["application_deadline"] = pd.to_datetime(df["application_deadline"], errors="coerce")
    df["average_salary"] = df[["salary_min", "salary_max"]].mean(axis=1)
    today = pd.Timestamp.today().normalize()

    total_jobs = len(df)
    open_jobs = len(df[df["status"] == "Open"])
    closed_jobs = len(df[df["status"] == "Closed"])
    expired_jobs = len(df[df["status"] == "Expired"])
    remote_jobs = len(df[df["work_mode"] == "Remote"])
    companies_count = df["company_name"].nunique()
    average_salary = df["average_salary"].mean()
    shortlisted_jobs = len(df[df["status"] == "Shortlisted"])

    st.subheader("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Opportunities", total_jobs)
    col2.metric("Open Jobs", open_jobs)
    col3.metric("Closed Jobs", closed_jobs)
    col4.metric("Expired Jobs", expired_jobs)

    col5, col6, col7, col8 = st.columns(4)
    col5.metric("Remote Jobs", remote_jobs)
    col6.metric("Companies", companies_count)
    col7.metric("Average Salary", f"{average_salary:,.0f} PKR")
    col8.metric("Shortlisted Jobs", shortlisted_jobs)

    st.divider()

    st.subheader("Charts and Trends")

    tab1, tab2, tab3 = st.tabs(["Job Distribution", "Salary Analysis", "Deadline and Skills"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            category_counts = df["category"].value_counts().reset_index()
            category_counts.columns = ["category", "count"]
            fig_category = px.bar(
                category_counts,
                x="category",
                y="count",
                title="Opportunities by Category",
                text="count"
            )
            st.plotly_chart(fig_category, use_container_width=True)

        with col2:
            status_counts = df["status"].value_counts().reset_index()
            status_counts.columns = ["status", "count"]
            fig_status = px.pie(
                status_counts,
                names="status",
                values="count",
                title="Opportunities by Status"
            )
            st.plotly_chart(fig_status, use_container_width=True)

        col3, col4 = st.columns(2)

        with col3:
            work_mode_counts = df["work_mode"].value_counts().reset_index()
            work_mode_counts.columns = ["work_mode", "count"]
            fig_work_mode = px.pie(
                work_mode_counts,
                names="work_mode",
                values="count",
                title="Work Mode Distribution"
            )
            st.plotly_chart(fig_work_mode, use_container_width=True)

        with col4:
            city_counts = df["city"].value_counts().reset_index()
            city_counts.columns = ["city", "count"]
            fig_city = px.bar(
                city_counts,
                x="city",
                y="count",
                title="Opportunities by City",
                text="count"
            )
            st.plotly_chart(fig_city, use_container_width=True)

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            salary_by_category = df.groupby("category", as_index=False)["average_salary"].mean()
            fig_salary_category = px.bar(
                salary_by_category,
                x="category",
                y="average_salary",
                title="Average Salary by Category",
                text_auto=".0f"
            )
            st.plotly_chart(fig_salary_category, use_container_width=True)

        with col2:
            fig_salary_box = px.box(
                df,
                x="experience_level",
                y="average_salary",
                title="Salary Distribution by Experience Level"
            )
            st.plotly_chart(fig_salary_box, use_container_width=True)

        salary_table = df[
            [
                "company_name",
                "job_title",
                "category",
                "city",
                "salary_min",
                "salary_max",
                "currency",
                "experience_level"
            ]
        ].sort_values(by="salary_max", ascending=False)

        st.subheader("Highest Salary Opportunities")
        st.dataframe(salary_table.head(10), use_container_width=True)

    with tab3:
        valid_deadlines = df.dropna(subset=["application_deadline"]).copy()
        valid_deadlines["deadline_month"] = valid_deadlines["application_deadline"].dt.to_period("M").astype(str)

        col1, col2 = st.columns(2)

        with col1:
            deadline_counts = valid_deadlines["deadline_month"].value_counts().sort_index().reset_index()
            deadline_counts.columns = ["deadline_month", "count"]
            fig_deadline = px.line(
                deadline_counts,
                x="deadline_month",
                y="count",
                markers=True,
                title="Application Deadlines by Month"
            )
            st.plotly_chart(fig_deadline, use_container_width=True)

        with col2:
            experience_counts = df["experience_level"].value_counts().reset_index()
            experience_counts.columns = ["experience_level", "count"]
            fig_experience = px.bar(
                experience_counts,
                x="experience_level",
                y="count",
                title="Opportunities by Experience Level",
                text="count"
            )
            st.plotly_chart(fig_experience, use_container_width=True)

        skills_series = (
            df["required_skills"]
            .dropna()
            .str.split(",")
            .explode()
            .str.strip()
        )

        top_skills = skills_series.value_counts().head(10).reset_index()
        top_skills.columns = ["skill", "count"]

        fig_skills = px.bar(
            top_skills,
            x="skill",
            y="count",
            title="Top 10 Required Skills",
            text="count"
        )
        st.plotly_chart(fig_skills, use_container_width=True)

        closing_soon = df[
            (df["application_deadline"] >= today)
            & (df["application_deadline"] <= today + pd.Timedelta(days=7))
        ]

        st.subheader("Opportunities Closing Within 7 Days")
        st.dataframe(
            closing_soon[
                [
                    "opportunity_id",
                    "company_name",
                    "job_title",
                    "city",
                    "application_deadline",
                    "status"
                ]
            ],
            use_container_width=True
        )

except Exception as error:
    st.error("Failed to load analytics dashboard.")
    st.code(str(error))
