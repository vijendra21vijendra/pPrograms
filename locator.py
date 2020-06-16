import requests
import folium
res = requests.get("https://ipinfo.io")
data = res.json()
print(data)
location = data['loc'].split(',')
print(type(location))
latitude = float(location[0])
longitude = float(location[1])
print(latitude, longitude)
