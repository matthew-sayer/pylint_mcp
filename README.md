# MCP Server Skeleton

A basic Model Context Protocol (MCP) server skeleton that demonstrates how to organise and structure MCP tools in a logical folder hierarchy.

## Overview

This project provides a foundational template for building MCP servers with a clean, organised structure. It includes:

- **Modular Tool Architecture**: Tools are organised in a dedicated `tools/` directory for easy management and discovery
- **Automatic Tool Registration**: The server automatically discovers and loads all tools from the tools directory
- **Example Implementation**: Includes a simple string reversal tool to demonstrate the MCP tool pattern

## Features

- **Organised Structure**: Clear separation of tools, resources, and configuration
- **Auto-Discovery**: Automatically registers all Python modules in the `tools/` directory
- **Example Tool**: A basic `reverse_string` tool that reverses any input string
- **FastMCP Integration**: Built using the FastMCP framework for easy development

## Project Structure

```
src/
├── tools/              # All MCP tools go here
│   └── tool.py         # Example string reversal tool
├── resources/          # Static resources and data files
├── main.py            # FastAPI server entry point
├── shared_mcp_object.py # Shared MCP instance and tool registration
└── config.py          # Configuration management
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

## Adding New Tools

To add a new tool:

1. Create a new Python file in the `tools/` directory
2. Import the shared MCP object: `from shared_mcp_object import mcp`
3. Use the `@mcp.tool()` decorator to register your function
4. The tool will be automatically discovered and registered when the server starts

## Example Tool Usage

The included `reverse_string` tool demonstrates the basic pattern:

```python
@mcp.tool()
def reverse_string(input: str) -> str:
    """Reverses the input string"""
    return input[::-1]
```

This skeleton provides a solid foundation for building more complex MCP servers with multiple tools and capabilities.