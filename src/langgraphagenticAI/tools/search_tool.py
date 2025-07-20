from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    
    tools = [TavilySearchResults(max_results=2)]
    
    return tools

def create_tool_node(tools=None):
    """
    Create a ToolNode for the Tavily search tool.
    """
    if tools is None:
        tools = get_tools()
    
    # Create a ToolNode with the Tavily search tool
    tool_node = ToolNode(tools=tools)    
    return tool_node