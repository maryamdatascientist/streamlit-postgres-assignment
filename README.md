# Internship & Job Tracking Dashboard

A complete Streamlit + PostgreSQL + Docker Compose web application for managing internship and job opportunities for students.

The system allows faculty members to add, view, search, update, delete, upload, export, analyze, and verify internship/job records using a real PostgreSQL database.

---

## GitHub Repository

Repository Link:

```text
https://github.com/maryamdatascientist/streamlit-postgres-assignment
```

---

## Project Features

The application includes the following modules:

1. Home / Introduction
2. Add New Opportunity
3. View and Search Opportunities
4. Update Opportunity
5. Delete Opportunity
6. Analytics Dashboard
7. CSV Upload / Bulk Insert
8. CSV Export
9. Duplicate Detection
10. Deadline Alerts
11. Database Health Check
12. Login / Role-Based Access Control

---

## Tools and Technologies Used

| Tool / Library  | Purpose                                  |
| --------------- | ---------------------------------------- |
| Python          | Application programming language         |
| Streamlit       | Frontend web application                 |
| PostgreSQL      | Permanent relational database            |
| pgAdmin         | Database inspection and SQL verification |
| Docker Desktop  | Container runtime                        |
| Docker Compose  | Multi-container setup                    |
| pandas          | CSV handling and data processing         |
| SQLAlchemy      | Database connection layer                |
| psycopg2-binary | PostgreSQL driver                        |
| Plotly          | Interactive dashboard charts             |
| Git and GitHub  | Version control and collaboration        |

---

## Login Credentials

The application supports two roles.

### Admin

Admin can add, update, delete, upload CSV, export CSV, and access all pages.

```text
Username: admin
Password: admin123
```

### Viewer

Viewer can view records, dashboard, duplicate detection, deadline alerts, and database health check.

```text
Username: viewer
Password: viewer123
```

---

## Project Folder Structure

```text
streamlit-postgres-assignment/
|
├── app/
│   ├── main.py
│   ├── db.py
│   ├── queries.py
│   ├── auth.py
│   ├── utils.py
│   └── pages/
│       ├── 1_Add_Opportunity.py
│       ├── 2_View_Search.py
│       ├── 3_Update_Opportunity.py
│       ├── 4_Delete_Opportunity.py
│       ├── 5_Analytics_Dashboard.py
│       ├── 6_CSV_Upload_Export.py
│       ├── 7_Duplicate_Detection.py
│       ├── 8_Deadline_Alerts.py
│       └── 9_Database_Health_Check.py
|
├── database/
│   ├── init.sql
│   └── seed_data.sql
|
├── screenshots/
│   ├── home_page.png
│   ├── add_form.png
│   ├── pgadmin_connection.png
│   ├── postgres_table.png
│   ├── github_commits.png
│   └── analytics_dashboard.png
|
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
└── report.pdf
```

---

## Database Design

Database name:

```text
student_opportunities_db
```

Main table:

```text
opportunities
```

Important columns:

| Column               | Description                              |
| -------------------- | ---------------------------------------- |
| opportunity_id       | Primary key                              |
| company_name         | Company name                             |
| job_title            | Internship or job title                  |
| category             | Job category                             |
| city                 | City                                     |
| country              | Country                                  |
| work_mode            | Remote, Onsite, or Hybrid                |
| required_skills      | Required technical skills                |
| salary_min           | Minimum salary                           |
| salary_max           | Maximum salary                           |
| currency             | Currency such as PKR, USD, EUR           |
| experience_level     | Internship, Entry Level, Mid Level, etc. |
| application_deadline | Last date to apply                       |
| status               | Open, Closed, Expired, or Shortlisted    |
| source_link          | Source URL                               |
| created_at           | Record creation timestamp                |

The database is created automatically using:

```text
database/init.sql
```

Sample data is inserted automatically using:

```text
database/seed_data.sql
```

The project includes at least 40 sample records with multiple companies, cities, categories, work modes, salaries, currencies, and statuses.

---

## Docker Compose Services

The project uses Docker Compose to run three services.

| Service       | Container Name        | Port      | Purpose              |
| ------------- | --------------------- | --------- | -------------------- |
| postgres_db   | opportunity_postgres  | 5432:5432 | PostgreSQL database  |
| pgadmin       | opportunity_pgadmin   | 5050:80   | pgAdmin database GUI |
| streamlit_app | opportunity_streamlit | 8501:8501 | Streamlit web app    |

