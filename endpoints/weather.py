"""
Weather-related endpoints for GEMS Exchange
"""
from typing import Dict, Any
import httpx


async def get_current(client: httpx.AsyncClient, lat: float, lon: float) -> Dict[str, Any]:
    """Get current weather observations for a location."""
    response = await client.get(f"/weather/v2/current?lat={lat}&lon={lon}")
    response.raise_for_status()
    return response.json()


async def get_alerts(client: httpx.AsyncClient, lat: float, lon: float) -> Dict[str, Any]:
    """Get severe weather alerts for a location."""
    response = await client.get(f"/weather/v2/alerts?lat={lat}&lon={lon}")
    response.raise_for_status()
    return response.json()


async def get_forecast(client: httpx.AsyncClient, lat: float, lon: float, days: int = 5) -> Dict[str, Any]:
    """Get weather forecast for a location."""
    response = await client.get(f"/weather/v2/forecast?lat={lat}&lon={lon}&days={days}")
    response.raise_for_status()
    return response.json()


async def get_historical(client: httpx.AsyncClient, lat: float, lon: float, start_date: str, end_date: str) -> Dict[str, Any]:
    """Get historical weather data for a location."""
    response = await client.get(
        f"/weather/v2/history/energy?lat={lat}&lon={lon}&start_date={start_date}&end_date={end_date}"
    )
    response.raise_for_status()
    return response.json()