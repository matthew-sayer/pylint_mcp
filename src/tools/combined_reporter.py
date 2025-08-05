from shared_mcp_object import mcp
from pylint_core import PylintUniverseCommandFactory

@mcp.tool()
async def run_full_report(path: str, pylint_options: str = "", symilar_options: str = ""):
    """
    Runs comprehensive Python code analysis combining Pylint and Symilar tools on specified path.
    
    Args:
        path (str): File path or directory to analyze. Supports single files or entire directories.
        pylint_options (str, optional): Pylint command line options. Common options include:
            --output-format: text|json|colorized|parseable|msvs|github (default: text)
            --reports: yes|no - Display full report or only messages (default: no)
            --score: yes|no - Show evaluation score (default: yes)
            --disable: Disable specific messages (e.g. C0114,missing-docstring,too-few-public-methods)
            --enable: Enable specific messages or categories
            --max-line-length: Maximum line length (default: 100)
            --max-args: Maximum function arguments (default: 5)
            --max-locals: Maximum local variables (default: 15)
            --max-statements: Maximum statements per function (default: 50)
            --min-public-methods: Minimum public methods per class (default: 2)
            --errors-only: Show only errors and fatal messages
            --exit-zero: Always return success exit code
            --jobs: Number of parallel processes (0 for auto-detect)
            --fail-under: Score threshold for failure (default: 10)
            --rcfile: Configuration file path
            --ignore: Files/directories to skip
            --ignore-patterns: Regex patterns to ignore
            --verbose: Verbose output
            
        symilar_options (str, optional): Symilar command line options. Available options:
            -d, --duplicates: Minimum lines for similarity detection (default: 4)
            -i, --ignore-comments: Ignore comments in similarity computation
            --ignore-docstrings: Ignore docstrings in similarity computation  
            --ignore-imports: Ignore import statements in similarity computation
            --ignore-signatures: Ignore function signatures in similarity computation
            
    Returns:
        dict: Combined analysis report containing:
            - pylint: Complete Pylint analysis results including messages, score, and statistics
            - symilar: Code duplication analysis across all Python files in the specified path
        You should provide a detailed code quality and duplication report to the user, with actionable insights and recommendations that could be used by a language model to improve the codebase.
        Provide suggestions of libraries or efficiencies that could be better used, or potential ways to follow SOLID principles better, or similar best practices.

        ***Organise the report in a clear and concise manner, highlighting key categories.***

    Examples:
        Basic analysis: run_full_report("./src")
        JSON output with relaxed rules: run_full_report("./src", "--output-format=json --disable=C0114,too-few-public-methods")
        Strict similarity checking: run_full_report("./project", "", "-d 2 --ignore-comments")
        Error-only analysis: run_full_report("./code", "--errors-only --exit-zero")
        
    Note: 
        - Pylint analyzes the entire directory structure
        - Symilar compares all Python files found in the path for code duplication
        - Both tools automatically discover Python files recursively in directories
        - Use comma-separated values for multiple options (e.g. "--disable=C0114,W0613")

    """
    pylint_result = PylintUniverseCommandFactory("pylint", path, pylint_options).run_code_quality_tool()
    symilar_result = PylintUniverseCommandFactory("symilar", path, symilar_options).run_similarity_checker()

    return {"Code Quality Report": {
        "pylint": pylint_result,
        "symilar": symilar_result
        }
    }
