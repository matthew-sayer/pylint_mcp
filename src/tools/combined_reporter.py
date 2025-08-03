from shared_mcp_object import mcp
from pylint_core import PylintUniverseCommandFactory

@mcp.tool()
def run_full_report(path: str, options: str = ""):
    """
    Runs the entire Pylint universe of tools on a specified path."""
    pylint_result = PylintUniverseCommandFactory("pylint", path, options).run_code_quality_tool()
    symilar_result = PylintUniverseCommandFactory("symilar", path, options).run_code_quality_tool()
    pyreverse_result = PylintUniverseCommandFactory("pyreverse", path, options).run_code_quality_tool()
    
    return {"Code Quality Report": {
        "pylint": pylint_result,
        "symilar": symilar_result,
        "pyreverse": pyreverse_result
        }
    }