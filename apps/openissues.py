import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode, JsCode
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

    gd = GridOptionsBuilder.from_dataframe(df_issue)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(min_column_width=5, resizable=True, filterable=True, sortable=True, editable=False, groupable=False)
    gd.configure_auto_height(autoHeight=True)
    gridoptions = gd.build()

    AgGrid(df_issue[["label", "title", "full_name", "issue_number", "comments", "author", "days_no_activity", "body"]],
        gridoptions=gridoptions,
        height=500,
        theme = "material",
        width=1000,
        allow_unsafe_jscode=True
    )

    
