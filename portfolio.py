# portfolio_app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---- SIDEBAR NAVIGATION ----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Projects", "Dashboards", "Blog"])

# ---- ABOUT ME ----
if page == "About Me":
    st.title("👋 Hi, I'm Ashish Gupta")
    st.subheader("Data Analyst | 10+ Years of Experience")

    st.write("""
    Welcome to my portfolio!  
    I'm a data analyst with 10 years of experience in AdTech, Retail Media, and Finance.  
    Skilled in **SQL, Python, Tableau, PySpark, and Data Visualization**.  
    This site is an interactive showcase of my skills and projects.
    """)

    st.download_button("📄 Download My Resume", "Resume_Ashish_Gupta.pdf")

    st.markdown("🔗 [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com) | [Kaggle](https://www.kaggle.com)")

# ---- PROJECTS ----
elif page == "Projects":
    st.title("📂 Projects Showcase")

    with st.expander("SQL Query Optimization"):
        st.write("""
        - Before: 120 sec execution → After: 5 sec  
        - Used CTE restructuring + indexing  
        - Increased efficiency by 24x
        """)

    with st.expander("Retail Media Campaign Dashboard"):
        st.write("""
        Built an interactive dashboard to track impressions, clicks, spend & conversions.  
        Automated reporting pipeline with Python + SQL + Tableau.
        """)

    with st.expander("Finance SIP Calculator"):
        st.write("""
        Developed a SIP (Systematic Investment Plan) calculator to visualize portfolio growth.  
        Useful for investors to compare different mutual funds.
        """)

# ---- DASHBOARDS ----
elif page == "Dashboards":
    st.title("📊 Interactive Dashboards")

    st.subheader("Sample Campaign Performance Dashboard")

    # Dummy dataset
    df = pd.DataFrame({
        "Campaign": ["A", "B", "C", "D"],
        "Impressions": [12000, 18000, 15000, 22000],
        "Clicks": [300, 450, 380, 600],
        "Spend": [5000, 7000, 6000, 9000]
    })
    df["CTR"] = df["Clicks"] / df["Impressions"]

    fig = px.bar(df, x="Campaign", y=["Impressions", "Clicks", "Spend"], 
                 barmode="group", title="Campaign Performance")
    st.plotly_chart(fig)

    st.write("### CTR Table")
    st.dataframe(df)

# ---- BLOG ----
elif page == "Blog":
    st.title("📝 Blog / Articles")

    st.markdown("""
    ### 📌 Basics of PySpark for Data Analysts
    PySpark is a great tool to handle large-scale data. It helps analysts process TBs of data efficiently.  
    Example: `df.groupBy("column").agg({"metric":"sum"})`

    ---

    ### 📌 SQL Best Practices
    - Use CTEs for readability  
    - Avoid SELECT * in production  
    - Index frequently joined columns  

    """)
