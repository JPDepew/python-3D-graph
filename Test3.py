# Get this figure: fig = py.get_figure("https://plot.ly/~ehernan/0/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~ehernan/0/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="plot from API", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~ehernan/0/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
import random
import csv

### I had to create a plotly account and use the credentials to use the graphing. ###
py.sign_in('jpdepew', 'tHBUsofzHSeHQTHe2N1O')

# Setting up some sort of data object thing

class Node(object):
    x = 0.0
    y = 0.0
    z = 0.0
    name = ""
    parent = None
    left = None  # Node object or None
    right = None  # Node object or None
# END Node


root = Node()

x = []
y = []
z = []
cities = []

# Lets see if we can import stuff from a csv file
with open('worldcities.csv', newline='') as csvfile:
    thingo = csv.DictReader(csvfile)
    counter = 0
    for row in thingo:
        #print(row['city'], row['lat'], row['lng'])
        cities.append(row['city'])
        x.append(row['lat'])
        y.append(row['lng'])
        z.append(random.uniform(0, 1.0))
        counter += 1
        if counter > 500:
            print("Limit", counter - 1, "reached")
            break

# Below are the two traces that make up the graph. One is for lines, and one is for dots.
# They have data points in the x, y and z positions to make up the graphs

layout = {
    "annotations": [
        {
            "x": 0,
            "y": 0.1,
            "font": {"size": 14},
            "showarrow": False,
            "text": "3d",
            "xanchor": "left",
            "xref": "paper",
            "yanchor": "bottom",
            "yref": "paper"
        }
    ],
    "height": 1000,
    "hovermode": "closest",
    "margin": {"t": 100},
    "scene": {
        "xaxis": {
            "showbackground": False,
            "showgrid": False,
            "showline": False,
            "showticklabels": False,
            "title": "x axis",
            "zeroline": False,
            "range": [20, 50]
        },
        "yaxis": {
            "showbackground": False,
            "showgrid": False,
            "showline": False,
            "showticklabels": False,
            "title": "y axis",
            "zeroline": False,
            "range": [75, 130]
        },
        "zaxis": {
            "showbackground": False,
            "showgrid": False,
            "showline": False,
            "showticklabels": False,
            "title": "z axis",
            "zeroline": False,
            "range": [-15, 15]
        }
    },
    "showlegend": False,
    "title": "3D visualization",
    "width": 1920
}


counterdude = 0

# initializes a list of nodes to the length of the cities array
def create_list(temp_node, length):
    global counterdude
    if counterdude < len(cities):
        n1 = Node()
        n1.parent = temp_node

        n2 = Node()
        n2.parent = temp_node

        temp_node.left = n1
        temp_node.right = n2
        temp_node.x = x[counterdude]
        temp_node.y = y[counterdude]
        temp_node.z = z[counterdude]
        temp_node.name = cities[counterdude]
        print(temp_node.name)

        counterdude += 1
        create_list(temp_node.left, length)
        create_list(temp_node.right, length)
# END create_list


# Prints the list in order. I think this is working, since root
# is printed right in the middle with values 0, 0
def in_order(temp_node):
    if temp_node is not None:
        in_order(temp_node.left)
        print("(", temp_node.x, ",", temp_node.y, ")")
        in_order(temp_node.right)
# END in_order


def assign_nodes(temp_node, i):
    if temp_node is not None:
        x.append(temp_node.x)
        y.append(temp_node.y)
        z.append(temp_node.z)

        i += 1

        assign_nodes(temp_node.right, i)
        assign_nodes(temp_node.left, i)
# END assign_nodes


# ============= CREATE THE ACTUAL LIST AND ASSIGN NODES ===================== #
create_list(root, 30)
print(root.x, root.right.x, root.right.parent.x)
#assign_nodes(root, 0)

trace3 = go.Scatter3d(
    x=x,
    y=y,
    z=z,

    hoverinfo="text",
    marker={
        "color": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 4, 0, 2, 3, 2, 2, 2,
                  2, 2, 2, 2, 2, 4, 6, 4, 4, 5, 0, 0, 7, 7, 8, 5, 5, 5, 5, 5, 5, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9,
                  4, 4, 4, 4, 5, 10, 10, 4, 8],
        "colorscale": "Viridis",
        "line": {
            "color": "rgb(50,50,50)",
            "width": 0.5
        },
        "size": 6,
        "symbol": "circle"
    },
    mode="markers",
    name="actors",
    text=cities
)

trace4 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    hoverinfo="none",
    line={
        "color": "rgb(125,125,125)",
        "width": 1
    },
    mode="lines"
)

# Creating the figure
fig = Figure(data=[trace3], layout=layout)
#plot_url = py.plot(fig)