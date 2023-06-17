import pandas as pd
import streamlit as st
from typing import Callable
from streamlit_option_menu import option_menu
from API import API


class DownloadVoter:
    def __init__(self, get_voters: Callable[[], list]):
        st.header("Voters List")
        voters = get_voters()
        st.download_button('Download Voter List', voters)
        if st.download_button('Download Voter List', voters):
            st.write('Thanks for downloading!')
        else:
            st.write('Error in Download')
