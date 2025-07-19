import streamlit as st
from src.langgraphagenticAI.ui.streamlit.loadui import LoadUI

def load_agentic_ai_ui():
    """
    Load the Agentic AI UI using Streamlit.
    """
    ui = LoadUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user controls. Please check the configuration.")
        return

    user_message = st.chat_input("Enter your message:")
    
