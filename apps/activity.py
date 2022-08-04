import streamlit as st
import pandas as pd
from random import randint
from python_functions import df_activity

def page_content():
    """Read and display data"""

    
    with open('style/activity.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.title("Overall Open pharma packages insights")

    PATH_REPO = "http://openpharma.s3-website.us-east-2.amazonaws.com/repos_clean.csv"
    PATH_COMMITS = "https://openpharma.s3.us-east-2.amazonaws.com/commits.csv"
    df_repos = df_activity.read_repos(PATH_REPO)
    df_commits = df_activity.read_commits(PATH_COMMITS)
    active_repo, evol_repo = df_activity.repo_contrib_activity(df_commits, "full_name")
    active_contrib, evol_contrib = df_activity.repo_contrib_activity(df_commits, "author")


    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Nb of packages", 
        "{nb}".format(nb=len(df_repos))
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
    
    st.header("!not real data for the moment! Cumulative trend of #contributors and #repos")
    chart_data = pd.DataFrame(
        [[randint(60, 120), randint(80, 200)] for i in range(0, 100)],
        columns=['Contributors', 'Repos']
    )

    st.line_chart(chart_data)
