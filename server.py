#!/usr/bin/env python3
"""
GEMS Exchange MCP Server - FastMCP Implementation

A Model Context Protocol server for accessing GEMS Exchange APIs.
Provides agricultural, environmental, and climate data through standardized tools.
"""

import json
from typing import Any, Dict, List, Optional
import httpx
from mcp.server.fastmcp import FastMCP

# Import configuration and endpoint modules
from config import Config
from endpoints import weather, plant, datasets, spatial

# Initialize FastMCP server
mcp = FastMCP(Config.SERVER_NAME)

# Global HTTP client
client = httpx.AsyncClient(
    base_url=Config.BASE_URL,
    timeout=Config.TIMEOUT,
    headers=Config.get_headers()
)

# Weather Tools
@mcp.tool("weather_current")
async def weather_current(latitude: float, longitude: float) -> Dict[str, Any]:
    """
    Get current weather observations for a specific location.
    
    Args:
        latitude: Latitude in decimal degrees (-90 to 90)
        longitude: Longitude in decimal degrees (-180 to 180)
    """
    try:
        result = await weather.get_current(client, latitude, longitude)
        return {
            "location": {"latitude": latitude, "longitude": longitude},
            "data": result
        }
    except Exception as e:
        return {"error": str(e), "location": {"latitude": latitude, "longitude": longitude}}


@mcp.tool("weather_alerts")
async def weather_alerts(latitude: float, longitude: float) -> Dict[str, Any]:
    """
    Get severe weather alerts for a specific location.
    
    Args:
        latitude: Latitude in decimal degrees (-90 to 90)
        longitude: Longitude in decimal degrees (-180 to 180)
    """
    try:
        result = await weather.get_alerts(client, latitude, longitude)
        return {
            "location": {"latitude": latitude, "longitude": longitude},
            "data": result
        }
    except Exception as e:
        return {"error": str(e), "location": {"latitude": latitude, "longitude": longitude}}


@mcp.tool("weather_forecast")
async def weather_forecast(latitude: float, longitude: float, days: int = 5) -> Dict[str, Any]:
    """
    Get weather forecast for a specific location.
    
    Args:
        latitude: Latitude in decimal degrees (-90 to 90)
        longitude: Longitude in decimal degrees (-180 to 180)
        days: Number of forecast days (1-10, default 5)
    """
    try:
        result = await weather.get_forecast(client, latitude, longitude, days)
        return {
            "location": {"latitude": latitude, "longitude": longitude},
            "days": days,
            "data": result
        }
    except Exception as e:
        return {"error": str(e), "location": {"latitude": latitude, "longitude": longitude}}


@mcp.tool("weather_historical")
async def weather_historical(
    latitude: float, 
    longitude: float, 
    start_date: str, 
    end_date: str
) -> Dict[str, Any]:
    """
    Get historical weather data for a specific location.
    
    Args:
        latitude: Latitude in decimal degrees (-90 to 90)
        longitude: Longitude in decimal degrees (-180 to 180)
        start_date: Start date for historical data (YYYY-MM-DD format)
        end_date: End date for historical data (YYYY-MM-DD format)
    """
    try:
        result = await weather.get_historical(client, latitude, longitude, start_date, end_date)
        return {
            "location": {"latitude": latitude, "longitude": longitude},
            "period": {"start": start_date, "end": end_date},
            "data": result
        }
    except Exception as e:
        return {"error": str(e), "location": {"latitude": latitude, "longitude": longitude}}


# Plant Variety Tools
@mcp.tool("plant_variety_search")
async def plant_variety_search(variety_name: str, pedigree_depth: int = 5) -> Dict[str, Any]:
    """
    Search for plant varieties and get pedigree information.
    
    Args:
        variety_name: Name of the plant variety to search for
        pedigree_depth: Depth of pedigree information to retrieve (1-10, default 5)
    """
    try:
        result = await plant.search_variety(client, variety_name, pedigree_depth)
        return {
            "variety": variety_name,
            "pedigree_depth": pedigree_depth,
            "data": result
        }
    except Exception as e:
        return {"error": str(e), "variety": variety_name}


@mcp.tool("coefficient_parentage")
async def coefficient_parentage(variety_names: List[str], max_depth: int = 10) -> Dict[str, Any]:
    """
    Calculate coefficient of parentage matrix for plant varieties.
    
    Args:
        variety_names: List of variety names to analyze (minimum 2)
        max_depth: Maximum depth for parentage calculation (1-20, default 10)
    """
    try:
        result = await plant.calculate_cop_matrix(client, variety_names, max_depth)
        return {
            "varieties": variety_names,
            "max_depth": max_depth,
            "data": result
        }
    except Exception as e:
        return {"error": str(e), "varieties": variety_names}


