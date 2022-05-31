import streamlit as st
from search_functions import df_pharmpack

def page_content():

    PATH = 'http://openpharma.s3-website.us-east-2.amazonaws.com/repos.csv'

    with open('style/pharmapackages.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    """
    
    Read Data

    """

    df = df_pharmpack.read_data_repos(PATH)

    """

    Side Bar Filter

    """
    with st.sidebar:
        st.title(":hammer_and_pick: Filter")
        
        st.header("Categories")
        categories_topics = st.multiselect(
            label='Select Multiple categories',
            options=['ctv', 'filing-tools', 'filing-tools, tlg', 'omics', 'clinical-statistics', 'tlg', 'filing-tools, gh-action', 'pkpd', 'synthetic-data'],
            default=['ctv', 'filing-tools', 'filing-tools, tlg', 'omics', 'clinical-statistics', 'tlg', 'filing-tools, gh-action', 'pkpd', 'synthetic-data']
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
            options=('All', 'R', 'Python', 'C++', 'Fortran', 'C'),
            index=0
        )
        st.header("Risk Metrics")
        risk_metric = st.slider(
            label="0 = Low maintainability ; 200 = High maintainability",
            min_value=0,
            max_value=200, 
            value=0
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

    """

    HTML Card

    """

    print(categories_topics,min_nb_contrib,prog_language,risk_metric,license_law)

    df_clean = df_pharmpack.filter_df(df,categories_topics,min_nb_contrib,prog_language,risk_metric,license_law)

    st.dataframe(df_clean)

    component = rf'''
                <div class="row">
                    <div class="col-lg-12">
                        <div class="card">
                        <div class="card-body pb-0">
                            <div class="row row_1">
                            <div class="col icon_package_card">
                                <img src="https://avatars.githubusercontent.com/u/8436743?s=200&v=4" alt="" class="m-2" height=80 width=80 />
                            </div>
                            <div class="col text-left">
                                <h2 class="d-inline-block">Package name</h2>
                                <div class="d-inline-block icon_proj">
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-github ml-2" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                                <img src="https://cran.r-project.org/Rlogo.svg" width="22" height="22" class="ml-2" alt="" />
                                </div>
                                <div class="proj_description">
                                <p class="mt-3">
                                    Reporting tables often have structure that goes beyond simple rectangular
                    data. The 'rtables' package provides a framework ....
                                </p>
                                </div>
                            </div>
                            </div>
                            <div class="row row_2 border-top pb-0">
                            <div class="col-xl-3 text-center align-top">
                                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-person" viewBox="0 0 15 15">
                    <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
                    </svg>
                                <p class="mt-2">Roche</p>
                            </div>
                            <div class="col-xl-3 text-center align-top">
                                <h2>+300</h2>
                                <p>Contributors</p>
                            </div>
                            <div class="col-xl-3 text-center align-top">
                                <h2>12 d</h2>
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
                    </div>
            '''
    col1, col2 = st.columns([1,1])


    with col1:
        st.markdown(component, unsafe_allow_html=True)

    with col2:
        st.markdown(component, unsafe_allow_html=True)
