![Pylint MCP Server Logo](assets/pylint_mcp_logo.png)

# Pylint MCP Server

A Model Context Protocol (MCP) server that provides Pylint code analysis capabilities through MCP tools.

## Overview

This project provides an MCP server specifically designed for Python code analysis using Pylint. It includes:

- **Pylint Integration**: Run Pylint analysis on Python files with customizable options
- **Modular Tool Architecture**: Tools are organised in a dedicated `tools/` directory for easy management and discovery
- **Automatic Tool Registration**: The server automatically discovers and loads all tools from the tools directory
- **FastMCP Integration**: Built using the FastMCP framework for easy development

## Features

- **Pylint Analysis Tool**: Run Pylint with custom options on any Python file
- **Subprocess Execution**: Safe execution of Pylint commands through subprocess calls
- **Auto-Discovery**: Automatically registers all Python modules in the `tools/` directory

## Project Structure

```
src/
├── tools/              # All MCP tools go here
│   └── pylint_tools.py # Pylint analysis tools
├── resources/          # Static resources and data files
├── main.py            # FastAPI server entry point
├── shared_mcp_object.py # Shared MCP instance and tool registration
├── config.py          # Configuration management
└── pylint_core.py     # Core Pylint execution logic
```

## Getting Started

1. **Install Dependencies**:
   ```bash
   uv sync
   ```

2. **Run the Server**:
   ```bash
   uv run fastapi dev main.py
   ```

3. **Connect via MCP**: Configure your MCP client to connect to `http://localhost:8000/sse`

## Available Tools

### `run_local_pylint_command`

Run Pylint analysis on Python files with customizable options.

**Parameters:**
- `path`: The file path to analyze with Pylint
- `options`: Pylint command line options as a space-separated string

**Example usage:**
```python
# Basic analysis
result = await run_local_pylint_command("my_script.py")

# With custom options
result = await run_local_pylint_command(
    "my_script.py", 
    "--disable=C0114 --max-line-length=100"
)

# JSON output format
result = await run_local_pylint_command(
    "my_script.py",
    "--output-format=json --disable=missing-docstring"
)
```

## Adding New Tools

To add a new tool:

1. Create a new Python file in the `tools/` directory
2. Import the shared MCP object: `from shared_mcp_object import mcp`
3. Use the `@mcp.tool()` decorator to register your function
4. The tool will be automatically discovered and registered when the server starts

## Pylint Options

The server supports all standard Pylint command-line options. Some useful examples:

- `--disable=C0114`: Disable missing module docstring warnings
- `--max-line-length=100`: Set maximum line length
- `--output-format=json`: Output results in JSON format
- `--enable=all --score=no`: Enable all checks without scoring

Always prefix options with `--` (double dash) and use `=` for options that take values.

This MCP server provides a convenient way to integrate Pylint code analysis into your development workflow through the Model Context Protocol.