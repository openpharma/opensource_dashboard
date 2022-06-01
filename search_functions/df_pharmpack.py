import pandas as pd
from typing import List
import streamlit as st

def clean_license(x):
    if ('GPL' in x) and ('3' in x):
        return 'GPL-3'
    elif ('GPL' in x) and ('2' in x):
        return 'GPL-2'
    elif 'GPL' in x:
        return 'GPL-1'
    elif 'MIT' in x:
        return 'MIT'
    elif 'LGPL' in x:
        return 'LGPL 2 or 3'
    elif 'Apache License' in x:
        return 'Apache License'
    else:
        return 'Other Licenses'

@st.cache(suppress_st_warning=True)
def read_data_repos(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df['description'] = df['cran_description']
    df['title'] = df['cran_title']
    df.loc[df['title'].isnull(), 'title'] = df['gh_description']
    df.loc[df['description'].isnull(), 'description'] = df['gh_description']
    df = df.dropna(subset=['title']).reset_index(drop=True)
    df['Contributors'] = df['Contributors'].fillna(0)
    df['Contributors'] = df['Contributors'].apply(lambda x: int(x))
    df['riskmetric_score_quintile'] = df['riskmetric_score_quintile'].fillna(0)
    df['os_health'] = df['os_health'].fillna(0)
    df['lang'] = df['lang'].fillna('R')
    df['cran_license'] = df['cran_license'].fillna('Other Licenses')
    df['license_clean'] = df['cran_license'].apply(clean_license)
    df['risk_column'] = 20*df['riskmetric_score_quintile']+df['os_health']
    df['last_commit_d'] = (pd.to_datetime("today") - pd.to_datetime(df['Last Commit'])).dt.days.astype('Int64')
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

    return df.reset_index(drop=True)

def fillin_cards(df: pd.DataFrame) -> List[str]:
    l_data = []
    nb_cards = 10
    pack_name = df['repo'][:nb_cards].tolist()
    cran_descri = df['description'][:nb_cards].tolist()
    org = df['org'][:nb_cards].tolist()
    contrib = df['Contributors'][:nb_cards].tolist()
    last_commit = df['last_commit_d'][:nb_cards].tolist()
    if (len(pack_name)>=1):
        for i in range(0, len(pack_name)):
            components = rf'''
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="card">
                            <div class="card-body pb-0">
                                <div class="row row_1">
                                <div class="col icon_package_card">
                                    <img src="https://avatars.githubusercontent.com/u/8436743?s=200&v=4" alt="" class="m-2" height=80 width=80 />
                                </div>
                                <div class="col text-left">
                                    <h2 class="d-inline-block">{pack_name[i]}</h2>
                                    <div class="d-inline-block icon_proj">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-github ml-2" viewBox="0 0 16 16">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                        </svg>
                                    <img src="https://cran.r-project.org/Rlogo.svg" width="22" height="22" class="ml-2" alt="" />
                                    </div>
                                    <div class="proj_description">
                                    <p class="mt-3">
                                        {cran_descri[i]}
                                    </p>
                                    </div>
                                </div>
                                </div>
                                <div class="row row_2 border-top pb-0">
                                <div class="col-xl-3 text-center align-top">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-person" viewBox="0 0 15 15">
                        <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
                        </svg>
                                    <p class="mt-2">
                                    {org[i]}
                                    </p>
                                </div>
                                <div class="col-xl-3 text-center align-top">
                                    <h2>+{contrib[i]}</h2>
                                    <p>Contributors</p>
                                </div>
                                <div class="col-xl-3 text-center align-top">
                                    <h2>{last_commit[i]} d</h2>
                                    <p class="p-0">Since last<br /> commit</p>
                                </div>
                                <div class="col-xl-3 text-center align-top">
                                    <p>Reliability</p>
                                    <div class="metrics_confidence"></div>
                                    <div class="metrics_confidence"></div>
                                    <div class="metrics_confidence"></div>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>'''
            l_data.append(components)
    return l_data

