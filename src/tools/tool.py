from shared_mcp_object import mcp
from config import *

@mcp.tool()
async def reverse_string(input: str):
    """
    A test tool that shows how an MCP tool can be defined, with a simple string reversal operation.
    
    Args:
        "input": str: The input string to be reversed.
    
    Returns: 
        output: str: The reversed string.
    """

    output = input[::-1] 

    return output