---

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/maryamdatascientist/streamlit-postgres-assignment.git
cd streamlit-postgres-assignment
```

### Step 2: Start Docker Desktop

Make sure Docker Desktop is running before executing Docker commands.

### Step 3: Build and Run All Services

```bash
docker compose up -d --build
```

This command starts:

* PostgreSQL
* pgAdmin
* Streamlit app

### Step 4: Check Running Containers

```bash
docker compose ps
```

Expected containers:

```text
opportunity_postgres
opportunity_pgadmin
opportunity_streamlit
```

### Step 5: Open the Streamlit App

```text
http://localhost:8501
```

### Step 6: Open pgAdmin

```text
http://localhost:5050
```

pgAdmin login:

```text
Email: admin@example.com
Password: admin123
```

---

## pgAdmin Server Registration

After logging into pgAdmin, register a new server.

### General Tab

```text
Name: Opportunity DB
```

### Connection Tab

```text
Host name/address: postgres_db
Port: 5432
Maintenance database: student_opportunities_db
Username: app_user
Password: app_password
```

Important: Use `postgres_db` as the host name because pgAdmin and PostgreSQL are running inside Docker Compose network.

---

## Required SQL Verification Queries

Run these queries in pgAdmin Query Tool.

```sql
SELECT * FROM opportunities;
```

```sql
SELECT COUNT(*) FROM opportunities;
```

```sql
SELECT category, COUNT(*)
FROM opportunities
GROUP BY category;
```

```sql
SELECT work_mode, COUNT(*)
FROM opportunities
GROUP BY work_mode;
```

```sql
SELECT *
FROM opportunities
WHERE status = 'Open';
```

```sql
SELECT *
FROM opportunities
WHERE application_deadline <= CURRENT_DATE + INTERVAL '7 days';
```

---

## Docker Commands

### Start all services

```bash
docker compose up -d
```

Starts PostgreSQL, pgAdmin, and Streamlit in detached mode.

### Build and start all services

```bash
docker compose up -d --build
```

Rebuilds the Streamlit image and starts all containers.

### Check running services

```bash
docker compose ps
```

Shows container names, status, and mapped ports.

### View PostgreSQL logs

```bash
docker compose logs postgres_db
```

### View pgAdmin logs

```bash
docker compose logs pgadmin
```

### View Streamlit logs

```bash
docker compose logs streamlit_app
```

### Stop containers but keep database volume

```bash
docker compose down
```

### List Docker volumes

```bash
docker volume ls
```

### Inspect PostgreSQL volume

```bash
docker volume inspect streamlit-postgres-assignment_postgres_data
```

### Stop containers and delete volumes

```bash
docker compose down -v
```

Warning: This deletes the PostgreSQL volume and removes stored database data. On next startup, `init.sql` and `seed_data.sql` will recreate the database and sample records.

---

## Application Pages

### Home / Introduction

Displays project title, tools used, login credentials, database connection status, and total opportunities.

### Add New Opportunity

Allows Admin users to insert a new internship or job opportunity with form validation and duplicate checking.

### View and Search

Allows logged-in users to view all opportunities and filter records by:

* Search text
* Category
* City
* Work mode
* Status
* Experience level
* Salary range

### Update Opportunity

Allows Admin users to select an existing record and update fields such as status, salary, deadline, skills, work mode, and source link.

### Delete Opportunity

Allows Admin users to preview a selected record and delete it after confirmation.

### Analytics Dashboard

Displays KPIs and charts, including:

* Total opportunities
* Open jobs
* Closed jobs
* Expired jobs
* Remote jobs
* Company count
* Average salary
* Shortlisted jobs
* Opportunities by category
* Opportunities by city
* Status distribution
* Work mode distribution
* Salary analysis
* Top required skills
* Deadline trends

### CSV Upload / Export

Allows Admin users to:

* Download a CSV template
* Upload a CSV file
* Validate CSV columns and data
* Insert valid records into PostgreSQL
* Skip duplicate records
* Export filtered records as CSV

### Duplicate Detection

Detects likely duplicate opportunities using:

```text
company_name + job_title + city + source_link
```

### Deadline Alerts

Shows:

* Opportunities closing within 7 days
* Opportunities expired based on application deadline
* Opportunities marked as Expired status

### Database Health Check

Shows:

* PostgreSQL connection status
* PostgreSQL version
* Current database
* Current user
* Table existence
* Total row count
* Latest record
* Table columns
* Manual verification SQL queries

---

## GitHub Workflow

The project uses Git and GitHub for version control.

Common commands used:

```bash
git status
git add .
git commit -m "meaningful commit message"
git push
```

Example meaningful commits:

```text
Initial project structure
Add database schema and seed data
Add Docker Compose PostgreSQL pgAdmin and Streamlit setup
Connect Streamlit app with PostgreSQL database
Create view and search opportunities page
Create add opportunity form with validation
Create update opportunity page
Create delete opportunity page
Create analytics dashboard with KPIs and charts
Create CSV upload and export page
Create duplicate detection page
Create deadline alerts page
Create database health check page
Add login system and role based access control
```

---

## Contribution Table

| Member Name    | GitHub Username     | Contribution                                                                                                                                                          |
| -------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maryam         | maryamdatascientist |  setup, Docker Compose, PostgreSQL schema, seed data, pages        |
| Fatima         | TODO                |  CRUD, dashboard, CSV, duplicate detection, deadline alerts,       |
| Syeda Aniqa    | TODO                |  seed data, Streamlit pages, login system, documentation           |

---

## Screenshots

Required screenshots are stored in the `screenshots/` folder.

| Screenshot           | File                                |
| -------------------- | ----------------------------------- |
| Home Page            | screenshots/home_page.png           |
| Add Opportunity Form | screenshots/add_form.png            |
| pgAdmin Connection   | screenshots/pgadmin_connection.png  |
| PostgreSQL Table     | screenshots/postgres_table.png      |
| GitHub Commits       | screenshots/github_commits.png      |
| Analytics Dashboard  | screenshots/analytics_dashboard.png |

---

## Troubleshooting

### Docker Desktop is not running

Error:

```text
Cannot connect to the Docker daemon
```

Solution:

Start Docker Desktop and wait until it is fully running.

---

### Port 5432 already in use

PostgreSQL port is already being used by another local PostgreSQL service.

Solution:

Stop the local PostgreSQL service or change the mapped port in `docker-compose.yml`.

---

### Port 5050 already in use

pgAdmin port is already being used.

Solution:

Change:

```yaml
ports:
  - "5050:80"
