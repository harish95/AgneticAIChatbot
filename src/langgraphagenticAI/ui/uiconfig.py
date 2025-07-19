from configparser import ConfigParser

class UIConfig:
    def __init__(self, config_file='src/langgraphagenticAI/ui/uiconfig.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config.get('DEFAULT', 'PAGE_TITLE', fallback='LangGraph Agentic AI')

    def get_llm_options(self):
        return self.config.get('DEFAULT', 'LLM_OPTIONS', fallback='Groq, Gemini').split(', ')

    def get_usecase_options(self):
        return self.config.get('DEFAULT', 'USECASE_OPTIONS', fallback='Basic Chat, Chatbot, AI News, Blog Generator').split(', ')

    def get_groq_model_options(self):
        return self.config.get('DEFAULT', 'GROQ_MODEL_OPTIONS', fallback='gemma2-9b-it, deepseek-r1-distill-llama-70b, mistral-saba-24b').split(', ')