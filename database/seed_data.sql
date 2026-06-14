TRUNCATE TABLE opportunities RESTART IDENTITY CASCADE;

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
) VALUES
('Google', 'Data Analyst Intern', 'Data Science', 'Lahore', 'Pakistan', 'Remote', 'Python, SQL, Excel, Pandas', 40000, 70000, 'PKR', 'Internship', '2026-06-20', 'Open', 'https://careers.google.com/data-analyst-intern-lhr'),
('Microsoft', 'Junior Data Scientist', 'Data Science', 'Karachi', 'Pakistan', 'Hybrid', 'Python, Machine Learning, SQL, Power BI', 90000, 140000, 'PKR', 'Entry Level', '2026-07-05', 'Open', 'https://careers.microsoft.com/junior-data-scientist-khi'),
('IBM', 'AI Research Intern', 'AI', 'Islamabad', 'Pakistan', 'Onsite', 'Python, NLP, TensorFlow, Research', 50000, 85000, 'PKR', 'Internship', '2026-06-18', 'Open', 'https://careers.ibm.com/ai-research-intern-isl'),
('Systems Ltd', 'Web Developer Intern', 'Web Development', 'Lahore', 'Pakistan', 'Onsite', 'HTML, CSS, JavaScript, React', 30000, 50000, 'PKR', 'Internship', '2026-06-25', 'Shortlisted', 'https://systems.com/careers/web-dev-intern'),
('Arbisoft', 'Software Engineer Trainee', 'Software Engineering', 'Lahore', 'Pakistan', 'Hybrid', 'Python, Django, Git, REST APIs', 70000, 110000, 'PKR', 'Entry Level', '2026-07-10', 'Open', 'https://arbisoft.com/careers/software-engineer-trainee'),
('NETSOL', 'Cyber Security Analyst Intern', 'Cyber Security', 'Lahore', 'Pakistan', 'Onsite', 'Networking, Linux, Security Tools, SIEM', 45000, 65000, 'PKR', 'Internship', '2026-06-12', 'Expired', 'https://netsoltech.com/careers/cyber-security-intern'),

('10Pearls', 'Machine Learning Intern', 'AI', 'Karachi', 'Pakistan', 'Remote', 'Python, Scikit-learn, Pandas, ML Models', 35000, 60000, 'PKR', 'Internship', '2026-06-30', 'Open', 'https://10pearls.com/careers/ml-intern'),
('Afiniti', 'Data Engineer Associate', 'Data Science', 'Islamabad', 'Pakistan', 'Hybrid', 'SQL, Python, ETL, Spark', 100000, 160000, 'PKR', 'Entry Level', '2026-07-15', 'Open', 'https://afiniti.com/careers/data-engineer-associate'),
('Contour Software', 'Frontend Developer', 'Web Development', 'Karachi', 'Pakistan', 'Hybrid', 'React, TypeScript, CSS, APIs', 120000, 180000, 'PKR', 'Mid Level', '2026-07-20', 'Open', 'https://contour-software.com/frontend-developer'),
('Tkxel', 'Backend Developer Intern', 'Software Engineering', 'Lahore', 'Pakistan', 'Onsite', 'Node.js, Express, MongoDB, Git', 40000, 70000, 'PKR', 'Internship', '2026-06-28', 'Open', 'https://tkxel.com/careers/backend-intern'),

('Google', 'Cloud Security Intern', 'Cyber Security', 'Islamabad', 'Pakistan', 'Remote', 'Cloud Security, IAM, Linux, Networking', 60000, 90000, 'PKR', 'Internship', '2026-07-01', 'Open', 'https://careers.google.com/cloud-security-intern'),
('Microsoft', 'AI Product Intern', 'AI', 'Lahore', 'Pakistan', 'Remote', 'Python, Product Analytics, AI Tools, SQL', 55000, 85000, 'PKR', 'Internship', '2026-06-22', 'Shortlisted', 'https://careers.microsoft.com/ai-product-intern'),
('IBM', 'Database Administrator Trainee', 'Software Engineering', 'Karachi', 'Pakistan', 'Onsite', 'SQL, PostgreSQL, Backup, Performance Tuning', 65000, 95000, 'PKR', 'Entry Level', '2026-06-10', 'Expired', 'https://careers.ibm.com/dba-trainee'),
('Systems Ltd', 'Business Intelligence Analyst', 'Data Science', 'Islamabad', 'Pakistan', 'Hybrid', 'Power BI, SQL, Excel, Data Modeling', 100000, 150000, 'PKR', 'Entry Level', '2026-07-12', 'Closed', 'https://systems.com/careers/bi-analyst'),
('Arbisoft', 'React Developer Intern', 'Web Development', 'Faisalabad', 'Pakistan', 'Remote', 'React, JavaScript, HTML, CSS', 30000, 55000, 'PKR', 'Internship', '2026-07-03', 'Open', 'https://arbisoft.com/careers/react-intern'),

