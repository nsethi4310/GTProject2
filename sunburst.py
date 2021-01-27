import chart_studio.plotly as py
import plotly.express as px 
import pandas as pd 
import numpy as np
import plotly.io as pio

df = pd.read_csv("csv/usa_breweries2.csv")
df = df[df["state"].isin(['NY', 'PA', 'GA'])]
df = df[df["types"].isin(['Brewery', 'Brewery, Bar', 'Brewery, Bar, Eatery'])]
df = df[df["city"].isin(['Atlanta', 'Alpharetta', 'Savannah', 'Athens', 'Brooklyn', 'New York', 'Rochester', 'Buffalo', 'Philapdelphia', 'Pittsburgh', 'Harrisburg', 'Lancaster'])]

fig = px.sunburst(
    data_frame=df,
    path=["state", "types", "city", "name"], 
    color="state",
    color_discrete_sequence=px.colors.qualitative.Vivid,
    maxdepth=-1,
)

fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()

with open('index_sunburst.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))

#py.plot(fig, filename = 'sunburst', auto_open=True)