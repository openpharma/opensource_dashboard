import pandas as pd
from typing import List
import streamlit as st

@st.cache(suppress_st_warning=True)
def read_data_leaderboard(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def filter_df(df: pd.DataFrame):
    try:
        columns = ['avatar','author','Best_author', 'Best_replier','P_comments', 'P_reactions', 'FC_reactions', 'C_reactions', 'commits', 'contributed_to']
        df = df.sort_values(by='Best_author', ascending=False)[columns].reset_index(drop=True)
        df=df[columns]
        df = df.rename(columns={'author': 'Username','Best_author': 'Best author on issues', 'Best_replier': 'Best replier on issues','P_comments': '#comments on my issues','P_reactions': '#reactions on my issues', 'FC_reactions': 'First comment','C_reactions': '#reactions on my comments', 'commits': '#commits', 'contributed_to': 'List repos'})
    except:
        pass
    return df
        
def path_to_image_html(path):
    return '<img src="'+ path + '" width="30"/>'


def display_data_categories(df: pd.DataFrame)-> List[str]:
    l_data = []
    l_icon_metric = ["&#x1F468;&#x200D;&#x1F4BB;", "&#x1F450", "&#x1F9BE"]
    l_title_metric = ["Best coder", "Best altruist", "Best self maintainer"]
    df_coder = df.sort_values(by="coder_metric", ascending=False)[:3].reset_index(drop=True)[["author", "avatar", "commits", "contributed_to"]]
    df_altruist = df.sort_values(by="altruist_metric", ascending=False)[:3].reset_index(drop=True)[["author", "avatar", "#comments_altruist", "#reactions_altruist", "#first_comments_altruist"]]
    df_maintainer = df.sort_values(by="self_maintainer_metric", ascending=False)[:3].reset_index(drop=True)[["author", "avatar", "#comments_self_maintainer", "#reactions_self_maintainer", "#first_comments_self_maintainer"]]
    coder_dict = {
        "image": df_coder["avatar"].tolist(),
        "author": df_coder["author"].tolist(),
        "text": ["{} commits | Contributions in {} projects".format(df_coder["commits"][i], df_coder["contributed_to"][i].astype(int)) for i in range(0,3)]
    }
    altruist_dict = {
        "image": df_altruist["avatar"].tolist(),
        "author": df_altruist["author"].tolist(),
        "text": ["{} comments | {} first replies | {} reactions".format(df_altruist["#comments_altruist"][i].astype(int), df_altruist["#first_comments_altruist"][i].astype(int), df_altruist["#reactions_altruist"][i].astype(int)) for i in range(0,3)]
    }
    maintainer_dict = {
        "image": df_maintainer["avatar"].tolist(),
        "author": df_maintainer["author"].tolist(),
        "text": ["{} comments | {} first replies | {} reactions".format(df_maintainer["#comments_self_maintainer"][i].astype(int), df_maintainer["#first_comments_self_maintainer"][i].astype(int), df_maintainer["#reactions_self_maintainer"][i].astype(int)) for i in range(0,3)]
    }
    l_users = [coder_dict, altruist_dict, maintainer_dict]
    l_metrics_info = ["The 'Best coder' metric rewards the most active developers on R packages (related to the pharmaceutical industry). The metric takes into account the number of involvement in R packages development and the number of commits.", "The altruistic metric rewards people who help other developers through github isssues. The metric takes into account the first response to a github post, the number of comments on a post and the number of reactions on it.", "The self pillar metric rewards people who are active on github issues of their own projects. The metric takes into account the first response to a github post, the number of comments on a post and the number of reactions on it."]
    for i in range(0,3):
        components = rf"""
            <div class="row row_card">
                <div class="sidebar col_left_icon d-inline">
                    <p class="icon_metric">{l_icon_metric[i]}</p>
                    <h2 class="h2_remove_hover">{l_title_metric[i]}</h2>
                    <dfn data-info="{l_metrics_info[i]}">&#x24D8</dfn>
                </div>
                <div class="col col_rank d-flex aligns-items-center">
                    <table class="table table_top3">
                    <tbody>
                        <tr class="border_tr_rank">
                        <td class="rank_number" style="width: 40px; color: #FED00E;">
                            #1
                        </td>
                        <td style="width: 40px;"><img src="{l_users[i]["image"][0]}" alt="" width="40" /></td>
                        <td>
                            <span class="name_ranking">{l_users[i]["author"][0]}</span>
                            <a href="https://github.com/{l_users[i]["author"][0]}" style="color: black" target="_blank">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-github ml-2" viewBox="0 0 16 16">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                        </svg></a>
                        <br /><span class="details_val_metric">{l_users[i]["text"][0]}</span>
                        </td>
                        </tr>
                        <tr class="border_tr_rank">
                        <td class="rank_number" style="color: #A2A2A2;">
                            #2
                        </td>
                        <td><img src="{l_users[i]["image"][1]}" alt="" width="40" /></td>
                        <td>
                            <span class="name_ranking">{l_users[i]["author"][1]}</span>
                            <a href="https://github.com/{l_users[i]["author"][1]}" style="color: black" target="_blank">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-github ml-2" viewBox="0 0 16 16">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                        </svg></a>
                        <br /><span class="details_val_metric">{l_users[i]["text"][1]}</span>
                        </td>
                        </tr>
                        <tr>
                        <td class="rank_number" style="color: #B7662A;">
                            #3
                        </td>
                        <td><img src="{l_users[i]["image"][2]}" alt="" width="40" /></td>
                        <td>
                            <span class="name_ranking">{l_users[i]["author"][2]}</span>
                            <a href="https://github.com/{l_users[i]["author"][2]}" style="color: black" target="_blank">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-github ml-2" viewBox="0 0 16 16">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                        </svg></a>
                        <br /><span class="details_val_metric">{l_users[i]["text"][2]}</span>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </div>
            </div>"""
        l_data.append(components)
    return l_data


def display_data_overall(df: pd.DataFrame)-> str:
    cell_components = rf""""""
    df_overall = df.sort_values(by="overall_metric", ascending=False)[:20].reset_index(drop=True)[["author", "avatar", "coder_metric", "self_maintainer_metric", "altruist_metric", "overall_metric"]]
    for i in range(len(df_overall)): 
        cell_components += rf"""<tr>
            <td style="width: 40px;"><img src="{df_overall["avatar"][i]}" alt="" width="30" /></td>
            <td><span class="pseudo">{df_overall["author"][i]}</span></td>
            <td class="number_rank">{df_overall["coder_metric"][i]}</td>
            <td class="number_rank">{df_overall["altruist_metric"][i]}</td>
            <td class="number_rank">{df_overall["self_maintainer_metric"][i]}</td>
            <td class="number_rank"><strong>{df_overall["overall_metric"][i]}</strong></td>
            </tr>
        """
    component = rf"""
        <div class="row row_global_lead">
            <div class="col col_rank d-flex aligns-items-center">
            <table class="table table_global_lead">
                <thead>
                    <tr>
                        <th scope="col">Pseudo</th>
                        <th scope="col"></th>
                        <th scope="col">Coder Score</th>
                        <th scope="col">Altruist Score</th>
                        <th scope="col">Self maintainer Score</th>
                        <th scope="col">Overall Score</th>
                    </tr>
                </thead>
                <tbody>{cell_components}</tbody>
            </table>
            </div>
        </div>"""
    return component
