import folium  # ✅ Ensure this is at the top
import geopandas as gpd
import streamlit as st
from streamlit_folium import st_folium
from shapely.geometry import Point

# Set Streamlit layout
st.set_page_config(layout="wide")

# Load the Icelandic EEZ boundary (GeoJSON or shapefile)
eez = gpd.read_file("/Users/ha/Downloads/eez/eez.shp")

# Function to calculate overfishing risk
def get_overfishing_risk(lat, lon):
    if lat < 64.5 and lon < -18:
        return "High"
    return "Moderate"

# **Create side-by-side layout with smaller maps**
col1, col2 = st.columns(2)

# Initial map centered on Iceland
iceland_coords = [64.9631, -19.0208]
m = folium.Map(location=iceland_coords, zoom_start=5)

# Add EEZ boundary
folium.GeoJson(eez).add_to(m)

# Display the **interactive** map
with col1:
    st.write("### Click on the map to see risk levels")  
    clicked_location = st_folium(m, width=500, height=400)

# Process click event
if clicked_location and clicked_location.get("last_clicked"):
    lat = clicked_location["last_clicked"]["lat"]
    lon = clicked_location["last_clicked"]["lng"]
    
    risk_level = get_overfishing_risk(lat, lon)

    # **New map with marker**
    m = folium.Map(location=[lat, lon], zoom_start=6)
    folium.GeoJson(eez).add_to(m)

    # Define color based on risk level (valid Folium colors)
    color = "green" if risk_level == "Low" else "orange" if risk_level == "Moderate" else "red"

    # Create styled popup message
    popup_html = f"""
    <div style="color: {color}; font-weight: bold; text-align: center;">
        Risk: {risk_level}
    </div>
    """

    # Add marker with colored icon
    folium.Marker(
        [lat, lon],
        popup=folium.Popup(popup_html, max_width=200),
        icon=folium.Icon(color=color)  # ✅ Marker color now works
    ).add_to(m)

    # **Display updated map beside the original**
    with col2:
        st.write("### Risk Analysis")  
        st.write(f"**Coordinates:** ({lat}, {lon})")
        st.write(f"**Overfishing Risk:** {risk_level}")
        st_folium(m, width=500, height=400)
