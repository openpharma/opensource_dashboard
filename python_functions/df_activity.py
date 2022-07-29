import streamlit as st
import pandas as pd
from typing import Tuple
import numpy as np
from datetime import datetime, timedelta


@st.cache(allow_output_mutation=True)
def read_repos(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

@st.cache(allow_output_mutation=True)
def read_commits(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def repo_contrib_activity(df: pd.DataFrame, type:str)-> Tuple[int, float]:
    df['date'] = pd.to_datetime(df['date'])
    today_1m = np.datetime64(datetime.today() - timedelta(days=30))
    today_2m = np.datetime64(datetime.today() - timedelta(days=60))
    active_repo = df[df['date'] > today_1m][type].nunique()
    active_repo_pred = df[(df['date'] < today_1m) & (df['date'] > today_2m)][type].nunique()
    evol = int(100*(active_repo-active_repo_pred)/active_repo_pred)
    return active_repo, evol