import plotly.express as px 
import pandas as pd 
import numpy as np
import chart_studio.plotly as py

# File to Load
csv_file = "https://raw.githubusercontent.com/nsethi4310/GTProject2/michelle/csv/ba_beerstyles.csv"

# file path
beer_df = pd.read_csv(csv_file)
beer_df = beer_df[beer_df["Category"].isin(['Pale Ale', 'Stout', 'Wild / Sour Beer', 'India Pale Ale', 'Strong Ale', 'Pilsener & Pale Lager'])]
fig = px.sunburst(
    data_frame=beer_df,
    path=["Category", "Glassware", "Style"], 
    color="Category",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    maxdepth=-1,
)

fig.update_traces(textinfo='label')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()

with open('index_sunburst2.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))