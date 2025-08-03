from shared_mcp_object import mcp
from pylint_core import PylintUniverseCommandFactory

@mcp.tool()
async def run_pylint_cmd(path: str, options: str = ""):
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

    result = PylintUniverseCommandFactory("pylint", path, options).run_code_quality_tool()
    return result

@mcp.tool()
async def run_symilar_cmd(path: str, options: str = ""):
    """
    Run Symilar on a Python file with specified options."""

    result = PylintUniverseCommandFactory("symilar", path, options).run_code_quality_tool()
    return result

@mcp.tool()
async def run_pyreverse_cmd(path: str, options: str = ""):
    """
    Run Pyreverse on a Python file with specified options."""
    result = PylintUniverseCommandFactory("pyreverse", path, options).run_code_quality_tool()
    return result
