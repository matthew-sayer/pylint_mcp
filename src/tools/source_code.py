from shared_mcp_object import mcp
from config import *
from tools.pylint_core import PylintInput

@mcp.tool()
async def run_pylint_command(path: str, options: str = ""):
    """
    Run pylint on a Python file with specified options.
    
    Args:
        path: The file path to analyze with pylint
        options: Pylint command line options as a space-separated string. 
                Examples: 
                - "--disable=C0114 --max-line-length=100"
                - "--output-format=json --disable=missing-docstring"
                - "--enable=all --score=no"
                
                Always prefix options with -- (double dash).
                Use = for options that take values.
                Separate multiple options with spaces.
    
    Returns: 
        result: The pylint command execution result.
    """

    result = PylintInput().run_pylint_command(path, options)

    return result