import streamlit as st
from python_functions import df_leaderboard

def page_content():
    """Read and display data"""

    with open('style/leaderboard.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    PATH = 'http://openpharma.s3-website.us-east-2.amazonaws.com/people_clean.csv'
    PATH_PHARMAVERSE = 'http://openpharma.s3-website.us-east-2.amazonaws.com/people_clean_pharmaverse.csv'

    st.title("Leaderboard")
    
    scope = st.selectbox(
        'Choose the scope of the leaderboard : all packages or pharmaverse packages',
        ('All packages', 'Pharmaverse')
    )
    
    if scope == "All packages":
        df_lead = df_leaderboard.read_data_leaderboard(PATH)
    if scope == "Pharmaverse":
        df_lead = df_leaderboard.read_data_leaderboard(PATH_PHARMAVERSE)

    l_components = df_leaderboard.display_data_categories(df_lead)
    l_global_leaderboard = df_leaderboard.display_data_overall(df_lead)


    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ranking by categories")
        for i in range(0, 3):
            st.markdown(l_components[i], unsafe_allow_html=True)
    with col2:
        st.subheader("Overall ranking")
        st.markdown(l_global_leaderboard, unsafe_allow_html=True)
    #st.markdown(df[:300].to_html(index=False, escape=False, formatters=dict(avatar=df_leaderboard.path_to_image_html)), unsafe_allow_html=True)
    
 