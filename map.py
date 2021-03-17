import folium
import pandas
import json


data = pandas.read_csv("c_cities.csv", encoding='latin-1')
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Capital"])


map = folium.Map(location=[54.37976337018291, 19.82089237395067], zoom_start=5, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Capital Cities")

for lt, ln, name in zip(lat, lon, name):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=name, icon=folium.Icon(color="red", icon="info-sign")))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
style_function=lambda x: {"fillColor":"green" if x ['properties']['POP2005'] < 10000000 
else "orange" if 10000000 <= x['properties']['POP2005'] < 20000000 else "red" }))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("map1.html")