```

to another port such as:

```yaml
ports:
  - "5051:80"
```

---

### Port 8501 already in use

Streamlit port is already being used.

Solution:

Stop the running Streamlit process or change the mapped port.

---

### pgAdmin cannot connect to PostgreSQL

Check these values:

```text
Host: postgres_db
Port: 5432
Username: app_user
Password: app_password
Database: student_opportunities_db
```

Do not use `localhost` as the host inside pgAdmin when both pgAdmin and PostgreSQL are running in Docker.

---

### Table does not exist

This can happen if database initialization scripts did not run.

Solution:

```bash
docker compose down -v
docker compose up -d --build
```

Warning: `docker compose down -v` deletes the database volume.

---

### CSV upload fails

Common reasons:

* Missing required columns
* Invalid category
* Invalid work mode
* Invalid status
* Invalid currency
* salary_max is less than salary_min
* Invalid date format

Use the CSV template download button from the CSV Upload page.

---

### Streamlit cannot connect to database

Check that all containers are running:

```bash
docker compose ps
```

Check Streamlit logs:

```bash
docker compose logs streamlit_app
```

Check PostgreSQL logs:

```bash
docker compose logs postgres_db
```

---

## References

* Streamlit Documentation: https://docs.streamlit.io/
* Docker Compose Documentation: https://docs.docker.com/compose/
* PostgreSQL Docker Official Image: https://hub.docker.com/_/postgres
* pgAdmin Documentation: https://www.pgadmin.org/docs/
* SQLAlchemy Documentation: https://docs.sqlalchemy.org/
* Plotly Python Documentation: https://plotly.com/python/
* GitHub Documentation: https://docs.github.com/

---

## Final Output

The completed project provides:

* A Dockerized Streamlit application
* A PostgreSQL database with a persistent volume
* pgAdmin verification support
* CRUD operations
* Search and filters
* CSV upload and export
* Duplicate detection
* Deadline alerts
* Analytics dashboard
* Admin and Viewer login system
* GitHub version control evidence
* Reproducible setup through Docker Compose
