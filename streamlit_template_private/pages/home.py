import streamlit as st

def app():

    # Configure page
    page = 'home'
    st.title(f'{st.session_state.app.pages[page].icon} {st.session_state.app.pages[page].title}')
    st.header("Welcome to Streamlit! 👋")

    # Using the data loader
    from ..utils import data_loader
    gics_df = data_loader.get_gics()

    # Your code goes here!
    # Or add a new page!