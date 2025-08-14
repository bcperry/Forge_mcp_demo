
# FastMCP template for REST applications

This repo provides a FastMCP application and a FastAPI stub for testing and development of MCP wrappers for REST APIs.

![system diagram](diagram.png)

## Local Development

This project includes both a stub API and a FastMCP wrapper for local development and testing.

### Running the Stub API

The stub API provides endpoints for testing the Forge application functionality:

```bash
fastapi dev stubapi/api.py --port 8042
```

This will start the FastAPI development server on port 8042 with auto-reload enabled.

### Running the FastMCP Wrapper

The FastMCP wrapper provides Model Context Protocol (MCP) tools that interact with the stub API:

```bash
fastmcp run mcp.py --transport streamable-http --port 8000
```

This will start the FastMCP server on port 8000, which can be used by MCP-compatible clients to interact with the Forge API through structured tools.