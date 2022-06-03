import pandas as pd
from typing import List
import streamlit as st


@st.cache(suppress_st_warning=True)
def read_data_openissues(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def filter_df(df: pd.DataFrame,
    label: List[str]=None,
    day: int=0,
    nb_comments: int=0,
    author_status: List[str]=None,
    search_bar: str=''
    ) -> pd.DataFrame:
    
    return df