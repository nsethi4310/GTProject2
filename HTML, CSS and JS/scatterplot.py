# x and y given as dataframe columns
import plotly.express as px
import pandas as pd 
import chart_studio.plotly as py
import plotly.graph_objects as go

data= pd.read_csv("https://raw.githubusercontent.com/nsethi4310/GTProject2/main/csv/us_state_data.csv")

fig = go.Figure(data=go.Scatter(x=data['abbr'],
                                y=data['yearly_barrels'],
                                mode='markers',
                                marker=dict(
                                        size=16,
                                        color=data['yearly_barrels'], 
                                        colorscale='Plotly3', 
                                        showscale=True),
                                text=data['state'])) 
