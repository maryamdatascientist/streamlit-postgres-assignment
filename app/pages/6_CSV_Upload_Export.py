from auth import require_admin
import streamlit as st
import pandas as pd
from queries import fetch_all_opportunities, insert_opportunity, check_duplicate

st.set_page_config(
    page_title="CSV Upload and Export",
    page_icon="📁",
    layout="wide"
)

require_admin()


st.title("CSV Upload / Bulk Insert and Export")

REQUIRED_COLUMNS = [
    "company_name",
    "job_title",
    "category",
    "city",
    "country",
    "work_mode",
    "required_skills",
    "salary_min",
    "salary_max",
    "currency",
    "experience_level",
    "application_deadline",
    "status",
    "source_link"
]

VALID_CATEGORIES = ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"]
VALID_WORK_MODES = ["Remote", "Onsite", "Hybrid"]
VALID_STATUSES = ["Open", "Closed", "Expired", "Shortlisted"]
VALID_CURRENCIES = ["PKR", "USD", "EUR"]


def validate_row(row, row_number):
    errors = []

    if pd.isna(row.get("company_name")) or str(row.get("company_name")).strip() == "":
        errors.append(f"Row {row_number}: company_name is required.")

    if pd.isna(row.get("job_title")) or str(row.get("job_title")).strip() == "":
        errors.append(f"Row {row_number}: job_title is required.")

    if pd.isna(row.get("required_skills")) or str(row.get("required_skills")).strip() == "":
        errors.append(f"Row {row_number}: required_skills is required.")

    if row.get("category") not in VALID_CATEGORIES:
        errors.append(f"Row {row_number}: invalid category.")

    if row.get("work_mode") not in VALID_WORK_MODES:
        errors.append(f"Row {row_number}: invalid work_mode.")

    if row.get("status") not in VALID_STATUSES:
        errors.append(f"Row {row_number}: invalid status.")

    if row.get("currency") not in VALID_CURRENCIES:
        errors.append(f"Row {row_number}: invalid currency.")

    try:
        salary_min = float(row.get("salary_min"))
        salary_max = float(row.get("salary_max"))

        if salary_min < 0 or salary_max < 0:
            errors.append(f"Row {row_number}: salary values cannot be negative.")

        if salary_max < salary_min:
            errors.append(f"Row {row_number}: salary_max cannot be less than salary_min.")
    except Exception:
        errors.append(f"Row {row_number}: salary_min and salary_max must be numeric.")

    try:
        pd.to_datetime(row.get("application_deadline"))
    except Exception:
        errors.append(f"Row {row_number}: invalid application_deadline date.")

    return errors


def convert_df_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")


tab1, tab2 = st.tabs(["CSV Upload / Bulk Insert", "CSV Export"])

with tab1:
    st.subheader("Upload CSV File")

    st.info("CSV file must contain all required columns with valid values.")

    template_df = pd.DataFrame([
        {
            "company_name": "Sample Company",
            "job_title": "Data Intern",
            "category": "Data Science",
            "city": "Lahore",
            "country": "Pakistan",
            "work_mode": "Remote",
            "required_skills": "Python, SQL, Excel",
            "salary_min": 30000,
            "salary_max": 50000,
            "currency": "PKR",
            "experience_level": "Internship",
            "application_deadline": "2026-07-01",
            "status": "Open",
            "source_link": "https://example.com/job"
        }
    ])

    st.download_button(
        label="Download CSV Template",
        data=convert_df_to_csv(template_df),
        file_name="opportunities_template.csv",
        mime="text/csv"
    )

    uploaded_file = st.file_uploader("Upload opportunities CSV", type=["csv"])

    if uploaded_file is not None:
        try:
            upload_df = pd.read_csv(uploaded_file)

            st.subheader("CSV Preview")
            st.dataframe(upload_df.head(20), use_container_width=True)

            missing_columns = [col for col in REQUIRED_COLUMNS if col not in upload_df.columns]

            if missing_columns:
                st.error("CSV file is missing required columns:")
                st.write(missing_columns)
            else:
                validation_errors = []

                for index, row in upload_df.iterrows():
                    validation_errors.extend(validate_row(row, index + 2))

                if validation_errors:
                    st.error("Validation errors found. Fix these before inserting.")
                    for error in validation_errors[:30]:
                        st.warning(error)

                    if len(validation_errors) > 30:
                        st.info(f"{len(validation_errors) - 30} more errors not shown.")
                else:
                    st.success("CSV validation passed.")

                    if st.button("Insert Valid Records into PostgreSQL"):
                        inserted_count = 0
                        duplicate_count = 0

                        for _, row in upload_df.iterrows():
                            company_name = str(row["company_name"]).strip()
                            job_title = str(row["job_title"]).strip()
                            city = str(row["city"]).strip()
                            source_link = str(row["source_link"]).strip()

                            is_duplicate = check_duplicate(
                                company_name=company_name,
                                job_title=job_title,
                                city=city,
                                source_link=source_link
                            )

                            if is_duplicate:
                                duplicate_count += 1
                                continue

                            data = {
                                "company_name": company_name,
                                "job_title": job_title,
                                "category": str(row["category"]).strip(),
                                "city": city,
                                "country": str(row["country"]).strip(),
                                "work_mode": str(row["work_mode"]).strip(),
                                "required_skills": str(row["required_skills"]).strip(),
                                "salary_min": float(row["salary_min"]),
                                "salary_max": float(row["salary_max"]),
                                "currency": str(row["currency"]).strip(),
                                "experience_level": str(row["experience_level"]).strip(),
                                "application_deadline": pd.to_datetime(row["application_deadline"]).date(),
                                "status": str(row["status"]).strip(),
                                "source_link": source_link
                            }

                            insert_opportunity(data)
                            inserted_count += 1

                        st.success(f"{inserted_count} records inserted successfully.")
                        st.warning(f"{duplicate_count} duplicate records skipped.")

        except Exception as error:
            st.error("Failed to process uploaded CSV.")
            st.code(str(error))

with tab2:
    st.subheader("Export Records as CSV")

    try:
        df = fetch_all_opportunities()

        if df.empty:
            st.warning("No records available for export.")
        else:
            st.sidebar.header("Export Filters")

            categories = sorted(df["category"].dropna().unique().tolist())
            statuses = sorted(df["status"].dropna().unique().tolist())
            cities = sorted(df["city"].dropna().unique().tolist())
            work_modes = sorted(df["work_mode"].dropna().unique().tolist())

            selected_categories = st.multiselect("Filter by Category", categories)
            selected_statuses = st.multiselect("Filter by Status", statuses)
            selected_cities = st.multiselect("Filter by City", cities)
            selected_work_modes = st.multiselect("Filter by Work Mode", work_modes)

            filtered_df = df.copy()

            if selected_categories:
                filtered_df = filtered_df[filtered_df["category"].isin(selected_categories)]

            if selected_statuses:
                filtered_df = filtered_df[filtered_df["status"].isin(selected_statuses)]

            if selected_cities:
                filtered_df = filtered_df[filtered_df["city"].isin(selected_cities)]

            if selected_work_modes:
                filtered_df = filtered_df[filtered_df["work_mode"].isin(selected_work_modes)]

            st.write(f"Exporting {len(filtered_df)} of {len(df)} records.")
            st.dataframe(filtered_df, use_container_width=True)

            st.download_button(
                label="Download Filtered CSV",
                data=convert_df_to_csv(filtered_df),
                file_name="filtered_opportunities.csv",
                mime="text/csv"
            )

    except Exception as error:
        st.error("Failed to export records.")
        st.code(str(error))