('NETSOL', 'QA Automation Engineer', 'Software Engineering', 'Lahore', 'Pakistan', 'Hybrid', 'Selenium, Python, Testing, Git', 90000, 130000, 'PKR', 'Entry Level', '2026-06-21', 'Open', 'https://netsoltech.com/careers/qa-automation'),
('10Pearls', 'Cyber Security Trainee', 'Cyber Security', 'Karachi', 'Pakistan', 'Onsite', 'Network Security, Linux, Firewalls, SOC', 50000, 80000, 'PKR', 'Entry Level', '2026-06-26', 'Open', 'https://10pearls.com/careers/cyber-trainee'),
('Afiniti', 'NLP Engineer Intern', 'AI', 'Islamabad', 'Pakistan', 'Hybrid', 'Python, NLP, Transformers, Data Cleaning', 60000, 95000, 'PKR', 'Internship', '2026-07-08', 'Open', 'https://afiniti.com/careers/nlp-intern'),
('Contour Software', 'Full Stack Developer', 'Web Development', 'Karachi', 'Pakistan', 'Onsite', 'React, Node.js, PostgreSQL, Docker', 160000, 240000, 'PKR', 'Mid Level', '2026-07-25', 'Open', 'https://contour-software.com/fullstack-developer'),
('Tkxel', 'Data Visualization Intern', 'Data Science', 'Lahore', 'Pakistan', 'Remote', 'Python, Plotly, Power BI, Pandas', 35000, 60000, 'PKR', 'Internship', '2026-06-19', 'Open', 'https://tkxel.com/careers/data-viz-intern'),

('Google', 'Software Engineering Intern', 'Software Engineering', 'Karachi', 'Pakistan', 'Remote', 'Java, Python, Algorithms, Git', 70000, 120000, 'PKR', 'Internship', '2026-08-01', 'Open', 'https://careers.google.com/software-engineering-intern'),
('Microsoft', 'Security Operations Analyst', 'Cyber Security', 'Islamabad', 'Pakistan', 'Hybrid', 'SIEM, Incident Response, Linux, Networking', 130000, 190000, 'PKR', 'Mid Level', '2026-07-18', 'Open', 'https://careers.microsoft.com/security-operations-analyst'),
('IBM', 'Frontend Engineer Trainee', 'Web Development', 'Lahore', 'Pakistan', 'Onsite', 'HTML, CSS, JavaScript, Angular', 65000, 100000, 'PKR', 'Entry Level', '2026-06-23', 'Shortlisted', 'https://careers.ibm.com/frontend-engineer-trainee'),
('Systems Ltd', 'AI Chatbot Developer', 'AI', 'Karachi', 'Pakistan', 'Hybrid', 'Python, LLMs, APIs, NLP', 140000, 220000, 'PKR', 'Mid Level', '2026-07-28', 'Open', 'https://systems.com/careers/ai-chatbot-developer'),
('Arbisoft', 'Data Quality Analyst', 'Data Science', 'Faisalabad', 'Pakistan', 'Remote', 'SQL, Excel, Data Cleaning, Python', 60000, 90000, 'PKR', 'Entry Level', '2026-06-16', 'Open', 'https://arbisoft.com/careers/data-quality-analyst'),

