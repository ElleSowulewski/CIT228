import plotly.graph_objects as go
from plotly import offline

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
numWeb = [376, 348, 153, 104, 19]
explode = (.1, 0, 0, 0, 0)

fig = go.Figure(data=[go.Pie(labels=labels, values=numWeb)])

fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=20
    )

var = fig.update_layout(
    title_text="Popular Graphic Formats",
    title_font_size=30, 
    title_xref="paper", 
    title_yref="paper",
    margin_l=200,
    margin_r=200
    )

offline.plot({'data': fig, 'layout':var}, filename='plotly.html')