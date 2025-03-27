import folium
import geopandas as gpd
import streamlit as st
from streamlit_folium import st_folium
import numpy as np
import random
from shapely.geometry import Point

# Set Streamlit layout
st.set_page_config(layout="wide")

# Load the Icelandic EEZ boundary (GeoJSON or shapefile) and the Iceland landmass
eez = gpd.read_file("/Users/ha/Downloads/eez/eez.shp")
land = gpd.read_file("/Users/ha/Downloads/iceland-latest-free.shp/gis_osm_landuse_a_free_1.shp")  # Load Iceland's land boundary shapefile

# Ensure both shapefiles are in the same coordinate reference system (CRS)
eez = eez.to_crs(epsg=4326)  # Convert to WGS84 (lat/lon)
land = land.to_crs(epsg=4326)

# Function to assign risk level with randomness and geographic consistency
def get_overfishing_risk(lat, lon):
    # Introduce randomness with some base geography
    base_risk = 0
    if lat < 64.5 and lon < -18:
        base_risk = 3  # High Risk
    elif lat < 65 and lon < -17:
        base_risk = 2  # Moderate Risk
    elif lat < 66 and lon < -16:
        base_risk = 1  # Low Risk
    
    # Add some random noise to the risk (e.g., ±1 risk level)
    risk_variation = random.choice([-1, 0, 1])
    risk = max(0, min(3, base_risk + risk_variation))  # Ensuring it stays between 0 and 3
    return risk

# Define color mapping
risk_colors = {
    0: "#ffffff00",  # Transparent (No risk)
    1: "#ffff99",  # Light Yellow (Low risk)
    2: "#ff4500",  # Orange-Red (Moderate risk)
    3: "#800080"   # Purple (High risk)
}

# Generate grid points within EEZ bounds (for heatmap effect)
bounds = eez.total_bounds  # minx, miny, maxx, maxy
lats = np.linspace(bounds[1], bounds[3], 30)
lons = np.linspace(bounds[0], bounds[2], 30)

# Create the base map
m = folium.Map(location=[64.9631, -19.0208], zoom_start=5)
folium.GeoJson(eez, name="EEZ").add_to(m)

# Add circular markers to represent areas with the same risk level
for lat in lats:
    for lon in lons:
        # Check if the point (lat, lon) is inside the EEZ area (sea) and outside land
        point = Point(lon, lat)
        if eez.contains(point).any() and not land.contains(point).any():  # Not on land, inside EEZ
            risk = get_overfishing_risk(lat, lon)
            if risk > 0:  # Avoid rendering transparent areas
                folium.CircleMarker(
                    location=[lat + 0.15, lon + 0.15],  # Offset slightly to avoid overlap
                    radius=10,  # Adjust the size of the circle
                    color=risk_colors[risk],
                    fill=True,
                    fill_color=risk_colors[risk],
                    fill_opacity=0.6,
                    weight=0
                ).add_to(m)

# Display the interactive map
st.write("### Overfishing Risk Heatmap")
st_folium(m, width=700, height=500)
