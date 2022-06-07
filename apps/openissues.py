import streamlit as st
from python_functions import df_openissues
import pandas as pd

def page_content():

    PATH = 'http://openpharma.s3-website.us-east-2.amazonaws.com/help.csv'
    df = df_openissues.read_data_openissues(PATH)


    with open('style/openissues.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with st.sidebar:
        st.title(":hammer_and_pick: Filter")
        
        st.header("Label")
        label_openissues = st.multiselect(
            label='Select Multiple categories',
            options=['good first issue', 'help wanted', 'discussion', 'good first issue, help wanted', 'bug'],
            default=['good first issue', 'help wanted', 'discussion', 'good first issue, help wanted', 'bug']
        )

        st.header("Days since inactivity")
        days_openissues = st.slider(
            label="Choose a value",
            min_value=0, 
            max_value=100, 
            value=0
        )
        
        st.header("Min # of comments")
        nb_comments = st.slider(
            label="Choose a value ",
            min_value=0, 
            max_value=10,
            value=0
        )

        st.header("Author status")
        label_creator = st.multiselect(
            label='Select creator type',
            options=['MEMBER', 'NONE', 'COLLABORATOR'],
            default=['MEMBER', 'NONE', 'COLLABORATOR']
        )

    st.header(":mag: Search")
    search_bar = st.text_input(
        '',
        placeholder='Search a package...'
    )


    df_issue = df_openissues.filter_df(df, label_openissues, days_openissues, nb_comments, label_creator, search_bar)

    st.dataframe(df_issue)
    
    
