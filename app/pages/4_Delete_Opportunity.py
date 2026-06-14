from auth import require_admin
import streamlit as st
from queries import fetch_all_opportunities, get_opportunity_by_id, delete_opportunity

st.set_page_config(
    page_title="Delete Opportunity",
    page_icon="🗑️",
    layout="wide"
)

require_admin()


st.title("Delete Opportunity")

st.warning("Delete operation is permanent. Use this page only for invalid or duplicate records.")

try:
    df = fetch_all_opportunities()

    if df.empty:
        st.info("No opportunities available to delete.")
    else:
        opportunity_options = {
            f"{row.opportunity_id} - {row.company_name} - {row.job_title}": row.opportunity_id
            for row in df.itertuples()
        }

        selected_label = st.selectbox(
            "Select Opportunity to Delete",
            list(opportunity_options.keys())
        )

        selected_id = opportunity_options[selected_label]
        selected_df = get_opportunity_by_id(selected_id)

        if selected_df.empty:
            st.error("Selected opportunity not found.")
        else:
            st.subheader("Record Preview")
            st.dataframe(selected_df, use_container_width=True)

            st.error("Are you sure you want to delete this record?")

            confirm_delete = st.checkbox("Yes, I confirm this record should be deleted.")

            if st.button("Delete Opportunity", type="primary"):
                if not confirm_delete:
                    st.warning("Please tick the confirmation checkbox before deleting.")
                else:
                    delete_opportunity(selected_id)
                    st.success(f"Opportunity ID {selected_id} deleted successfully.")
                    st.info("Open View/Search page to verify the record has been removed.")

except Exception as error:
    st.error("Failed to delete opportunity.")
    st.code(str(error))
