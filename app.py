import streamlit as st
import streamlit.components.v1 as components
from multiapp import MultiApp
from apps import pharmapackages, openissues, leaderboard # import your app modules here

app = MultiApp()
st.set_page_config(
    layout="wide"
)

with open("style/header.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Add all your application here
app.add_app("Pharma Packages", pharmapackages.page_content)
app.add_app("Open issues", openissues.page_content)
app.add_app("LeaderBoard", leaderboard.page_content)
# The main app
app.run()