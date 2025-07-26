import streamlit as st
import os

from src.langgraphagenticAI.ui.uiconfig import UIConfig

class LoadUI:
    def __init__(self):
        self.ui_config = UIConfig()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.ui_config.get_page_title(), layout='wide')
        st.header(" 🤖 " + self.ui_config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        
        llm_options = self.ui_config.get_llm_options()
        usecase_options = self.ui_config.get_usecase_options()
        groq_model_options = self.ui_config.get_groq_model_options()

        with st.sidebar:
            st.title("Agentic AI Settings")
            st.markdown("Configure your Agentic AI settings below:")
       
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            
            if self.user_controls["selected_llm"] == "Groq":
                self.user_controls["selected_groq_model"] = st.selectbox("Select Groq Model", groq_model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("GROQ_API_KEY", type="password")
                
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to use Groq models.")
            
            ## usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Web" or self.user_controls["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY_API_KEY", type="password")
                
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY API key to use the Chatbot with Web use case.")
            
            if self.user_controls["selected_usecase"] == "AI News":
                st.markdown("### AI News")  # Removed st.sidebar prefix
                st.markdown("Fetch the latest AI news from various sources.")  # Removed st.sidebar prefix

                time_frame = st.selectbox("Select Time Frame", ["Daily", "Weekly", "Monthly"], index=0)
                
                if st.button("Fetch AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame
                
        return self.user_controls
