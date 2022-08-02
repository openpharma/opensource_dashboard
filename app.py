import streamlit as st
import utils as utl
from apps import pharmapackages, openissues, activity, leaderboard, about # import your app modules here

st.set_page_config(layout="wide", page_title='OpenPharma', page_icon=':pill:')
st.set_option('deprecation.showPyplotGlobalUse', False)

#contain both header and boostrap 5.2
utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = utl.get_current_route()
    if route == "pharmapackages":
        pharmapackages.page_content()
    elif route == "openissues":
        openissues.page_content()
    elif route == "activity":
        activity.page_content()
    elif route == "leaderboard":
        leaderboard.page_content()
    elif route == "about":
        about.page_content()
    elif route == None:
        pharmapackages.page_content()
        
navigation()