import streamlit as st

PATH_IMG_OBJECTIVES = "https://openpharma.s3.us-east-2.amazonaws.com/streamlit_img/openpharma_objectives.png"
PATH_PHUSE_PRES = "https://openpharma.s3.us-east-2.amazonaws.com/Phuse/Openpharma-Phuse+Connect+EU+2022+-+Belfast.pdf"
IMG_JAMES = "https://avatars.githubusercontent.com/u/2760096?v=4"
IMG_MATHIEU = "https://avatars.githubusercontent.com/u/49449000?v=4"

def page_content():
    """Read and display data"""

    with open('style/about.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.header("About Open pharma")
    
    manifesto = rf"""
    <p style="font-size: 1.3em;">The objective of openpharma is to provide a neutral home for open source software related to pharmaceutical industry that is not tied to one company or institution.</p>
    <p id="title_main_obj">Objectives</p>
    <div class="row icon_objective_open">
            <img src="{PATH_IMG_OBJECTIVES}" style="width: 70%; margin: auto;" />
    </div>

    <p id="principles_open_pharma">This Github organization is managed under the following principals:</p>
    <ul>
        <li>openpharma allows repositories housed within it to set their own governance model</li>
        <li>openpharma is open to any project related to the Pharma industry</li>
        <li>openpharma makes no assumptions on what packages are part of an ‘ideal’ workflow</li>
        <li>a preference is always placed on opensource from day 1, but openpharma will also host packages in private repos on request</li>
        <li>at launch, Roche has admin status for the organization] openpharma will work towards a governance model that is inclusive and builds trust in those contributing to packages (e.g. use a more formalized consortia like the pharmaverse to provide governance of the Github organization)</li>
        <li>openpharma is open to collaborating with relevant organizations like PHUSE, R Consortium, PSI and the pharmaverse – but openpharma will remain an open host to share projects and provide a platform for repositories looking for a neutral host.</li>
        <li>openpharma will not hold any IP or copyright of associated projects, it will not be a platform for discussion or host initiatives, and it will not release opinions or standards on which repositories form part of an ideal workflow.</li>
    </ul>
    <p>Promoting collaboration on projects:</p>
    <ul>
        <li>openpharma will aim to build an inclusive list of collaborative projects hosted on github.com that goes beyond those physically hosted in github.com/openpharma.</li>
    </ul>
    """
    st.markdown(manifesto, unsafe_allow_html=True)

    st.subheader("Presentation : PHUSE EU Connect 2022 - Belfast")

    st.write("Link to the presentation : [Openpharma PDF]({})".format(PATH_PHUSE_PRES))

    st.subheader("Authors and maintainers :")

    st.image(IMG_MATHIEU, width=80, caption="Mathieu Cayssol")
    st.write("[Github]({})".format("https://github.com/MathieuCayssol"))

    st.image(IMG_JAMES, width=80, caption="James Black")
    st.write("[Github]({})".format("https://github.com/epijim"))
