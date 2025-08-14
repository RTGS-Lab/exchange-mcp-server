"""
Plant variety and pedigree endpoints for GEMS Exchange
"""
from typing import Dict, Any, List
import httpx


async def search_variety(client: httpx.AsyncClient, variety_name: str, pedigree_depth: int = 5) -> Dict[str, Any]:
    """Search for plant varieties and get pedigree information."""
    response = await client.get(f"/pedtools/v1/{variety_name}?pedigree_depth={pedigree_depth}")
    response.raise_for_status()
    return response.json()


async def calculate_cop_matrix(client: httpx.AsyncClient, variety_names: List[str], max_depth: int = 10) -> Dict[str, Any]:
    """Calculate coefficient of parentage matrix for plant varieties."""
    response = await client.post(
        f"/pedtools/v1/cop/matrix?max_depth={max_depth}",
        json=variety_names
    )
    response.raise_for_status()
    return response.json()