from cProfile import label
from logging import PlaceHolder
import streamlit as st

def page_content():
    with open('style/pharmapackages.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with st.sidebar:
        st.title(":hammer_and_pick: Filter")
        
        st.header("Categories")
        categories_topics = st.multiselect(
            label='Select Multiple categories',
            options=['TLG', 'CTV', 'Clinical Statistics', 'Filings tools', 'Omics'],
            default=['TLG', 'CTV', 'Clinical Statistics', 'Filings tools', 'Omics']
        )

        st.header("Min # of contributions")
        min_nb_contrib = st.slider(
            label="Choose a value",
            min_value=0, 
            max_value=200, 
            value=0
        )
        st.header("Language")
        prog_language = st.radio(
            label="Choose the language",
            options=('All', 'R', 'Python', 'C++'),
            index=0
        )
        st.header("Risk Metrics")
        risk_metric = st.slider(
            label="0 = Low maintainability ; 100 = High maintainability",
            min_value=0,
            max_value=100, 
            value=50
        )

        st.header("License")
        license_law = st.radio(
            label="Choose the License",
            options=('All', 'GPT', 'MIT', 'Apache'),
            index=0
        )

    st.header(":mag: Search")
    search_bar = st.text_input(
        '',
        placeholder='Search a package...'
    )

    col1, col2 = st.columns([1,1])


    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    st.title('Rpackages')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")