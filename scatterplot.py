# x and y given as dataframe columns
import plotly.express as px
import pandas as pd 
import chart_studio.plotly as py
import plotly.graph_objects as go

data= pd.read_csv("https://raw.githubusercontent.com/nsethi4310/GTProject2/main/csv/us_state_data.csv")

fig = go.Figure(data=go.Scatter(x=data['abbr'],
                                y=data['breweries'],
                                mode='markers',
                                marker=dict(
                                        size=16,
                                        color=data['breweries'], 
                                        colorscale='Plotly3', 
                                        showscale=True),
                                text=data['state'])) 


fig.update_layout(title='States vs. Number of Breweries')
fig.show()

fig.write_html('scatterplot.html',
                full_html=False,
                include_plotlyjs='cdn')

#py.plot(fig, filename = 'scatterplot', auto_open=True)


