# Standard library imports
import time

# Third-Party Imports
import streamlit as st


# Importing other files for setup and functionalities
from setup_st import *
#from helper_functions import *
#from index_functions import *

# Initialize session state variables if they don't exist
#initialize_session_state()

# Setup Streamlit UI/UX elements
set_design()
sidebar()
get_user_config()
clear_button()
download_button()

st.title("GPT guru")
