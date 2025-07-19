from langgraph.graph import StateGraph, START, END
from src.langgraphagenticAI.state.state import State
from src.langgraphagenticAI.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self,model):
        print(f"GraphBuilder: Initializing with model type: {type(model)}")
        self.llm = model
        self.graph_builder = StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
            
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
        
        
    
    def setup_graph(self,usecase:str):
        """setup the graph based on the use case"""
        
        if usecase == "Basic Chat":
            self.basic_chatbot_build_graph()
        
        return self.graph_builder.compile()
    