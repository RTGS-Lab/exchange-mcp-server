# GEMS Exchange MCP Server

A Model Context Protocol (MCP) server providing access to the GEMS Exchange APIs for agricultural, environmental, and climate data. This server enables AI assistants to query comprehensive datasets for research and analysis.

## Overview

GEMS Exchange is a portfolio of interoperable streaming data services for agri-food applications, spanning Genetics × Environment × Management × Socioeconomic data domains. The APIs provide spatially and temporally explicit datasets with acute focus on geospatial and temporal attributes.

## API Services Hierarchy

### 1. **Pedtools API** (`/pedtools/v1`)
Plant breeding and variety information tools
- **Varieties**: Get matching plant varieties with pedigree information
  - `GET /{variety}` - Get varieties matching a name with pedigree depth
- **Coefficient of Parentage**: Calculate genetic relationships between varieties  
  - `POST /cop/matrix` - Get coefficient of parentage matrix for variety list

### 2. **Weather API** (`/weather/v2`) 
Current, historical, and forecast weather data
- **Alerts**: Severe weather alerts from meteorological agencies
  - `GET /alerts?lat={lat}&lon={lon}` - Get weather alerts for location
- **Current Weather**: Real-time weather observations
  - `GET /current?lat={lat}&lon={lon}` - Get current weather for location
- **Historical Weather**: Past weather data
  - `GET /historical?lat={lat}&lon={lon}` - Get historical weather data
- **Forecast**: Weather predictions
  - `GET /forecast?lat={lat}&lon={lon}` - Get weather forecast for location

### 3. **Climate API** (`/climate/v2`)
Long-term climate datasets from multiple sources (CRU, Daymet, PRISM)
- **Grid System**: GEMS hierarchical grid metadata
  - `GET /grid` - Get all available grid resolutions
  - `GET /grid/{id}` - Get specific grid metadata
- **Datasets**: Climate data collections
  - `GET /datasets` - List available climate datasets
- **Spatial Data**: Location-based climate queries
  - `GET /{keyname}/object/search` - Search climate objects with filters
  - `GET /{keyname}/object/{id}` - Get climate object metadata
  - `GET /{keyname}/object/{id}/point` - Get point climate data
  - `GET /{keyname}/object/{id}/raster` - Get raster climate data
  - `GET /{keyname}/object/{id}/stats` - Get climate data statistics

### 4. **Biotic Risk API** (`/biotic-risk/v2`)
Agricultural pest and pathogen risk geographies (24 risk types, global coverage)
- **Grid System**: Same grid endpoints as Climate API
- **Risk Datasets**: Biotic risk data collections
- **Spatial Analysis**: Same spatial endpoints as Climate API for risk data

### 5. **Crop API** (`/crop/v2`)
Global crop calendar and planting information
- **Crop Calendar**: Global planting and harvest dates (circa 2007)
- **Grid System**: Standard GEMS grid system
- **Crop Data**: Crop-specific information with spatial context

### 6. **Elevation API** (`/elevation/v2`)
Digital elevation models from multiple sources
- **Global Data**: GMTED2010, SRTM elevation datasets
- **High-Resolution**: LiDAR-derived elevation for Minnesota
- **Terrain Analysis**: Slope calculations and terrain derivatives

### 7. **Hydro API** (`/hydro/v2`)
Water quality and hydrological datasets
- **Lake Water Quality**: Minnesota satellite-derived water quality data
- **Catchments**: Watershed and lake boundary data
- **Water Bodies**: Hydrological feature analysis

### 8. **Land Cover API** (`/landcover/v2`)
Land use and land cover datasets
- **LCMAP**: Land Change Monitoring, Assessment, and Projection
- **NLCD**: National Land Cover Database
- **CDL**: Cropland Data Layer for Minnesota
- **Temporal Analysis**: Land cover change over time

### 9. **Market API** (`/market/v2`)
Global accessibility and market indicators
- **Accessibility**: Travel time to nearest cities and ports (2015)
- **Economic Geography**: Market access indicators
- **Transportation**: Infrastructure accessibility analysis

### 10. **Soil API** (`/soil/v2`)
Soil properties and characteristics
- **Soil Properties**: Physical and chemical soil characteristics
- **Spatial Coverage**: Soil data with geographic context
- **Agricultural Applications**: Soil suitability and management data

## Common API Patterns

### Authentication
All APIs use header-based authentication:
```http
apikey: YOUR_API_KEY
```

### Grid System
GEMS uses a discrete hierarchical grid system (EASE-Grid 2.0 projection):
- **Grid Level 0**: 36km resolution (global)
- **Grid Level 1**: ~9km resolution
- **Grid Level 3**: ~1km resolution  
- **Grid Level 4**: ~100m resolution
- **Grid Level 5**: ~10m resolution
- **Grid Level 6**: 1m resolution

### Spatial Queries
Most APIs support:
- **Bounding Box**: `bbox=minx,miny,maxx,maxy`
- **Point Queries**: `lat` and `lon` parameters
- **GeoJSON**: POST endpoints accept polygon geometries
- **Pagination**: `offset` and `limit` parameters

### Response Formats
- **JSON**: Primary response format
- **GeoTIFF**: Raster data (with compression options)
- **Statistics**: Summary statistics for spatial data
- **Histograms**: Data distribution analysis

## MCP Server Setup

### Prerequisites
- Python 3.8+
- GEMS Exchange API key

### Installation
1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   ```
4. Set up environment variables:
   ```bash
   export GEMS_API_KEY="your-api-key-here"
   ```

### Usage with Claude Code
1. Start the MCP server:
   ```bash
   python -m server
   ```
2. Add to your Claude Code configuration:
   ```json
   {
     "mcpServers": {
       "gems-exchange": {
         "command": "python",
         "args": ["-m", "server"],
         "env": {
           "GEMS_API_KEY": "your-api-key"
         }
       }
     }
   }
   ```

### Usage with Other AI Assistants

#### Gemini CLI
```bash
gemini configure mcp add gems-exchange python -m server
```

#### ChatGPT in Browser COMING IN THE FUTURE
Install the MCP browser extension and add:
```json
{
  "name": "gems-exchange",
  "command": "python -m server",
  "env": {"GEMS_API_KEY": "your-key"}
}
```

#### Claude in Browser COMING IN THE FUTURE
Use the Claude MCP extension with the same configuration as Claude Code.

## API Base URLs
- **Production**: `https://exchange-1.gems.msi.umn.edu`
- **Documentation**: `https://exchange-1.gems.msi.umn.edu/portal/home`

## Support
- **Email**: gemssupport@umn.edu
- **Website**: https://gems.umn.edu/exchange
- **GitHub**: https://github.com/GEMS-UMN

## Data Citation
When using GEMS Exchange data, please cite appropriately according to the dataset documentation and follow the terms of use for each API service.

## License
This MCP server is provided under MIT License. Individual datasets may have their own licensing terms - please refer to the GEMS Exchange documentation for specific dataset usage rights.
