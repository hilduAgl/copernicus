
import geopandas as gpd
import folium
from folium.plugins import HeatMap

# Load the shapefile
shapefile_path = '/Users/ha/Downloads/eez/eez.shp'
gdf = gpd.read_file(shapefile_path)

# Convert to lat/lon if the CRS isn't already in EPSG:4326 (WGS84)
gdf = gdf.to_crs(epsg=4326)

# Check the columns to find the correct one for intensity or efficiency
print(gdf.columns)

# Replace 'efficiency' with the actual column name holding the intensity values
heat_data = [[row['geometry'].centroid.y, row['geometry'].centroid.x, row['efficiency']] for idx, row in gdf.iterrows()]

# Initialize the map, focusing on the ocean
m = folium.Map(location=[0, 0], zoom_start=2)

# Add the heatmap to the map
HeatMap(heat_data).add_to(m)

# Save the map to an HTML file
m.save('carbon_pump_efficiency_map.html')

