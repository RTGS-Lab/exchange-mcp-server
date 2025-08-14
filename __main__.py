#!/usr/bin/env python3
"""
Main entry point for GEMS Exchange MCP Server
"""

from server import mcp

if __name__ == "__main__":
    mcp.run(transport="stdio")