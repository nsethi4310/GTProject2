import plotly.express as px 
import pandas as pd 
import numpy as np

df = pd.read_csv("ba_beerstyles.csv")

fig = px.sunburst(
    data_frame=df,
    path=["Category", "Style", "Glassware"], 
    color="Category",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    maxdepth=-1,

)

fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()