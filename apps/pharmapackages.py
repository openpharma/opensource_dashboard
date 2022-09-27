import streamlit as st
from python_functions import df_pharmpack

def page_content():
    """Read and display data"""

    PATH = "http://openpharma.s3-website.us-east-2.amazonaws.com/repos_clean.csv"
    df = df_pharmpack.read_df(PATH)

    with open('style/pharmapackages.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    #Side bar Filter

    with st.sidebar:
        st.title(":hammer_and_pick: Filter")
        
        st.header("Only pharmaverse packages")
        agree_pharmaverse = st.checkbox('Yes')

        st.header("Categories")
        categories_topics = st.multiselect(
            label='Select categories',
            options=['Plots', 'Tables', 'Stats', 'CDISC', 'Utilities']
        )

        st.header("Number of contributors")
        nb_contribs = st.slider(
            label="Choose a range of values",
            min_value=0, 
            max_value=180, 
            value=(0, 180)
        )
        st.header("Language")
        prog_language = st.radio(
            label="Choose the language",
            options=('All', 'R', 'Python'),
            index=0
        )
        st.header("OS health")
        os_health = st.slider(
            label="0 = Low health ; 100 = High health",
            min_value=0,
            max_value=100, 
            value=(0, 100)
        )

        st.header("Risk metric")
        risk_metric = st.slider(
            label="0 = Low risk ; 100 = High risk",
            min_value=0,
            max_value=100, 
            value=(0, 100)
        )

        st.header("License")
        license_law = st.radio(
            label="Choose the License",
            options=('All', 'GPL', 'GPL-2', 'GPL-3', 'MIT', 'LGPL 2 or 3', 'Apache License', 'Other Licenses'),
            index=0
        )

    st.header(":mag: Search")
    search_bar = st.text_input(
        '',
        placeholder='Search across more than 400 R/Python pharma packages for your data formatting, analysis and plots'
    )
    
    #HTML CARDS

    df_clean = df_pharmpack.filter_df(df=df,
        categories = categories_topics,
        nb_contribs = nb_contribs,
        language = prog_language,
        risk_metrics = risk_metric,
        os_health = os_health,
        license = license_law,
        search_bar = search_bar,
        pharmaverse = agree_pharmaverse
    )
    #st.dataframe(df_clean)

    col1, col2 = st.columns([1,1])
    
    l_components = df_pharmpack.display_data(df_clean)

    if len(l_components) >= 1:
        with col1:
            for i in range(0, len(l_components), 2):
                st.markdown(l_components[i], unsafe_allow_html=True)

        with col2:
            for i in range(1, len(l_components), 2):
                st.markdown(l_components[i], unsafe_allow_html=True)
    else:
        st.markdown("We don't have a package matching your request")


    
    
