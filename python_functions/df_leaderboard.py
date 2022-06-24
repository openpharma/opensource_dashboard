import pandas as pd
from typing import List
import streamlit as st

@st.cache(suppress_st_warning=True)
def read_data_leaderboard(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def filter_df(df: pd.DataFrame):
    try:
        columns = ['avatar','author','Best_author', 'Best_replier','P_comments', 'P_reactions', 'FC_reactions', 'C_reactions', 'commits', 'contributed_to']
        #df = df.sort_values(by='Best_author', ascending=False)[columns].reset_index(drop=True)
        df = df.rename(columns={'author': 'Username','Best_author': 'Best author on issues', 'Best_replier': 'Best replier on issues','P_comments': '#comments on my issues','P_reactions': '#reactions on my issues', 'FC_reactions': 'First comment','C_reactions': '#reactions on my comments', 'commits': '#commits', 'contributed_to': 'List repos'})
    except:
        pass
    return df
        
def path_to_image_html(path):
    return '<img src="'+ path + '" width="30"/>'