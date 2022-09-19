from typing import List
import markdown
import pandas as pd
import streamlit as st
from python_functions import search_engine

PATH_PHARMAVERSE = "http://openpharma.s3-website.us-east-2.amazonaws.com/pharmaverse_packages.csv"

@st.cache(suppress_st_warning=True, ttl=43200)
def read_df(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def filter_df(df: pd.DataFrame,
    label: List[str]=None,
    day_no_activity: int=0,
    nb_comments: int=0,
    author_status: List[str]=None,
    search_bar: str='',
    pharmaverse: bool=False
    ) -> pd.DataFrame:

    if search_bar != "":
        embed_corpus = search_engine.read_copy_tensor_openissues()
        result_index = search_engine.SearchEngine(embed_corpus).fit(search_bar).predict(20)
        df = df.reindex(result_index[1].tolist())
    #Categories filter
    if len(label) >= 1:
        df = df[df['label'].isin(label)]
    
    # Filter on pharmaverse packages only
    if pharmaverse:
        df_pharmaverse = read_df(PATH_PHARMAVERSE)
        l_pharmaverse = df_pharmaverse['full_name'].to_list()
        df = df[df['full_name'].isin(l_pharmaverse)]

    df = df[(df['days_no_activity'] >= day_no_activity[0]) & (df['days_no_activity'] <= day_no_activity[1]) & (df['comments'] >= nb_comments[0]) & (df['comments'] <= nb_comments[1]) & (df['author_status'].isin(author_status))]

    return df

def display_data(df) -> List[str]:
    l_data = []
    if len(df) >= 30:
        nb_cards = 30
    else:
        nb_cards = len(df)
    pack_name = df['full_name'][:nb_cards].tolist()
    pack_icon = df['icon_package'][:nb_cards].tolist()
    issue_day = df['days_no_activity'][:nb_cards].tolist()
    issue_author = df['author'][:nb_cards].tolist()
    issue_author_status = df['author_status'][:nb_cards].tolist()
    issue_title = df['title'][:nb_cards].tolist()
    issue_label = df['label'][:nb_cards].tolist()
    issue_comments = df['comments'][:nb_cards].tolist()
    issue_body = df['body'][:nb_cards].tolist()
    
    if len(pack_name) >= 1:
        for i in range(0, len(pack_name)):
            components = rf"""        
                    <div class="row">
                        <div class="col-sm-auto align-items-center d-inline-flex package_name">
                            <div class="big_circle">
                                        <div class="small_circle">
                                        </div>
                                    </div>
                            <h2 class="h2_remove_hover">{pack_name[i]}</h2>
                        </div>
                        <div class="col-sm-auto">
                            <!-- Nothing inside -->
                        </div>
                        <div class="card">
                            <div class="row">
                                <div class="open_issue_icon d-none col-sm-2 align-items-center d-md-flex justify-content-center">
                                    <img src="{pack_icon[i]}" alt="" height="50" />
                                </div>
                                <div class="col-sm-10">
                                    <h3 class="author_status h2_remove_hover"><u>Last active :</u> {issue_day[i]} d | <u>Author</u> : {issue_author[i]} - {issue_author_status[i]}</h3>
                                    <div class="title_tag_issue align-items-center d-inline-flex">
                                        <p class="h2_remove_hover title_open_issue">{issue_title[i]}</p>
                                        <p class="pill_tag"><span class="badge rounded-pill text-bg-primary">{issue_label[i]}</span></p>
                                    </div>
                                    <div class="list_metrics">
                                        <div class="pills d-inline-flex">
                                            <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4ac.png" alt="" height=13>
                                            <p>{issue_comments[i]}</p>
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
                                <div class="display_collapse">{markdown.markdown(str(issue_body[i]), extensions=['extra'])}</div>
                            </details>
                        </div>
                    </div>"""
            l_data.append(components)
    return l_data