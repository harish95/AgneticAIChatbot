from langgraph.graph import StateGraph, START, END
from src.langgraphagenticAI.state.state import State
from src.langgraphagenticAI.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticAI.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraphagenticAI.nodes.chatbot_with_tool import ChatbotWithToolNode

class GraphBuilder:
    def __init__(self, model):
        print(f"GraphBuilder: Initializing with model type: {type(model)}")
        self.llm = model
        
    def setup_graph(self, usecase: str):
        """Setup the graph based on the use case"""
        
        print(f"Setting up graph for usecase: {usecase}")
        
        # Create a fresh graph for each setup
        graph_builder = StateGraph(State)
        
        try:
            if usecase == "Basic Chat":
                print("Building basic chatbot graph...")
                
                # Create and add the basic chatbot node
                basic_chatbot_node = BasicChatbotNode(self.llm)
                print(f"Created basic_chatbot_node: {type(basic_chatbot_node)}")
                
                graph_builder.add_node("chatbot", basic_chatbot_node.process)
                print("Added chatbot node to graph")
                
                graph_builder.add_edge(START, "chatbot")
                print("Added START -> chatbot edge")
                
                graph_builder.add_edge("chatbot", END)
                print("Added chatbot -> END edge")
                
                print("Basic chatbot graph built successfully")
            
            elif usecase == "Chatbot with Web":
                print("Building chatbot with web graph...")
                
                # Define tool and tool node
                tools = get_tools()
                tool_node = create_tool_node(tools)
                
                # Define the chatbot node
                obj_chat_with_node = ChatbotWithToolNode(self.llm)
                chatbot_node = obj_chat_with_node.create_chatbot(tools)
                
                # Add nodes to the graph        
                graph_builder.add_node("chatbot", chatbot_node)
                graph_builder.add_node("tools", tool_node)
                
                # Define conditional and direct edges
                graph_builder.add_edge(START, "chatbot")
                graph_builder.add_conditional_edges("chatbot", tools_condition)
                graph_builder.add_edge("tools", "chatbot")
                graph_builder.add_edge("chatbot", END)
                
                print("Chatbot with web graph built successfully")
            else:
                raise ValueError(f"Unknown usecase: {usecase}")
            
            # Debug: Print graph structure before compilation
            print(f"Graph nodes: {list(graph_builder.nodes.keys())}")
            print(f"Graph edges: {graph_builder.edges}")
            
            # Check if START edge exists
            start_edges = [edge for edge in graph_builder.edges if edge[0] == START]
            print(f"START edges: {start_edges}")
            
            if not start_edges:
                raise RuntimeError("No edges from START found!")
            
            # Check if END edge exists
            end_edges = [edge for edge in graph_builder.edges if edge[1] == END]
            print(f"END edges: {end_edges}")
            
            if not end_edges:
                raise RuntimeError("No edges to END found!")
            
            print("Compiling graph...")
            compiled_graph = graph_builder.compile()
            print("Graph compiled successfully")
            
            return compiled_graph
            
        except Exception as e:
            print(f"Error in setup_graph: {e}")
            print(f"Graph state - nodes: {list(graph_builder.nodes.keys()) if hasattr(graph_builder, 'nodes') else 'No nodes'}")
            print(f"Graph state - edges: {graph_builder.edges if hasattr(graph_builder, 'edges') else 'No edges'}")
            raise
        
        