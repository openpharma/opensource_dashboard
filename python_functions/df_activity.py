import streamlit as st
import pandas as pd
from typing import List


@st.cache(suppress_st_warning=True)
def read_repos_clean(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df