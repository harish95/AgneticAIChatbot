import streamlit as st
import os

from src.langgraphagenticAI.ui.uiconfig import UIConfig

class LoadUI:
    def __init__(self):
        self.ui_config = UIConfig()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= self.ui_config.get_page_title(), layout='wide')
        st.header(" 🤖 " + self.ui_config.get_page_title())
        
        llm_options = self.ui_config.get_llm_options()
        usecase_options = self.ui_config.get_usecase_options()
        groq_model_options = self.ui_config.get_groq_model_options()

        with st.sidebar:
            st.title("Agentic AI Settings")
            st.markdown("Configure your Agentic AI settings below:")
       
            self.user_controls["selected_llm"] = st.sidebar.selectbox("Select LLM", llm_options)
        
        
            
            if self.user_controls["selected_llm"]  == "Groq":
                self.user_controls["selected_groq_model"] = st.sidebar.selectbox("Select Groq Model", groq_model_options)
            
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("GROQ_API_KEY", type="password")
                
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to use Groq models.")
            
            ## usecase selection
            self.user_controls["selected_usecase"] = st.sidebar.selectbox("Select Use Case", usecase_options)
    
        return self.user_controls
    