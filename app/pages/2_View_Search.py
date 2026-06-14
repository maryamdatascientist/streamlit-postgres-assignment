from auth import require_login
import streamlit as st
from queries import fetch_all_opportunities

st.set_page_config(
    page_title="View and Search Opportunities",
    page_icon="🔍",
    layout="wide"
)

require_login()


st.title("View and Search Opportunities")

try:
    df = fetch_all_opportunities()

    if df.empty:
        st.warning("No opportunities found in the database.")
    else:
        st.success(f"{len(df)} opportunities loaded from PostgreSQL.")

        st.sidebar.header("Filters")

        search_text = st.sidebar.text_input("Search company, title, skills, or city")

        categories = sorted(df["category"].dropna().unique().tolist())
        selected_categories = st.sidebar.multiselect("Category", categories)

        cities = sorted(df["city"].dropna().unique().tolist())
        selected_cities = st.sidebar.multiselect("City", cities)

        work_modes = sorted(df["work_mode"].dropna().unique().tolist())
        selected_work_modes = st.sidebar.multiselect("Work Mode", work_modes)

        statuses = sorted(df["status"].dropna().unique().tolist())
        selected_statuses = st.sidebar.multiselect("Status", statuses)

        experience_levels = sorted(df["experience_level"].dropna().unique().tolist())
        selected_experience = st.sidebar.multiselect("Experience Level", experience_levels)

        min_salary = int(df["salary_min"].fillna(0).min())
        max_salary = int(df["salary_max"].fillna(0).max())

        salary_range = st.sidebar.slider(
            "Salary Range",
            min_value=min_salary,
            max_value=max_salary,
            value=(min_salary, max_salary)
        )

        filtered_df = df.copy()

        if search_text:
            search_text = search_text.lower()
            filtered_df = filtered_df[
                filtered_df["company_name"].str.lower().str.contains(search_text, na=False)
                | filtered_df["job_title"].str.lower().str.contains(search_text, na=False)
                | filtered_df["required_skills"].str.lower().str.contains(search_text, na=False)
                | filtered_df["city"].str.lower().str.contains(search_text, na=False)
            ]

        if selected_categories:
            filtered_df = filtered_df[filtered_df["category"].isin(selected_categories)]

        if selected_cities:
            filtered_df = filtered_df[filtered_df["city"].isin(selected_cities)]

        if selected_work_modes:
            filtered_df = filtered_df[filtered_df["work_mode"].isin(selected_work_modes)]

        if selected_statuses:
            filtered_df = filtered_df[filtered_df["status"].isin(selected_statuses)]

        if selected_experience:
            filtered_df = filtered_df[filtered_df["experience_level"].isin(selected_experience)]

        filtered_df = filtered_df[
            (filtered_df["salary_min"].fillna(0) >= salary_range[0])
            & (filtered_df["salary_max"].fillna(0) <= salary_range[1])
        ]

        st.subheader("Filtered Results")
        st.write(f"Showing {len(filtered_df)} of {len(df)} records.")

        st.dataframe(filtered_df, use_container_width=True)

except Exception as error:
    st.error("Failed to load opportunities.")
    st.code(str(error))
