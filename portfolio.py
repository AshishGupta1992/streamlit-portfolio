# portfolio_resume_app.py
import streamlit as st

# ---------------------------
# Sidebar Navigation
# ---------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Profile", "Skills", "Experience", "Education", "Download Resume"])

# ---------------------------
# Profile Section
# ---------------------------
if page == "Profile":
    st.title("👨‍💻 Ashish Gupta")
    st.subheader("Analytics Manager | Data Analyst | 10+ Years Experience")

    st.markdown("""
    Data-driven Analytics Manager with 8+ years of experience; I excel at converting raw data into valuable insights 
    that drive business decisions.  
    Proficient in **Tableau, Power BI, MySQL, ETL processes, and AWS**, I specialize in data visualization, reporting, 
    and ML model development to propel business growth.  
    With a knack for leadership, I have a proven record of effectively managing and nurturing data analyst teams.
    """)

    st.markdown("📞 Phone: **7022450444**")  
    st.markdown("📧 Email: [ashish.gp10@gmail.com](mailto:ashish.gp10@gmail.com)")  
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/ashishgupta92/)")  

    st.success("Invited by Tableau & CIMR, Mumbai, as a guest lecturer to present analytics and ML work.")

# ---------------------------
# Skills Section
# ---------------------------
elif page == "Skills":
    st.title("🛠️ Skills")

    skills = [
        "Tableau", "Power BI", "Python (Numpy, Pandas, Scikit Learn)", "MySQL", "ETL",
        "AWS", "Machine Learning (AI/ML)", "Flask API", "VBA Macros",
        "JIRA", "Data Visualization", "Data Driven Decision Making", "Stakeholder Management"
    ]

    st.write(", ".join(skills))

    st.progress(85)  # Just to show progress-like effect

# ---------------------------
# Experience Section
# ---------------------------
elif page == "Experience":
    st.title("💼 Work Experience")

    st.subheader("Analytics Manager – MCube Financial Services (2020–Present)")
    st.write("""
    - Spearheaded SaaS solution development with AI/ML models  
    - Managed loan portfolio monitoring dashboards (Tableau) → reduced time 70%  
    - Automated financial data pipelines with Python + AWS → 75% manual effort saved  
    - ML-based document classification with 97% accuracy  
    """)

    st.subheader("Tech Lead (Business Analyst) – Pinkerton (2019–2020)")
    st.write("""
    - Led team of 6, created Tableau dashboards consolidating data  
    - Handled C-level stakeholder management (CEO, VP Finance)  
    - Revenue prediction using ML → generated $5M revenue  
    - Built OCR system for ID documents → reduced time 1 day → 2 hours  
    """)

    st.subheader("Data Analyst – Zycus (2017–2019)")
    st.write("""
    - Built reporting infra with Tableau + SQL for recruitment metrics  
    - Reduced hiring TAT by 15 days  
    - Automated offer letter generation (Python Flask) → 80% faster process  
    """)

    st.subheader("Associate Analyst – IBM (2015–2017)")
    st.write("""
    - Data extraction from DB2, SQL warehouses  
    - Built statistical models + Tableau dashboards for inventory forecasting  
    """)

# ---------------------------
# Education Section
# ---------------------------
elif page == "Education":
    st.title("🎓 Education")

    st.write("""
    - **Post Graduation Program (Product Management, 2024)** – IIM Indore  
    - **B.Tech IT (2015)** – JUIT Solan, Himachal Pradesh  
    - **Higher Secondary (2011)** – Abhinav Public School, Delhi (CBSE)  
    - **Senior Secondary (2009)** – DAV Public School, Delhi (CBSE)  
    """)

# ---------------------------
# Resume Download
# ---------------------------
elif page == "Download Resume":
    st.title("📄 Download My Resume")

    with open("Ashish Gupta Resume.docx", "rb") as file:
        btn = st.download_button(
            label="Download Resume (Word)",
            data=file,
            file_name="Ashish_Gupta_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
