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


def check_duplicate(company_name, job_title, city, source_link):
    engine = get_engine()
    query = text("""
        SELECT COUNT(*)
        FROM opportunities
        WHERE LOWER(company_name) = LOWER(:company_name)
          AND LOWER(job_title) = LOWER(:job_title)
          AND LOWER(COALESCE(city, '')) = LOWER(:city)
          AND LOWER(COALESCE(source_link, '')) = LOWER(:source_link);
    """)

    with engine.connect() as connection:
        result = connection.execute(query, {
            "company_name": company_name.strip(),
            "job_title": job_title.strip(),
            "city": city.strip(),
            "source_link": source_link.strip()
        })
        return result.scalar() > 0


def insert_opportunity(data):
    engine = get_engine()
    query = text("""
        INSERT INTO opportunities (
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
            source_link
        )
        VALUES (
            :company_name,
            :job_title,
            :category,
            :city,
            :country,
            :work_mode,
            :required_skills,
            :salary_min,
            :salary_max,
            :currency,
            :experience_level,
            :application_deadline,
            :status,
            :source_link
        );
    """)

    with engine.begin() as connection:
        connection.execute(query, data)


def get_opportunity_by_id(opportunity_id):
    engine = get_engine()
    query = text("""
        SELECT *
        FROM opportunities
        WHERE opportunity_id = :opportunity_id;
    """)

    return pd.read_sql(query, engine, params={"opportunity_id": opportunity_id})


def update_opportunity(opportunity_id, data):
    engine = get_engine()
    query = text("""
        UPDATE opportunities
        SET
            company_name = :company_name,
            job_title = :job_title,
            category = :category,
            city = :city,
            country = :country,
            work_mode = :work_mode,
            required_skills = :required_skills,
            salary_min = :salary_min,
            salary_max = :salary_max,
            currency = :currency,
            experience_level = :experience_level,
            application_deadline = :application_deadline,
            status = :status,
            source_link = :source_link
        WHERE opportunity_id = :opportunity_id;
    """)

    data["opportunity_id"] = opportunity_id

    with engine.begin() as connection:
        connection.execute(query, data)


def delete_opportunity(opportunity_id):
    engine = get_engine()
    query = text("""
        DELETE FROM opportunities
        WHERE opportunity_id = :opportunity_id;
    """)

    with engine.begin() as connection:
        connection.execute(query, {"opportunity_id": opportunity_id})
