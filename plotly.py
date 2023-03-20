import plotly.graph_objs as go

data = [("Mark", 1000),
        ("John", 1500),
        ("Daniel", 2300),
        ("Greg", 5000)]

x_values = [x[0] for x in data]
y_values = [x[1] for x in data]

fig = go.Figure(data=go.Bar(x=x_values, y=y_values))