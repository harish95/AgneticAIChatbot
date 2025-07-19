from src.langgraphagenticAI.state.state import State


class BasicChatbotNode:
    """
    A node for a basic chatbot that can be used in the Agentic AI application.
    This node is designed to handle user input and provide responses based on the input.
    """
    
    def __init__(self, model):
        self.llm = model
        self.description = "A basic chatbot node for handling user interactions."
    
    def process(self, state:State) -> dict:
        """
        Generate a response based on the user's input message.

        Args:
            state (State): _description_

        Returns:
            dict: _description_
        """
        
        # Debug: Check if LLM is properly initialized
        if self.llm is None:
            raise ValueError("LLM model is not initialized")
        
        # Debug: Check the state messages
        print(f"State messages: {state['messages']}")
        print(f"LLM type: {type(self.llm)}")
        
        try:
            response = self.llm.invoke(state["messages"])
            print(f"LLM response: {response}")
            return {
                "messages": response
            }
        except Exception as e:
            print(f"Error in LLM invocation: {e}")
            raise e
        