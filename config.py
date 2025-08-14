"""
Configuration management for GEMS Exchange MCP Server
"""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration settings for the MCP server."""
    
    # Required settings
    GEMS_API_KEY: str = os.getenv("GEMS_API_KEY", "")
    
    # API settings
    BASE_URL: str = "https://exchange-1.gems.msi.umn.edu"
    TIMEOUT: float = 30.0
    
    # Server settings
    SERVER_NAME: str = "gems-exchange"
    SERVER_VERSION: str = "1.0.0"
    
    @classmethod
    def validate(cls) -> None:
        """Validate required configuration."""
        if not cls.GEMS_API_KEY:
            raise ValueError("GEMS_API_KEY environment variable is required")
    
    @classmethod
    def get_headers(cls) -> dict:
        """Get HTTP headers for API requests."""
        return {"apikey": cls.GEMS_API_KEY}

# Validate configuration on import
Config.validate()