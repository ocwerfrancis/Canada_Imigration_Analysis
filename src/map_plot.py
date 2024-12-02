
import folium
from data_processing import df_canada


# Create a plain world map
world_map = folium.Map(
    zoom_start=2,
    tiles='CartoDB positron'
)

# Path to GeoJSON file
world_geo = '/home/francis/Projects/Canada_Immigration_Analysis/countries.geojson'

# Generate Choropleth Map
folium.Choropleth(
    geo_data=world_geo,
    name='choropleth',
    data=df_canada,
    columns=['Country', 'Total'],  # Ensure these match your DataFrame
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Immigrants to Canada',
).add_to(world_map)

# Save the map as an HTML file
output_path = "world_map.html"
world_map.save(output_path)

print(f"Map has been saved to {output_path}")
