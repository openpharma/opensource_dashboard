import streamlit as st
import pandas as pd
from random import randint
from python_functions import df_activity

def page_content():
    with open('style/activity.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.title("Not real Data!")

    PATH = 'http://openpharma.s3-website.us-east-2.amazonaws.com/repos_clean.csv'
    df = df_activity.read_repos_clean(PATH)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Nb of packages", "{nb}".format(nb=len(df)))
    col2.metric("Active repos", "112", "+3%")
    col3.metric("Active contributors", "256", "-2%")
    col4.metric("Docs Ratio", "86%")
    
    st.header("Cumulative trend of #contributors and #repos")
    chart_data = pd.DataFrame(
        [[randint(60, 120), randint(80, 200)] for i in range(0, 100)],
        columns=['Contributors', 'Repos']
    )

    st.line_chart(chart_data)