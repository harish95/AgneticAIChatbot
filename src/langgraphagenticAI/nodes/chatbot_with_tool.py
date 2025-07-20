from src.langgraphagenticAI.state.state import State

class ChatbotWithToolNode:
    """
    A node for a chatbot that can use tools.
    """
    def __init__(self, model):
        self.llm = model
        

    def process(self, state: State):
        """
        Process the input text using the LLM and available tools.
        """
        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.llm.invoke([{"role":"user", "content": user_input}])
        
        tools_response = f"Tool integration for :{user_input}"
        
        return {"messages":[llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """
        Create a chatbot with the given tools.
        """
        
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state: State) -> dict:
            """
            Process the input state using the LLM with tools.
            """
            try:
                response = llm_with_tools.invoke(state['messages'])
                return {"messages": [response]}
            except Exception as e:
                print(f"Error in chatbot node: {e}")
                return {"messages": [f"Error: {e}"]}
        
        return chatbot_node
    
    