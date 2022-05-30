import streamlit as st
import utils as utl
from apps import pharmapackages, openissues, leaderboard # import your app modules here

st.set_page_config(layout="wide", page_title='Navbar sample')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.navbar_component()
utl.inject_custom_css()

def navigation():
    route = utl.get_current_route()
    if route == "pharmapackages":
        pharmapackages.page_content()
    elif route == "openissues":
        openissues.page_content()
    elif route == "leaderboard":
        leaderboard.page_content()
    elif route == None:
        pharmapackages.page_content()
        
navigation()