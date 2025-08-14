"""
Spatial data search and retrieval endpoints for GEMS Exchange
"""
from typing import Dict, Any, Optional
import httpx


async def search_data(
    client: httpx.AsyncClient,
    api_type: str,
    dataset_name: str,
    bbox: Optional[str] = None,
    grid_level: Optional[int] = None,
    limit: int = 100
) -> Dict[str, Any]:
    """Search for spatial data objects in various dataset types."""
    params = [f"limit={limit}"]
    if bbox:
        params.append(f"bbox={bbox}")
    if grid_level is not None:
        params.append(f"grid={grid_level}")
    
    query_string = "&".join(params)
    response = await client.get(f"/{api_type}/v2/{dataset_name}/object/search?{query_string}")
    response.raise_for_status()
    return response.json()


async def get_point_data(
    client: httpx.AsyncClient,
    api_type: str,
    dataset_name: str,
    object_id: int,
    lat: float,
    lon: float
) -> Dict[str, Any]:
    """Get point data for a specific location from various dataset types."""
    response = await client.get(
        f"/{api_type}/v2/{dataset_name}/object/{object_id}/point?lat={lat}&lon={lon}"
    )
    response.raise_for_status()
    return response.json()