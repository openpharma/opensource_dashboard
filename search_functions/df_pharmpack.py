import pandas as pd
from typing import List
import streamlit as st

@st.cache(suppress_st_warning=True)
def read_data_repos(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df['description'] = df['cran_description']
    df['title'] = df['cran_title']
    df.loc[df['title'].isnull(), 'title'] = df['gh_description']
    df.loc[df['description'].isnull(), 'description'] = df['gh_description']
    df = df.dropna(subset=['title']).reset_index(drop=True)
    df['Contributors'] = df['Contributors'].fillna(0)
    df['riskmetric_score_quintile'] = df['riskmetric_score_quintile'].fillna(0)
    df['os_health'] = df['os_health'].fillna(0)
    df['gh_language'] = df['gh_language'].fillna('R')
    df['gh_language'] = df['gh_language'].apply(lambda x: 'R' if x in ['HTML', 'Jupyter Notebook', 'Unsure', 'Rich Text Format'] else x)
    df['risk_column'] = 20*df['riskmetric_score_quintile']+df['os_health']
    return df

def filter_df(
    df: pd.DataFrame,
    categories: List[str]=None,
    nb_contribs: int=0,
    language: str='All',
    risk_metrics: int=0,
    license: str='All',
    search_bar: str=''
    ) -> pd.DataFrame:
    df = df[(df['type'].isin(categories)) & (df['Contributors'] >= nb_contribs) & (df['risk_column'] >= risk_metrics)]
    """
    Need cleaning!

    if(license != 'All'):
        df = df[df['cran_license']]"""

    if(language != 'All'):
        df = df[df['gh_language'] == language]
    return df.reset_index(drop=True)

