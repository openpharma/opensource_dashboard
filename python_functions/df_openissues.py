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

def display_data(df) -> List[str]:
    l_data = []
    nb_cards = 5
    pack_name = df['full_name'][:nb_cards].tolist()
    if (len(pack_name)>=1):
        for i in range(0, 2):
            components = rf"""                    
                    <div class="row">
                        <div class="col-sm-3 align-items-center d-inline-flex package_name">
                            <img src="https://avatars.githubusercontent.com/u/8436743?s=200&v=4" alt="" height=16/>
                            <h2 class="h2_remove_hover">rTables</h2>
                        </div>
                        <div class="col-sm-9">
                            <!-- Nothing inside -->
                        </div>
                        <div class="card">
                            <div class="row">
                                <div class="open_issue_icon d-none col-sm-2 align-items-center d-md-flex justify-content-center">
                                    <div class="big_circle">
                                        <div class="small_circle">
                                        </div>
                                    </div>
                                </div>
                                <div class="col-sm-10">
                                    <h3 class="author_status h2_remove_hover"><u>Author</u> : sbrockhaus - MEMBER</h3>
                                    <div class="title_tag_issue align-items-center d-inline-flex">
                                        <h2 class="h2_remove_hover">Split up the code that calculates data for component plots</h2>
                                        <p><span class="badge rounded-pill text-bg-primary">Good first issue</span></p>
                                    </div>
                                    <div class="list_metrics">
                                        <div class="pills d-inline-flex">
                                            <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png" alt="" height=13>
                                            <p>40</p>
                                        </div>
                                        <div class="pills d-inline-flex">
                                            <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4ac.png" alt="" height=13>
                                            <p>8</p>
                                        </div>
                                        <div class="pills d-inline-flex">
                                            <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f511.png" alt="" height=13>
                                            <p>plots, components, graphics, calculation, model</p>
                                        </div>    
                                    </div>
                                </div>
                            </div>
                            <details class="display_more">
                                <summary class="btn btn-primary">></summary>
                                <div class="display_collapse">
                                    <p>Oh, hello</p>
                                    <p>Oh, hello</p>
                                    <p>Oh, hello</p>
                                    <p>Oh, hello</p>
                                    <p>Oh, hello</p>
                                    <p>Oh, hello</p>
                                </div>
                            </details>
                        </div>
                    </div>
"""
            l_data.append(components)
    return l_data