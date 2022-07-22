import streamlit as st
import pandas as pd
from random import randint

def page_content():
    with open('style/activity.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.title("!Not real Data!")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("#Repos", "286")
    col2.metric("Active repos", "112", "+3%")
    col3.metric("Active contributors", "256", "-2%")
    col4.metric("Docs Ratio", "86%")
    
    st.header("Cumulative trend of #contributors and #repos")
    chart_data = pd.DataFrame(
        [[randint(60, 120), randint(80, 200)] for i in range(0, 100)],
        columns=['Contributors', 'Repos']
    )

    st.line_chart(chart_data)