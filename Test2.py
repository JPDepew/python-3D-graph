import plotly.plotly as py
import plotly.graph_objs as go
import plotly


import pandas as pd

plotly.tools.set_credentials_file(username='jpdepew', api_key='tHBUsofzHSeHQTHe2N1O')

# Read data from a csv
z_data = pd.read_csv('thing.csv')

data = [
    go.Surface(
        z=z_data.as_matrix()
    )
]

for x in data[0]:
    print(data[0])

layout = go.Layout(
    title='Mt Poopo Elevation',
    autosize=False,
    width=1000,
    height=1000,
    margin=dict(
        l=5,
        r=100,
        b=100,
        t=100
    )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='elevations-3d-surface')