('NETSOL', 'DevOps Intern', 'Software Engineering', 'Islamabad', 'Pakistan', 'Hybrid', 'Docker, Linux, CI/CD, GitHub Actions', 50000, 85000, 'PKR', 'Internship', '2026-07-06', 'Open', 'https://netsoltech.com/careers/devops-intern'),
('10Pearls', 'Python Developer', 'Software Engineering', 'Lahore', 'Pakistan', 'Onsite', 'Python, FastAPI, PostgreSQL, Git', 110000, 170000, 'PKR', 'Entry Level', '2026-07-16', 'Closed', 'https://10pearls.com/careers/python-developer'),
('Afiniti', 'MLOps Intern', 'AI', 'Islamabad', 'Pakistan', 'Remote', 'Python, Docker, MLflow, Git', 65000, 100000, 'PKR', 'Internship', '2026-06-24', 'Open', 'https://afiniti.com/careers/mlops-intern'),
('Contour Software', 'Application Security Engineer', 'Cyber Security', 'Karachi', 'Pakistan', 'Hybrid', 'OWASP, Pen Testing, APIs, Security Reviews', 150000, 230000, 'PKR', 'Mid Level', '2026-08-05', 'Open', 'https://contour-software.com/app-security-engineer'),
('Tkxel', 'UI Developer Intern', 'Web Development', 'Lahore', 'Pakistan', 'Onsite', 'HTML, CSS, Bootstrap, JavaScript', 25000, 45000, 'PKR', 'Internship', '2026-06-15', 'Expired', 'https://tkxel.com/careers/ui-developer-intern'),

('Google', 'Analytics Engineer', 'Data Science', 'Faisalabad', 'Pakistan', 'Remote', 'SQL, dbt, Python, Data Warehousing', 180000, 280000, 'PKR', 'Mid Level', '2026-07-30', 'Open', 'https://careers.google.com/analytics-engineer'),
('Microsoft', 'Junior Backend Engineer', 'Software Engineering', 'Karachi', 'Pakistan', 'Hybrid', 'C#, .NET, SQL Server, APIs', 100000, 160000, 'PKR', 'Entry Level', '2026-07-09', 'Open', 'https://careers.microsoft.com/junior-backend-engineer'),
('IBM', 'SOC Analyst Intern', 'Cyber Security', 'Islamabad', 'Pakistan', 'Onsite', 'SIEM, Logs, Network Security, Linux', 45000, 70000, 'PKR', 'Internship', '2026-06-29', 'Open', 'https://careers.ibm.com/soc-analyst-intern'),
('Systems Ltd', 'Data Science Intern', 'Data Science', 'Lahore', 'Pakistan', 'Remote', 'Python, Pandas, SQL, Statistics', 40000, 70000, 'PKR', 'Internship', '2026-07-02', 'Open', 'https://systems.com/careers/data-science-intern'),
('Arbisoft', 'Angular Developer', 'Web Development', 'Lahore', 'Pakistan', 'Hybrid', 'Angular, TypeScript, RxJS, REST APIs', 130000, 200000, 'PKR', 'Mid Level', '2026-07-22', 'Open', 'https://arbisoft.com/careers/angular-developer'),

('NETSOL', 'AI Data Annotator', 'AI', 'Faisalabad', 'Pakistan', 'Remote', 'Data Labeling, Excel, QA, AI Basics', 35000, 55000, 'PKR', 'Entry Level', '2026-06-27', 'Open', 'https://netsoltech.com/careers/ai-data-annotator'),
('10Pearls', 'Junior Penetration Tester', 'Cyber Security', 'Karachi', 'Pakistan', 'Hybrid', 'Burp Suite, OWASP, Linux, Reporting', 90000, 150000, 'PKR', 'Entry Level', '2026-07-14', 'Open', 'https://10pearls.com/careers/junior-penetration-tester'),
('Afiniti', 'Data Analyst', 'Data Science', 'Islamabad', 'Pakistan', 'Onsite', 'SQL, Excel, Python, Dashboarding', 90000, 135000, 'PKR', 'Entry Level', '2026-07-11', 'Shortlisted', 'https://afiniti.com/careers/data-analyst'),
('Contour Software', 'React Native Intern', 'Software Engineering', 'Karachi', 'Pakistan', 'Remote', 'React Native, JavaScript, APIs, Git', 40000, 65000, 'PKR', 'Internship', '2026-06-17', 'Open', 'https://contour-software.com/react-native-intern'),
('Contour Software', 'React Native Intern', 'Software Engineering', 'Karachi', 'Pakistan', 'Remote', 'React Native, JavaScript, APIs, Git', 40000, 65000, 'PKR', 'Internship', '2026-06-17', 'Open', 'https://contour-software.com/react-native-intern');
