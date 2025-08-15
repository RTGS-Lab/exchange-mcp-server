"""
Configuration management for GEMS Exchange MCP Server
"""
import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from project root
project_root = Path(__file__).parent.parent.parent.parent.parent
env_path = project_root / '.env'
load_dotenv(env_path)

class Config:
    """Configuration settings for the MCP server."""
    
    # Required settings
    GEMS_EXCHANGE_API_KEY: str = os.getenv("GEMS_EXCHANGE_API_KEY", "")
    
    # API settings
    BASE_URL: str = "https://exchange-1.gems.msi.umn.edu"
    TIMEOUT: float = 30.0
    
    # Server settings
    SERVER_NAME: str = "gems-exchange"
    SERVER_VERSION: str = "1.0.0"
    
    @classmethod
    def validate(cls) -> None:
        """Validate required configuration."""
        if not cls.GEMS_EXCHANGE_API_KEY:
            raise ValueError("GEMS_EXCHANGE_API_KEY environment variable is required. Obtain from https://exchange-1.gems.msi.umn.edu")
    
    @classmethod
    def get_headers(cls) -> dict:
        """Get HTTP headers for API requests."""
        return {"apikey": cls.GEMS_EXCHANGE_API_KEY}

# Validate configuration on import
Config.validate()