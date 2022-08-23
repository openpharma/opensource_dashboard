from datetime import datetime
import streamlit as st
import pandas as pd
from random import randint
from python_functions import df_activity

## Add pharmaverse and overall filters on all metrics

def page_content():
    """Read and display data"""

    
    with open('style/activity.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.title("Overall Open pharma packages insights")

    PATH_REPO = "http://openpharma.s3-website.us-east-2.amazonaws.com/repos_clean.csv"
    PATH_COMMITS = "https://openpharma.s3.us-east-2.amazonaws.com/commits.csv"

    df_repos = df_activity.read_df(PATH_REPO)
    df_commits = df_activity.read_df(PATH_COMMITS)

    pharmaverse = st.selectbox(
        'Choose the scope of the activity : all packages or pharmaverse packages',
        ('All packages', 'Pharmaverse')
    )

    active_repo, evol_repo = df_activity.repo_contrib_activity(df_commits, pharmaverse, "full_name")
    active_contrib, evol_contrib = df_activity.repo_contrib_activity(df_commits, pharmaverse, "author")
    length_pack = df_activity.packages_count(df_repos, pharmaverse)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Nb of packages", 
        "{nb}".format(nb=length_pack)
    )

    col2.metric(
        "Active repos (last 30 days)",
        "{nb}".format(nb=active_repo), 
        "{nb}%".format(nb=evol_repo)
    )

    col3.metric(
        "Active contributors (last 30 days)",
        "{nb}".format(nb=active_contrib),
        "{nb}%".format(nb=evol_contrib)
    )
    
    st.header("Active repositories and people defined by monthly commits")
    chart_data = df_activity.activity_line_chart(df_commits, pharmaverse, datetime(2020,1,1))

    st.line_chart(chart_data[["full_name", "author_clean"]].rename(columns={"full_name": "Nb of Active repositories", "author_clean": "Nb of contributors"}))
