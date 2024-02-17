import openai
import os
import streamlit as st

st.title("ChatGPT-like clone")

        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
