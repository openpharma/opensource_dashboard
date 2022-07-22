import streamlit as st
import pandas as pd

def page_content():
    with open('style/about.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.header("About Pharmaverse")