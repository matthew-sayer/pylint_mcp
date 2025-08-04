from shared_mcp_object import mcp
from pylint_core import PylintUniverseCommandFactory

@mcp.tool()
async def run_pylint_cmd(path: str, options: str = ""):
    """
    Run Pylint code quality analysis on Python files with specified options.
    
    Args:
        path (str): File path or directory to analyze with Pylint
        options (str, optional): Pylint command line options. Common options include:
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
            
    Returns:
        dict: Pylint analysis results including messages, score, and code quality metrics
        
    Examples:
        Basic analysis: path="./src/main.py"
        JSON output: options="--output-format=json --disable=C0114"
        Errors only: options="--errors-only --exit-zero"
    """

    result = PylintUniverseCommandFactory("pylint", path, options).run_code_quality_tool()
    return result

@mcp.tool()
async def run_symilar_cmd(path: str, options: str = ""):
    """
    Run Symilar code duplication analysis on Python files with specified options.
    
    Args:
        path (str): File path or directory to analyze for code similarities
        options (str, optional): Symilar command line options. Available options:
            -d, --duplicates: Minimum lines for similarity detection (default: 4)
            -i, --ignore-comments: Ignore comments in similarity computation
            --ignore-docstrings: Ignore docstrings in similarity computation
            --ignore-imports: Ignore import statements in similarity computation
            --ignore-signatures: Ignore function signatures in similarity computation
            
    Returns:
        dict: Symilar analysis results showing duplicate code blocks and similarity percentages
        
    Examples:
        Basic analysis: path="./src"
        Strict checking: options="-d 2 --ignore-comments"
        Ignore docstrings: options="--ignore-docstrings --ignore-imports"
        
    Note: Symilar automatically processes all Python files in the specified directory
    """

    result = PylintUniverseCommandFactory("symilar", path, options).run_similarity_checker()
    return result

@mcp.tool()
async def run_pyreverse_cmd(path: str, options: str = ""):
    """
    Run Pyreverse UML diagram generation and dependency analysis on Python files.
    
    Args:
        path (str): File path or directory to analyze with Pyreverse
        options (str, optional): Pyreverse command line options. Common options include:
            --output, -o: Output format (dot|puml|plantuml|mmd|html) (default: dot)
            --filter-mode, -f: Filter mode (PUB_ONLY|ALL|SPECIAL|OTHER) (default: PUB_ONLY)
            --class, -c: Create class diagram for specific class
            --show-ancestors, -a: Show ancestor generations
            --all-ancestors, -A: Show all ancestors of all classes
            --show-associated, -s: Show association levels
            --all-associated, -S: Show all associated classes recursively
            --show-builtin, -b: Include builtin objects
            --show-stdlib, -L: Include standard library objects
            --module-names, -m: Include module names in class representation
            --only-classnames, -k: Show only class names without attributes/methods
            --no-standalone: Only show nodes with connections
            --colorized: Use colored output
            --max-color-depth: Color depth for packages (default: 2)
            --project, -p: Set project name
            --output-directory, -d: Set output directory path
            --verbose: Verbose output for debugging
            
    Returns:
        dict: Pyreverse analysis results and generated diagram information
        
    Examples:
        Basic UML: path="./src/main.py"
        PNG output: options="--output=png --colorized"
        Class diagram: options="--class=MyClass --all-ancestors"
        PlantUML format: options="--output=puml --show-associated=2"
        
    Note: Pyreverse generates UML diagrams and dependency graphs for code visualization
    """

    result = PylintUniverseCommandFactory("pyreverse", path, options).run_code_quality_tool()
    return result
