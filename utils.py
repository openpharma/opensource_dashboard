import streamlit as st
import base64
from streamlit.components.v1 import html


#https://icon-sets.iconify.design/?query=growth to get icon

NAVBAR_PATHS = {
    '<svg class="icon_size_menu_1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="18" height="18" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path fill="currentColor" fill-rule="evenodd" d="M14 10V1.5l-.5-.5H3.74a1.9 1.9 0 0 0-.67.13a1.77 1.77 0 0 0-.94 1a1.7 1.7 0 0 0-.13.62v9.5a1.7 1.7 0 0 0 .13.67c.177.427.515.768.94.95a1.9 1.9 0 0 0 .67.13H4v-1h-.26a.72.72 0 0 1-.29-.06a.74.74 0 0 1-.4-.4a.93.93 0 0 1-.05-.29v-.5a.93.93 0 0 1 .05-.29a.74.74 0 0 1 .4-.4a.72.72 0 0 1 .286-.06H13v2H9v1h4.5l.5-.5V10zM4 10V2h9v8H4zm1-7h1v1H5V3zm0 2h1v1H5V5zm1 2H5v1h1V7zm.5 6.49L5.28 15H5v-3h3v3h-.28L6.5 13.49z" clip-rule="evenodd"/></svg><span class="d-none d-md-inline">Packages</span>': 'pharmapackages',
    '<svg class="icon_size_menu_2" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="18" height="18" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm0 7a3 3 0 1 0 .002 6.002A3 3 0 0 0 16 13z"/></svg><span class="d-none d-md-inline">Open issues</span>': 'openissues',
    '<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="18" height="18" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path fill="currentColor" d="M21.92 6.62a1 1 0 0 0-.54-.54A1 1 0 0 0 21 6h-5a1 1 0 0 0 0 2h2.59L13 13.59l-3.29-3.3a1 1 0 0 0-1.42 0l-6 6a1 1 0 0 0 0 1.42a1 1 0 0 0 1.42 0L9 12.41l3.29 3.3a1 1 0 0 0 1.42 0L20 9.41V12a1 1 0 0 0 2 0V7a1 1 0 0 0-.08-.38Z"/></svg><span class="d-none d-md-inline">Activity</span>': 'activity',
    '<svg class="icon_size_menu_3" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="18" height="18" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M26 7h-2V6a2.002 2.002 0 0 0-2-2H10a2.002 2.002 0 0 0-2 2v1H6a2.002 2.002 0 0 0-2 2v3a4.005 4.005 0 0 0 4 4h.322A8.169 8.169 0 0 0 15 21.934V26h-5v2h12v-2h-5v-4.069A7.966 7.966 0 0 0 23.74 16H24a4.005 4.005 0 0 0 4-4V9a2.002 2.002 0 0 0-2-2ZM8 14a2.002 2.002 0 0 1-2-2V9h2Zm14 0a6 6 0 0 1-6.186 5.997A6.2 6.2 0 0 1 10 13.707V6h12Zm4-2a2.002 2.002 0 0 1-2 2V9h2Z"/></svg><span class="d-none d-md-inline">LeaderBoard</span>': 'leaderboard',
    '<svg class="icon_size_menu_4" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="16" height="16" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><g fill="currentColor"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="m8.93 6.588l-2.29.287l-.082.38l.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319c.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246c-.275 0-.375-.193-.304-.533L8.93 6.588zM9 4.5a1 1 0 1 1-2 0a1 1 0 0 1 2 0z"/></g></svg><span class="d-none d-md-inline">About</span>': 'about'
}


def inject_custom_css():
    with open('style/header.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def get_current_route():
    try:
        return st.experimental_get_query_params()['nav'][0]
    except:
        return None


def navbar_component():
    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<li><a class="navitem" id="{value}" href="/?nav={value}">{key}</a></li>')
    component = rf'''
                <nav class="navbar">
                    <a class="navbar-brand">
                        <img src="https://openpharma.s3.us-east-2.amazonaws.com/streamlit_img/logo.png" width="45" alt="">
                        <span class="d-none d-md-inline">Open Pharma</span>
                    </a>
                    <ul class="navbar-nav">
                        {navbar_items}
                    </ul>
                </nav>
            '''
    st.markdown(component, unsafe_allow_html=True)
    js = '''
    <script>
        // navbar elements
        var navigationTabs = window.parent.document.getElementsByClassName("navitem");
        var cleanNavbar = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }
        
        for (var i = 0; i < navigationTabs.length; i++) {
            cleanNavbar(navigationTabs[i]);
        }
    </script>
    '''
    html(js, height=0)