from typing import Tuple
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import streamlit as st

PATH_PHARMAVERSE = "http://openpharma.s3-website.us-east-2.amazonaws.com/pharmaverse_packages.csv"

@st.cache(allow_output_mutation=True, ttl=14400)
def read_df(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def packages_count(df : pd.DataFrame, pharmaverse: str)-> int:
    if pharmaverse == "Pharmaverse":
        df_pharmaverse = read_df(PATH_PHARMAVERSE)
        l_pharmaverse = df_pharmaverse['full_name'].to_list()
        df = df[df['full_name'].isin(l_pharmaverse)]
    length_pack = len(df)
    return length_pack


def repo_contrib_activity(df: pd.DataFrame, pharmaverse: str, type: str)-> Tuple[int, float]:
    if pharmaverse == "Pharmaverse":
        df_pharmaverse = read_df(PATH_PHARMAVERSE)
        l_pharmaverse = df_pharmaverse['full_name'].to_list()
        df = df[df['full_name'].isin(l_pharmaverse)]
    df['date'] = pd.to_datetime(df['date'])
    today_1m = np.datetime64(datetime.today() - timedelta(days=30))
    today_2m = np.datetime64(datetime.today() - timedelta(days=60))
    active_repo = df[df['date'] > today_1m][type].nunique()
    active_repo_pred = df[(df['date'] < today_1m) & (df['date'] > today_2m)][type].nunique()
    evol = int(100*(active_repo-active_repo_pred)/active_repo_pred)
    return active_repo, evol


def activity_line_chart(df: pd.DataFrame, pharmaverse: str, from_date: datetime)-> pd.DataFrame:
    if pharmaverse == "Pharmaverse":
        df_pharmaverse = read_df(PATH_PHARMAVERSE)
        l_pharmaverse = df_pharmaverse['full_name'].to_list()
        df = df[df['full_name'].isin(l_pharmaverse)]
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['date'] >= from_date]
    df_res = df.groupby(pd.Grouper(key="date",freq="M")).nunique()
    return df_res

