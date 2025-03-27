import folium
import geopandas as gpd
import streamlit as st
from streamlit_folium import st_folium
from shapely.geometry import Point

# Load the Icelandic EEZ boundary (GeoJSON or shapefile)
eez = gpd.read_file("/Users/ha/Downloads/eez/eez.shp")

# Create a map centered on Iceland
iceland_coords = [64.9631, -19.0208]
m = folium.Map(location=iceland_coords, zoom_start=5)

# Add the EEZ boundary to the map
folium.GeoJson(eez).add_to(m)

# Function to calculate overfishing risk based on coordinates
def get_overfishing_risk(lat, lon):
    # Dummy example: Change this to actual logic based on environmental data
    risk_level = "Moderate"  # Example risk level
    if lat < 64.5 and lon < -18:  # Dummy condition for high risk
        risk_level = "High"
    return risk_level

# Display the map and capture the clicked location
clicked_location = st_folium(m, width=700)

# Check if the user clicked on the map
if clicked_location and "last_clicked" in clicked_location:
    # Extract the coordinates from the last clicked location
    lat = clicked_location["last_clicked"]["lat"]
    lon = clicked_location["last_clicked"]["lng"]

    # Get the overfishing risk for the clicked location
    risk_level = get_overfishing_risk(lat, lon)

    # Add a marker at the clicked location
    folium.Marker([lat, lon], popup=f"Overfishing Risk: {risk_level}").add_to(m)

    # Re-render the map with the new marker
    st_folium(m, width=700)

    # Display the overfishing risk
    st.write(f"Overfishing Risk at Latitude {lat} and Longitude {lon}: {risk_level}")
