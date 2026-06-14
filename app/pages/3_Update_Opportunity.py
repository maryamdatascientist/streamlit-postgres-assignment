from auth import require_admin
import streamlit as st
from queries import fetch_all_opportunities, get_opportunity_by_id, update_opportunity

st.set_page_config(
    page_title="Update Opportunity",
    page_icon="✏️",
    layout="wide"
)

require_admin()


st.title("Update Opportunity")

try:
    df = fetch_all_opportunities()

    if df.empty:
        st.warning("No opportunities available to update.")
    else:
        opportunity_options = {
            f"{row.opportunity_id} - {row.company_name} - {row.job_title}": row.opportunity_id
            for row in df.itertuples()
        }

        selected_label = st.selectbox(
            "Select Opportunity",
            list(opportunity_options.keys())
        )

        selected_id = opportunity_options[selected_label]
        selected_df = get_opportunity_by_id(selected_id)

        if selected_df.empty:
            st.error("Selected opportunity not found.")
        else:
            record = selected_df.iloc[0]

            st.subheader("Current Record")
            st.dataframe(selected_df, use_container_width=True)

            with st.form("update_opportunity_form"):
                col1, col2 = st.columns(2)

                with col1:
                    company_name = st.text_input("Company Name *", value=record["company_name"])
                    job_title = st.text_input("Job Title *", value=record["job_title"])

                    categories = ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"]
                    category = st.selectbox(
                        "Category *",
                        categories,
                        index=categories.index(record["category"]) if record["category"] in categories else 0
                    )

                    city = st.text_input("City", value=record["city"] or "")
                    country = st.text_input("Country", value=record["country"] or "Pakistan")

                    work_modes = ["Remote", "Onsite", "Hybrid"]
                    work_mode = st.selectbox(
                        "Work Mode *",
                        work_modes,
                        index=work_modes.index(record["work_mode"]) if record["work_mode"] in work_modes else 0
                    )

                    experience_levels = ["Internship", "Entry Level", "Mid Level", "Senior Level"]
                    experience_level = st.selectbox(
                        "Experience Level",
                        experience_levels,
                        index=experience_levels.index(record["experience_level"]) if record["experience_level"] in experience_levels else 0
                    )

                with col2:
                    salary_min = st.number_input(
                        "Minimum Salary",
                        min_value=0.0,
                        step=5000.0,
                        value=float(record["salary_min"] or 0)
                    )

                    salary_max = st.number_input(
                        "Maximum Salary",
                        min_value=0.0,
                        step=5000.0,
                        value=float(record["salary_max"] or 0)
                    )

                    currencies = ["PKR", "USD", "EUR"]
                    currency = st.selectbox(
                        "Currency",
                        currencies,
                        index=currencies.index(record["currency"]) if record["currency"] in currencies else 0
                    )

                    application_deadline = st.date_input(
                        "Application Deadline",
                        value=record["application_deadline"]
                    )

                    statuses = ["Open", "Closed", "Expired", "Shortlisted"]
                    status = st.selectbox(
                        "Status",
                        statuses,
                        index=statuses.index(record["status"]) if record["status"] in statuses else 0
                    )

                    source_link = st.text_input("Source Link", value=record["source_link"] or "")

                required_skills = st.text_area(
                    "Required Skills *",
                    value=record["required_skills"]
                )

                submitted = st.form_submit_button("Update Opportunity")

            if submitted:
                errors = []

                if not company_name.strip():
                    errors.append("Company name is required.")

                if not job_title.strip():
                    errors.append("Job title is required.")

                if not required_skills.strip():
                    errors.append("Required skills are required.")

                if salary_max < salary_min:
                    errors.append("Maximum salary cannot be less than minimum salary.")

                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    updated_data = {
                        "company_name": company_name.strip(),
                        "job_title": job_title.strip(),
                        "category": category,
                        "city": city.strip(),
                        "country": country.strip(),
                        "work_mode": work_mode,
                        "required_skills": required_skills.strip(),
                        "salary_min": salary_min,
                        "salary_max": salary_max,
                        "currency": currency,
                        "experience_level": experience_level,
                        "application_deadline": application_deadline,
                        "status": status,
                        "source_link": source_link.strip()
                    }

                    update_opportunity(selected_id, updated_data)
                    st.success("Opportunity updated successfully.")
                    st.info("Refresh the page or open View/Search to verify changes.")

except Exception as error:
    st.error("Failed to update opportunity.")
    st.code(str(error))
