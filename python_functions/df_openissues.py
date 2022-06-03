import pandas as pd
from typing import List
import streamlit as st


@st.cache(suppress_st_warning=True)
def read_data_openissues(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def filter_df(df: pd.DataFrame,
    label: List[str]=None,
    day_no_activity: int=0,
    nb_comments: int=0,
    author_status: List[str]=None,
    search_bar: str=''
    ) -> pd.DataFrame:

    df = df[(df['label'].isin(label)) & (df['days_no_activity'] >= day_no_activity) & (df['comments'] >= nb_comments) & (df['author_status'].isin(author_status))]

    list_search = search_bar.lower().split()
    rstr = '|'.join(list_search)
    df = df[df['title'].str.lower().str.contains(rstr) | df['description'].str.lower().str.contains(rstr)]
    return df