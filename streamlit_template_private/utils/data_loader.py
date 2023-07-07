import streamlit as st
import os
import pandas as pd

@st.cache_data
def get_gics():
    path = os.path.join(st.session_state['root_path'], 'data', 'gics.csv')
    df = pd.read_csv(path)
    return df
