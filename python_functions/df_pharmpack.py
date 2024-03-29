import re
from typing import List
import pandas as pd
import streamlit as st
from python_functions import search_engine


PATH_PHARMAVERSE = "http://openpharma.s3-website.us-east-2.amazonaws.com/pharmaverse_packages.csv"
PATH_CATEGORY = "http://openpharma.s3-website.us-east-2.amazonaws.com/ml/repos_categorization.csv"

@st.cache(suppress_st_warning=True, ttl=14400)
def read_df(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def clean_html(raw_html: str):
    CLEANR = re.compile('<.*?>') 
    cleantext = re.sub(CLEANR, '', raw_html)
    cleantext = re.sub("\n", ' ', cleantext)
    return cleantext

def filter_df(
    df: pd.DataFrame,
    categories: List[str]=None,
    nb_contribs: tuple=(0,200),
    language: str='All',
    risk_metrics: int=0,
    os_health: int=0,
    license: str='All',
    search_bar: str='',
    pharmaverse: bool=False
    ) -> pd.DataFrame:

    # BERT Model
    if search_bar != "":
        embed_corpus = search_engine.read_copy_tensor_packages()
        result_index = search_engine.SearchEngine(embed_corpus).fit(search_bar).predict(20)
        df = df.reindex(result_index[1].tolist())
    # General filter
    df = df[(df['Contributors'] >= nb_contribs[0]) & (df['Contributors'] <= nb_contribs[1]) & (df['riskmetric_score'] >= risk_metrics[0]) & (df['riskmetric_score'] <= risk_metrics[1]) & (df['os_health'] >= os_health[0]) & (df['os_health'] <= os_health[1])]

    #Categories filter
    if len(categories) >= 1:
        df_cg = read_df(path=PATH_CATEGORY)
        df = df.merge(df_cg, on="full_name", how="left")
        categories = [x.lower() for x in categories]
        for x in categories:
            df = df[df[x] == True]

    
    # Filter on pharmaverse packages only
    if pharmaverse:
        df_pharmaverse = read_df(PATH_PHARMAVERSE)
        l_pharmaverse = df_pharmaverse['full_name'].to_list()
        df = df[df['full_name'].isin(l_pharmaverse)]

    # Filter on license 
    if license != 'All':
        df = df[df['license_clean'] == license]
    if language != 'All':
        df = df[df['lang'] == language.lower()]

    if search_bar == '':
        df = df.sort_values(by="Contributors", ascending=False)

    return df.reset_index(drop=True)




def display_data(df: pd.DataFrame) -> List[str]:
    l_data = []
    if len(df) >= 20:
        nb_cards = 20
    else:
        nb_cards = len(df)
    df = df.iloc[:nb_cards]
    df = df.astype({'last_commit_d': "Int64"})
    pack_img = df['icon_package'].tolist()
    lang_img = df['icon_package_link'].tolist()
    list_full_name = df['full_name'].tolist()
    link_github = ["https://github.com/"+x for x in list_full_name]
    pack_name = df['repo'].tolist()
    link_cran = ["https://cran.r-project.org/web/packages/"+x+"/index.html" for x in pack_name]
    link_oss_insight = ["https://ossinsight.io/analyze/"+x for x in list_full_name]
    descri = [clean_html(x) for x in df['description'].tolist()]
    org = df['org'].tolist()
    contrib = df['Contributors'].tolist()
    last_commit = df['last_commit_d'].tolist()
    oshealth_metric = df['os_health'].tolist()
    risk_color = ['bg-success' if (x >=  53) else 'bg-warning' if (x >= 21) else 'bg-danger' for x in oshealth_metric]
    risk_width_color = ["auto" if (x >=  53) else "15px" if (x >= 21) else "15px" for x in oshealth_metric]
    if len(pack_name) >= 1:
        for i in range(0, len(pack_name)):
            components = rf"""
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="card">
                            <div class="card-body pb-0">
                                <div class="row row_1">
                                <div class="col icon_package_card">
                                    <img src="{pack_img[i]}" alt="" class="m-2" width=65 />
                                </div>
                                <div class="col text-left">
                                    <h2 class="d-inline-block h2_remove_hover">{pack_name[i]}</h2>
                                    <div class="d-inline-block icon_proj">
                                    <a href="{link_github[i]}" style="color: black" target="_blank">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-github ml-2" viewBox="0 0 16 16">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                        </svg></a>
                                    <a href="{link_cran[i]}" style="color: white" target="_blank">
                                        <img src="{lang_img[i]}" width="17" height="17" class="ml-2" alt="" />
                                    </a>
                                    <div class="pills d-inline-flex pills_oss_insight">
                                        <dfn data-info="Click to get more insight in OSSinsight">
                                            <a href="{link_oss_insight[i]}" style="color: white" target="_blank">
                                            &#128202;
                                            </a>
                                        </dfn>
                                    </div>
                                    </div>
                                    <div class="proj_description">
                                    <p class="mt-3">
                                        {descri[i]}
                                    </p>
                                    </div>
                                </div>
                                </div>
                                <div class="row row_2 border-top pb-0">
                                <div class="col-xl-3 col-md-4 col-4 text-center align-top">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-building" viewBox="0 0 15 15">
  <path fill-rule="evenodd" d="M14.763.075A.5.5 0 0 1 15 .5v15a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5V14h-1v1.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V10a.5.5 0 0 1 .342-.474L6 7.64V4.5a.5.5 0 0 1 .276-.447l8-4a.5.5 0 0 1 .487.022zM6 8.694 1 10.36V15h5V8.694zM7 15h2v-1.5a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 .5.5V15h2V1.309l-7 3.5V15z"/>
  <path d="M2 11h1v1H2v-1zm2 0h1v1H4v-1zm-2 2h1v1H2v-1zm2 0h1v1H4v-1zm4-4h1v1H8V9zm2 0h1v1h-1V9zm-2 2h1v1H8v-1zm2 0h1v1h-1v-1zm2-2h1v1h-1V9zm0 2h1v1h-1v-1zM8 7h1v1H8V7zm2 0h1v1h-1V7zm2 0h1v1h-1V7zM8 5h1v1H8V5zm2 0h1v1h-1V5zm2 0h1v1h-1V5zm0-2h1v1h-1V3z"/>
</svg>
                                    <p class="mt-2">
                                    {org[i]}
                                    </p>
                                </div>
                                <div class="col-xl-3 col-lg-4 col-4 text-center align-top">
                                    <h2 class="h2_remove_hover">{contrib[i]}</h2>
                                    <p>Contributors</p>
                                </div>
                                <div class="col-xl-3 text-center align-top d-none d-xl-inline">
                                    <h2 class="h2_remove_hover">{last_commit[i]} d</h2>
                                    <p class="p-0">Since last<br /> commit</p>
                                </div>
                                <div class="col-xl-3 col-lg-4 col-4 text-center align-top reliability_info">
                                    <p><dfn data-info="The OS Activity score is based on openpharma.github.io/os-health.html">Os-Activity &#x24D8;</dfn></p>
                                        <div class="progress">
                                            <div class="metrics_confidence progress-bar-striped progress-bar-animated {risk_color[i]}" style="width: {int(oshealth_metric[i])}%" role="progressbar" aria-valuenow="{oshealth_metric[i]}" aria-valuemin="0" aria-valuemax="100">
                                            <p style="width: {risk_width_color[i]};">{int(oshealth_metric[i])}</p>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>"""
            l_data.append(components)
    return l_data
