import pandas as pd
from sqlalchemy import text
from db import get_engine


def fetch_all_opportunities():
    engine = get_engine()
    query = """
        SELECT 
            opportunity_id,
            company_name,
            job_title,
            category,
            city,
            country,
            work_mode,
            required_skills,
            salary_min,
            salary_max,
            currency,
            experience_level,
            application_deadline,
            status,
            source_link,
            created_at
        FROM opportunities
        ORDER BY opportunity_id;
    """
    return pd.read_sql(query, engine)


def get_total_records():
    engine = get_engine()
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM opportunities;"))
        return result.scalar()
