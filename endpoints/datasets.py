"""
Dataset listing endpoints for GEMS Exchange
"""
from typing import Dict, Any, Optional
import httpx


async def list_climate(client: httpx.AsyncClient) -> Dict[str, Any]:
    """List available climate datasets."""
    response = await client.get("/climate/v2/datasets")
    response.raise_for_status()
    return response.json()


async def get_grid_info(client: httpx.AsyncClient, grid_id: Optional[int] = None) -> Dict[str, Any]:
    """Get information about GEMS grid system resolutions."""
    if grid_id is not None:
        response = await client.get(f"/climate/v2/grid/{grid_id}")
    else:
        response = await client.get("/climate/v2/grid")
    response.raise_for_status()
    return response.json()


async def list_soil(client: httpx.AsyncClient) -> Dict[str, Any]:
    """List available soil datasets and properties."""
    response = await client.get("/soil/v2/datasets")
    response.raise_for_status()
    return response.json()


async def list_landcover(client: httpx.AsyncClient) -> Dict[str, Any]:
    """List available land cover datasets."""
    response = await client.get("/landcover/v2/datasets")
    response.raise_for_status()
    return response.json()


async def list_elevation(client: httpx.AsyncClient) -> Dict[str, Any]:
    """List available elevation datasets."""
    response = await client.get("/elevation/v2/datasets")
    response.raise_for_status()
    return response.json()


async def list_crop(client: httpx.AsyncClient) -> Dict[str, Any]:
    """List available crop calendar datasets."""
    response = await client.get("/crop/v2/datasets")
    response.raise_for_status()
    return response.json()


async def list_hydro(client: httpx.AsyncClient) -> Dict[str, Any]:
    """List available water quality and hydrological datasets."""
    response = await client.get("/hydro/v2/datasets")
    response.raise_for_status()
    return response.json()


async def list_market(client: httpx.AsyncClient) -> Dict[str, Any]:
    """List available market accessibility datasets."""
    response = await client.get("/market/v2/datasets")
    response.raise_for_status()
    return response.json()


async def list_biotic_risk(client: httpx.AsyncClient) -> Dict[str, Any]:
    """List available biotic risk datasets."""
    response = await client.get("/biotic-risk/v2/datasets")
    response.raise_for_status()
    return response.json()