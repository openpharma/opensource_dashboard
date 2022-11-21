from typing import List
import markdown
import pandas as pd
import streamlit as st
from python_functions import search_engine

PATH_PHARMAVERSE = "http://openpharma.s3-website.us-east-2.amazonaws.com/pharmaverse_packages.csv"
PATH_CATEGORY = "http://openpharma.s3-website.us-east-2.amazonaws.com/ml/repos_categorization.csv"


@st.cache(suppress_st_warning=True, ttl=14400)
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
    df = df.iloc[:nb_cards]
    df_cg = read_df(PATH_CATEGORY)
    df = df.merge(df_cg, how="left", on="full_name")
    pack_name = df['full_name'].tolist()
    pack_icon = df['icon_package'].tolist()
    issue_day = df['days_no_activity'].tolist()
    issue_author = df['author'].tolist()
    issue_author_status = df['author_status'].tolist()
    issue_title = df['title'].tolist()
    issue_label = df['label'].tolist()
    issue_comments = df['comments'].tolist()
    issue_body = df['body'].tolist()
    issue_url = df['url'].tolist()
    df['plots'] = df['plots'].apply(lambda x: ", plots" if x == True else "")
    df['tables'] = df['tables'].apply(lambda x: ", tables" if x == True else "")
    df['stats'] = df['stats'].apply(lambda x: ", stats" if x == True else "")
    df['cdisc'] = df['cdisc'].apply(lambda x: ", CDISC" if x == True else "")
    df['utilities'] = df['utilities'].apply(lambda x: ", utilities" if x == True else "")
    issue_cg = [x1+x2+x3+x4+x5 for x1, x2, x3, x4, x5 in zip(df.plots, df.tables, df.stats, df.cdisc, df.utilities)]
    issue_cg = [x[2:] if len(x) >= 2 else x for x in issue_cg]
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
                                    <p class="author_status h2_remove_hover"><u>Last active :</u> {issue_day[i]} d | <u>Author</u> : {issue_author[i]} - {issue_author_status[i]} | <a href="{issue_url[i]}" style="color: black" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" fill="currentColor" class="bi bi-github ml-2" viewBox="0 0 20 20">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                        </svg></a></p>
                                    <div class="title_tag_issue align-items-center d-inline-flex">
                                        <p class="h2_remove_hover title_open_issue"><a href="{issue_url[i]}">{issue_title[i]}</a></p>
                                        <p class="pill_tag"><span class="badge rounded-pill text-bg-primary">{issue_label[i]}</span></p>
                                    </div>
                                    <div class="list_metrics">
                                        <div class="pills d-inline-flex">
                                            <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4ac.png" alt="" height=13>
                                            <p>{issue_comments[i]}</p>
                                        </div>
                                        <div class="pills d-inline-flex">
                                            <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f511.png" alt="" height=13>
                                            <p>{issue_cg[i]}</p>
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