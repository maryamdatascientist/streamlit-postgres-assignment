from auth import require_login
import streamlit as st
from queries import find_duplicate_opportunities

st.set_page_config(
    page_title="Duplicate Detection",
    page_icon="🧩",
    layout="wide"
)

require_login()


st.title("Duplicate Detection")

st.info(
    "This page detects likely duplicate opportunities using company name, job title, city, and source link."
)

try:
    duplicate_df = find_duplicate_opportunities()

    if duplicate_df.empty:
        st.success("No duplicate opportunities found.")
    else:
        total_duplicate_rows = len(duplicate_df)
        duplicate_groups = duplicate_df[
            ["company_name", "job_title", "city", "source_link"]
        ].drop_duplicates().shape[0]

        col1, col2 = st.columns(2)
        col1.metric("Duplicate Groups", duplicate_groups)
        col2.metric("Duplicate Rows", total_duplicate_rows)

        st.warning("Possible duplicate opportunities found.")

        st.subheader("Duplicate Records")
        st.dataframe(duplicate_df, use_container_width=True)

        st.subheader("Duplicate Summary")

        summary_df = (
            duplicate_df.groupby(
                ["company_name", "job_title", "city", "source_link"],
                dropna=False
            )
            .size()
            .reset_index(name="duplicate_count")
            .sort_values(by="duplicate_count", ascending=False)
        )

        st.dataframe(summary_df, use_container_width=True)

        st.info(
            "Use the Delete Opportunity page to remove invalid duplicate records after manual review."
        )

except Exception as error:
    st.error("Failed to detect duplicates.")
    st.code(str(error))
