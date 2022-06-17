import pandas as pd
from typing import List
import streamlit as st

@st.cache(suppress_st_warning=True)
def read_data_repos(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
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

    if(license != 'All'):
        df = df[df['license_clean'] == license]
    if(language != 'All'):
        df = df[df['lang'] == language.lower()]

    # Simple character matching
    list_search = search_bar.lower().split()
    rstr = '|'.join(list_search)
    df = df[df['title'].str.lower().str.contains(rstr) | df['description'].str.lower().str.contains(rstr)]

    return df.reset_index(drop=True)

def display_data(df: pd.DataFrame) -> List[str]:
    l_data = []
    nb_cards = 20
    pack_img = df['icon_package'][:nb_cards].tolist()
    pack_name = df['repo'][:nb_cards].tolist()
    descri = df['description'][:nb_cards].tolist()
    org = df['org'][:nb_cards].tolist()
    contrib = df['Contributors'][:nb_cards].tolist()
    last_commit = df['last_commit_d'][:nb_cards].tolist()
    risk_metric = (5+df['risk_column'][:nb_cards]).tolist()
    risk_color = ['bg-success' if (x >=  53.0) else 'bg-danger' if (x <= 21.0) else 'bg-warning' for x in risk_metric]
    if (len(pack_name)>=1):
        for i in range(0, len(pack_name)):
            
            components = rf'''
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
                                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-github ml-2" viewBox="0 0 16 16">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                        </svg>
                                    <img src="https://cran.r-project.org/Rlogo.svg" width="17" height="17" class="ml-2" alt="" />
                                    </div>
                                    <div class="proj_description">
                                    <p class="mt-3">
                                        {descri[i]}
                                    </p>
                                    </div>
                                </div>
                                </div>
                                <div class="row row_2 border-top pb-0">
                                <div class="col-xl-3 text-center align-top">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-person" viewBox="0 0 15 15">
                        <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
                        </svg>
                                    <p class="mt-2">
                                    {org[i]}
                                    </p>
                                </div>
                                <div class="col-xl-3 text-center align-top">
                                    <h2 class="h2_remove_hover">+{contrib[i]}</h2>
                                    <p>Contributors</p>
                                </div>
                                <div class="col-xl-3 text-center align-top">
                                    <h2 class="h2_remove_hover">{last_commit[i]} d</h2>
                                    <p class="p-0">Since last<br /> commit</p>
                                </div>
                                <div class="col-xl-3 text-center align-top">
                                    <p>Reliability</p>
                                    <div class="progress">
                                        <div class="metrics_confidence progress-bar-striped progress-bar-animated {risk_color[i]}" style="width: {risk_metric[i]}%" role="progressbar" aria-valuenow="{risk_metric[i]}" aria-valuemin="0" aria-valuemax="100">
                                        <p>{int(risk_metric[i]-5)}</p>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>'''
            l_data.append(components)
    return l_data

