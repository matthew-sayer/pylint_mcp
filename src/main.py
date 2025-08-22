from shared_mcp_object import mcp, register_all_tools

tools_count = register_all_tools()

if __name__ == "__main__":
    print(f"Registered tools from {tools_count} modules")
    mcp.run(transport='streamable-http')
    