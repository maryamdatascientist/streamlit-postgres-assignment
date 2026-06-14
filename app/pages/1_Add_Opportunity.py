from auth import require_admin
import streamlit as st
from queries import insert_opportunity, check_duplicate

st.set_page_config(
    page_title="Add New Opportunity",
    page_icon="➕",
    layout="wide"
)

require_admin()


st.title("Add New Opportunity")

st.info("Use this form to add a new internship or job opportunity into PostgreSQL.")

with st.form("add_opportunity_form"):
    col1, col2 = st.columns(2)

    with col1:
        company_name = st.text_input("Company Name *")
        job_title = st.text_input("Job Title *")
        category = st.selectbox(
            "Category *",
            ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"]
        )
        city = st.text_input("City")
        country = st.text_input("Country", value="Pakistan")
        work_mode = st.selectbox("Work Mode *", ["Remote", "Onsite", "Hybrid"])
        experience_level = st.selectbox(
            "Experience Level",
            ["Internship", "Entry Level", "Mid Level", "Senior Level"]
        )

    with col2:
        salary_min = st.number_input("Minimum Salary", min_value=0.0, step=5000.0)
        salary_max = st.number_input("Maximum Salary", min_value=0.0, step=5000.0)
        currency = st.selectbox("Currency", ["PKR", "USD", "EUR"])
        application_deadline = st.date_input("Application Deadline")
        status = st.selectbox("Status", ["Open", "Closed", "Expired", "Shortlisted"])
        source_link = st.text_input("Source Link")

    required_skills = st.text_area("Required Skills *", placeholder="Example: Python, SQL, Machine Learning")

    submitted = st.form_submit_button("Add Opportunity")

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
        is_duplicate = check_duplicate(
            company_name=company_name,
            job_title=job_title,
            city=city,
            source_link=source_link
        )

        if is_duplicate:
            st.warning("Possible duplicate opportunity found. This record was not inserted.")
        else:
            data = {
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

            try:
                insert_opportunity(data)
                st.success("Opportunity added successfully.")
                st.info("Go to View and Search page to verify the new record.")
            except Exception as error:
                st.error("Failed to add opportunity.")
                st.code(str(error))
