import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = '4.5_week.json'
with open(filename, "rb") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mag = eq_dict['properties']['mag']
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
    'size': [5*mag for mag in mags],
    'color': mags,
    'colorscale': 'YlGnBu',
    'reversescale': True,
    'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
