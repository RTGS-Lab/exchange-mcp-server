#!/usr/bin/env python3
"""
Test script for GEMS Exchange MCP Server
"""
import asyncio
import json
from server import (
    weather_current,
    climate_datasets,
    soil_datasets,
    grid_info,
    plant_variety_search
)


async def test_tools():
    """Test various MCP tools."""
    print("Testing GEMS Exchange MCP Server Tools\n")
    print("=" * 50)
    
    # Test weather current
    print("\n1. Testing weather_current for Minneapolis (44.98, -93.26):")
    try:
        result = await weather_current(44.98, -93.26)
        print(f"   Status: ✓ Success")
        if "error" in result:
            print(f"   Error: {result['error']}")
        else:
            print(f"   Location: {result.get('location', {})}")
    except Exception as e:
        print(f"   Status: ✗ Failed - {e}")
    
    # Test climate datasets
    print("\n2. Testing climate_datasets:")
    try:
        result = await climate_datasets()
        print(f"   Status: ✓ Success")
        if "error" in result:
            print(f"   Error: {result['error']}")
        else:
            print(f"   Data available: {'data' in result}")
    except Exception as e:
        print(f"   Status: ✗ Failed - {e}")
    
    # Test soil datasets
    print("\n3. Testing soil_datasets:")
    try:
        result = await soil_datasets()
        print(f"   Status: ✓ Success")
        if "error" in result:
            print(f"   Error: {result['error']}")
        else:
            print(f"   Data available: {'data' in result}")
    except Exception as e:
        print(f"   Status: ✗ Failed - {e}")
    
    # Test grid info
    print("\n4. Testing grid_info (all grids):")
    try:
        result = await grid_info()
        print(f"   Status: ✓ Success")
        if "error" in result:
            print(f"   Error: {result['error']}")
        else:
            print(f"   Data available: {'data' in result}")
    except Exception as e:
        print(f"   Status: ✗ Failed - {e}")
    
    # Test plant variety search
    print("\n5. Testing plant_variety_search for 'Pioneer P9234':")
    try:
        result = await plant_variety_search("Pioneer P9234", pedigree_depth=3)
        print(f"   Status: ✓ Success")
        if "error" in result:
            print(f"   Error: {result['error']}")
        else:
            print(f"   Variety: {result.get('variety', '')}")
            print(f"   Pedigree depth: {result.get('pedigree_depth', 0)}")
    except Exception as e:
        print(f"   Status: ✗ Failed - {e}")
    
    print("\n" + "=" * 50)
    print("Testing complete!")


if __name__ == "__main__":
    asyncio.run(test_tools())