"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from streamlit_option_menu import option_menu

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.app_title = []
        self.app_function = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.app_title.append(title)
        self.app_function.append(func)

    def run(self):
        # app = st.sidebar.radio(
        my_app = option_menu(
            menu_title="",
            options=self.app_title,
            orientation="horizontal",
            icons=["boxes", "exclamation-circle", "award"],
            styles={
                "container": {"background-color": "#002171", "border-radius": "0px"},
                "icon": {"color": "white", "font-size": "25px"},
                "nav-link": {"color":"white", "padding": "25px", "font-size": "1em"},
                "nav-link-selected": {"background-color": "#113CA1"},
            }
        )

        if my_app == self.app_title[0]:
            self.app_function[0]()
        elif my_app == self.app_title[1]:
            self.app_function[1]()
        elif my_app == self.app_title[2]:
            self.app_function[2]()