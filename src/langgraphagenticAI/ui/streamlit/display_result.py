
import streamlit as st 
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResult:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        
    def display_result_on_ui(self):
        """
        Display the result of the graph execution on the Streamlit UI.
        """
        user_message = self.user_message
        graph = self.graph
        usecase = self.usecase
        print(user_message)
        
        if usecase == "Basic Chat":    
            # Create proper message format for the graph
            messages = [HumanMessage(content=user_message)]
            
            # Display user message first
            with st.chat_message("user"):
                st.write(user_message)
            
            for event in graph.stream({'messages': ("user", user_message)}):
                print(event.values())
                
                for value in event.values():
                    print(f"Value type: {type(value)}")
                    print(f"Value content: {value}")
                    
                    # Handle different possible structures
                    if isinstance(value, dict) and "messages" in value:
                        message = value["messages"]
                        
                        # Check if message is a single message or list of messages
                        if isinstance(message, list):
                            # Handle list of messages
                            for msg in message:
                                if isinstance(msg, AIMessage):
                                    with st.chat_message("assistant"):
                                        st.write(msg.content)
                        elif isinstance(message, AIMessage):
                            # Handle single AIMessage
                            with st.chat_message("assistant"):
                                st.write(message.content)
                                
                    elif isinstance(value, AIMessage):
                        # Handle direct AIMessage
                        with st.chat_message("assistant"):
                            st.write(value.content)
                            
                    elif isinstance(value, dict) and "content" in value:
                        # Handle dictionary with content key
                        with st.chat_message("assistant"):
                            st.write(value["content"])
                            
        elif usecase == "Chatbot with Web":
            # Create proper message format for the graph
            messages = [HumanMessage(content=user_message)]
            
            # Display user message first
            with st.chat_message("user"):
                st.write(user_message)
            
            for event in graph.stream({'messages': ("user", user_message)}):
                print(event.values())
                
                for value in event.values():
                    print(f"Value type: {type(value)}")
                    print(f"Value content: {value}")
                    
                    if isinstance(value, dict) and "messages" in value:
                        message = value["messages"]
                        
                        if isinstance(message, list):
                            for msg in message:
                                if isinstance(msg, AIMessage):
                                    with st.chat_message("assistant"):
                                        st.write(msg.content)
                                elif isinstance(msg, ToolMessage):
                                    with st.chat_message("tool"):
                                        st.write(msg.content)
                        elif isinstance(message, AIMessage):
                            with st.chat_message("assistant"):
                                st.write(message.content)
                        elif isinstance(message, ToolMessage):
                            with st.chat_message("tool"):
                                st.write(message.content)
                    elif isinstance(value, AIMessage):
                        with st.chat_message("assistant"):
                            st.write(value.content)
                    elif isinstance(value, ToolMessage):
                        with st.chat_message("tool"):
                            st.write(value.content)