from shared_mcp_object import mcp
from pylint_core import GitRepoDirectoryReader

@mcp.tool()
def read_git_repo_python_modules(path: str):
    """Read Python modules from a Git repository.
    Args: path to the Git repository"""
    return GitRepoDirectoryReader(path).read_entire_git_repo()