# Dataset Listing Tools
@mcp.tool("climate_datasets")
async def climate_datasets() -> Dict[str, Any]:
    """List available climate datasets."""
    try:
        result = await datasets.list_climate(client)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool("grid_info")
async def grid_info(grid_id: Optional[int] = None) -> Dict[str, Any]:
    """
    Get information about GEMS grid system resolutions.
    
    Args:
        grid_id: Specific grid ID to get details for (0-6). If not provided, returns all grids.
    """
    try:
        result = await datasets.get_grid_info(client, grid_id)
        return {"grid_id": grid_id, "data": result} if grid_id else {"data": result}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool("soil_datasets")
async def soil_datasets() -> Dict[str, Any]:
    """List available soil datasets and properties."""
    try:
        result = await datasets.list_soil(client)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool("landcover_datasets")
async def landcover_datasets() -> Dict[str, Any]:
    """List available land cover datasets (LCMAP, NLCD, CDL)."""
    try:
        result = await datasets.list_landcover(client)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool("elevation_datasets")
async def elevation_datasets() -> Dict[str, Any]:
    """List available elevation datasets (DEM, LIDAR, SRTM)."""
    try:
        result = await datasets.list_elevation(client)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool("crop_datasets")
async def crop_datasets() -> Dict[str, Any]:
    """List available crop calendar datasets."""
    try:
        result = await datasets.list_crop(client)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool("hydro_datasets")
async def hydro_datasets() -> Dict[str, Any]:
    """List available water quality and hydrological datasets."""
    try:
        result = await datasets.list_hydro(client)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool("market_datasets")
async def market_datasets() -> Dict[str, Any]:
    """List available market accessibility datasets."""
    try:
        result = await datasets.list_market(client)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool("biotic_risk_datasets")
async def biotic_risk_datasets() -> Dict[str, Any]:
    """List available biotic risk datasets for agricultural pests/pathogens."""
    try:
        result = await datasets.list_biotic_risk(client)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}


# Spatial Data Tools
@mcp.tool("spatial_data_search")
async def spatial_data_search(
    api_type: str,
    dataset_name: str,
    bbox: Optional[str] = None,
    grid_level: Optional[int] = None,
    limit: int = 100
) -> Dict[str, Any]:
    """
    Search for spatial data objects in soil, landcover, climate, or biotic risk datasets.
    
    Args:
        api_type: Type of dataset API (soil, landcover, climate, biotic-risk, elevation, crop, hydro, market)
        dataset_name: Name of the dataset to search within
        bbox: Bounding box filter in format 'minx,miny,maxx,maxy'
        grid_level: GEMS grid resolution level (0-6)
        limit: Maximum number of results to return (1-300, default 100)
    """
    try:
        result = await spatial.search_data(client, api_type, dataset_name, bbox, grid_level, limit)
        return {
            "api_type": api_type,
            "dataset": dataset_name,
            "parameters": {
                "bbox": bbox,
                "grid_level": grid_level,
                "limit": limit
            },
            "data": result
        }
    except Exception as e:
        return {"error": str(e), "api_type": api_type, "dataset": dataset_name}


@mcp.tool("spatial_point_data")
async def spatial_point_data(
    api_type: str,
    dataset_name: str,
    object_id: int,
    latitude: float,
    longitude: float
) -> Dict[str, Any]:
    """
    Get point data for a specific location from soil, landcover, climate, or biotic risk datasets.
    
    Args:
        api_type: Type of dataset API (soil, landcover, climate, biotic-risk, elevation, crop, hydro, market)
        dataset_name: Name of the dataset
        object_id: Object ID from dataset search
        latitude: Latitude in decimal degrees (-90 to 90)
        longitude: Longitude in decimal degrees (-180 to 180)
    """
    try:
        result = await spatial.get_point_data(client, api_type, dataset_name, object_id, latitude, longitude)
        return {
            "api_type": api_type,
            "dataset": dataset_name,
            "object_id": object_id,
            "location": {"latitude": latitude, "longitude": longitude},
            "data": result
        }
    except Exception as e:
        return {
            "error": str(e), 
            "api_type": api_type, 
            "dataset": dataset_name,
            "location": {"latitude": latitude, "longitude": longitude}
        }


# Main execution
if __name__ == "__main__":
    mcp.run(transport="stdio")