import streamlit as st
from src.langgraphagenticAI.ui.streamlit.loadui import LoadUI
from src.langgraphagenticAI.LLMS.groqllm import GroqLLM
from src.langgraphagenticAI.graph.graph_builder import GraphBuilder
from src.langgraphagenticAI.ui.streamlit.display_result import DisplayResult

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
    
    if user_message:
        try:
            ## Configure the llm
            obj_llm_config = GroqLLM( user_controls_input= user_input)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error: LLM model could not be initialized. Please check your configuration.")
                return
            
            # Inititalize and set up the graph based on use case
            usecase = user_input.get("selected_usecase")
            
            if not usecase:
                st.error("No use case selected. Please select a use case from the sidebar.")
                return
            ## Graph builder
            graph_builder = GraphBuilder(model=model)
            
            try:
                graph = graph_builder.setup_graph(usecase=usecase)
                DisplayResult(usecase=usecase, graph=graph, user_message=user_message).display_result_on_ui()
                
            except Exception as e:
                st.error(f"Error setting up graph: {e}")
                return
            
        except Exception as e:
            st.error(f"Error setting up graph: {e}")
            