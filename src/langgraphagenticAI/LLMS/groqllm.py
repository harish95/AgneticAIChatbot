import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input
        
    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            
            if groq_api_key=="" and os.environ.get("GROQ_API_KEY") is None:
                st.error("⚠️ Please enter your GROQ API key to use Groq models.")
                return None
            
            # Use environment variable if user input is empty
            if groq_api_key == "":
                groq_api_key = os.environ.get("GROQ_API_KEY")
            
            if not groq_api_key:
                st.error("⚠️ Please enter your GROQ API key to use Groq models.")
                return None
            
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            return llm
        
        except Exception as e:
            st.error(f"Error initializing Groq LLM: {e}")
            return None
    