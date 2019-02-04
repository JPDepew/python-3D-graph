from urllib.request import OpenerDirector

import jgraph as jg
import json
import urllib

data = []
req = urllib.request.Request("https://raw.githubusercontent.com/plotly/datasets/master/miserables.json")
opener: OpenerDirector = urllib.request.build_opener()
f = opener.open(req)

data = json.loads(f.read())
N = len(data['nodes'])

Edges = [(data['links'][k]['source'], data['links'][k]['target']) for k in range(N)]

print(N)

print(data.keys())
