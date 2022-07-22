import streamlit as st
import base64
from streamlit.components.v1 import html

NAVBAR_PATHS = {
    '<span class="icon_size_menu_1">&#9778;</span><span class="d-none d-md-inline">Packages</span>': 'pharmapackages',
    '<span class="icon_size_menu_2">&#x2609</span><span class="d-none d-md-inline">Open issues</span>': 'openissues',
    '<span class="icon_size_menu_3"> &#9813;</span><span class="d-none d-md-inline">LeaderBoard</span>': 'leaderboard',
    '<span class="icon_size_menu_4"> &#x24D8;</span><span class="d-none d-md-inline">About</span>': 'about'
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
                    <a class="navbar-brand" href="/" target="_blank">
                        <img src="https://avatars.githubusercontent.com/u/8436743?s=200&v=4" width="30" height="30" alt="">
                        Open Pharma
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