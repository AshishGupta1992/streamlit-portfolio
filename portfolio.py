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
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("profile_image.jpeg", width=180)  # <-- add your image in same folder
    with col2:
        st.title("👨‍💻 Ashish Gupta")
        st.subheader("Analytics Manager | Data Analyst | 10+ Years Experience")
        st.markdown("📧 [ashish.gp10@gmail.com](mailto:ashish.gp10@gmail.com)")
        st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/ashishgupta92/)")
        st.markdown("📞 Phone: **7022450444**")

    st.markdown("---")
    st.markdown("""
    Data-driven Analytics Manager with 8+ years of experience; I excel at converting raw data into valuable insights 
    that drive business decisions.  
    Proficient in **Tableau, Power BI, MySQL, ETL processes, and AWS**, I specialize in data visualization, reporting, 
    and ML model development to propel business growth.  
    With a knack for leadership, I have a proven record of effectively managing and nurturing data analyst teams.
    """) 

    st.success("Invited by Tableau & CIMR, Mumbai, as a guest lecturer to present analytics and ML work.")

# ---------------------------
# Skills Section
# ---------------------------
elif page == "Skills":
    st.title("🛠️ Skills")

    skills = {
        "Python (Numpy, Pandas, Scikit-Learn)": 90,
        "SQL / MySQL": 85,
        "Tableau / Power BI": 95,
        "Machine Learning": 80,
        "AWS": 75,
        "ETL & Data Pipelines": 85,
        "Stakeholder Management": 90
    }

    for skill, percent in skills.items():
        st.write(f"**{skill}**")
        st.progress(percent)


# ---------------------------
# Experience Section
# ---------------------------
elif page == "Experience":
    st.title("📅 Career Timeline")

    with st.expander("2020 – Present | Analytics Manager @ MCube Financial Services"):
        st.write("""
        - Spearheaded SaaS solution development with AI/ML models  
        - Managed loan portfolio monitoring dashboards (Tableau) → reduced time 70%  
        - Automated financial data pipelines with Python + AWS → 75% manual effort saved  
        - ML-based document classification with 97% accuracy  
        """)

    with st.expander("2019 – 2020 | Tech Lead (Business Analyst) @ Pinkerton"):
        st.write("""
        - Led team of 6, created Tableau dashboards consolidating data  
        - Handled C-level stakeholder management (CEO, VP Finance)  
        - Revenue prediction using ML → generated $5M revenue  
        - Built OCR system for ID documents → reduced time 1 day → 2 hours  
        """)

    with st.expander("2017 – 2019 | Data Analyst @ Zycus"):
        st.write("""
        - Built reporting infra with Tableau + SQL for recruitment metrics  
        - Reduced hiring TAT by 15 days  
        - Automated offer letter generation (Python Flask) → 80% faster process  
        """)

    with st.expander("2015 – 2017 | Associate Analyst @ IBM"):
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
# Portfolio Projects Section
# ---------------------------
elif page == "Portfolio Projects":
    st.title("📊 Portfolio Projects")

    projects = {
        "Sales Forecasting with ML": "https://share.streamlit.io/ashish/sales-forecast",
        "Tableau Dashboard – Retail Analytics": "https://public.tableau.com/xyz",
        "SQL Case Study – Customer Churn": "https://github.com/ashish/churn-sql"
    }

    for name, link in projects.items():
        st.markdown(f"🔗 [{name}]({link})")

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



