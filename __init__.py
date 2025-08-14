"""
GEMS Exchange MCP Server

A Model Context Protocol server for accessing GEMS Exchange APIs.
"""

__version__ = "1.0.0"

from .gems_exchange_mcp import main, GEMSExchangeServer

__all__ = ["main", "GEMSExchangeServer"]