import os
import importlib
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP_QUICK_START")

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')
TOOLS_DIR = os.path.join(os.path.dirname(__file__), 'tools')


def register_all_tools():
    """Discover and register all tools from the tools directory"""
    
    # Track how many tools were registered
    registered = 0
    
    # List all Python files in the tools directory
    for filename in os.listdir(TOOLS_DIR):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            
            try:
                import sys
                base_dir = os.path.dirname(__file__)
                if base_dir not in sys.path:
                    sys.path.insert(0, base_dir)
                
                module = importlib.import_module(f'tools.{module_name}')
                
                print(f"Loaded module: tools.{module_name}")
                registered += 1
            except Exception as e:
                print(f"Error loading tools from {module_name}: {str(e)}")
                
    return registered