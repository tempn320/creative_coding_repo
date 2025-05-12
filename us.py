import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#### INTERACTIVE PLOTS WITH PLOTLY ####


### BAR CHART ###

df = pd.read_csv("us_data.csv")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = df['Year'],
    y = df['Local jail'],
    mode= 'lines',
    name = "Local jail",

    line =dict(
        color = 'green'
    )
))    

fig.add_trace(go.Scatter(
    x = df['Year'],
    y = df['State & federal prisons'],
    mode= 'lines',
    name = "State & federal prisons",

    line =dict(
        color = 'blue'
    )
))    

fig.update_layout(title='U.S. Incarceration Over Time',
                  xaxis_title='Year',
                  yaxis_title='Total Incarceration',
                  legend_title='Type of Incarceration')

fig.show()

# fig = px.bar(
#     top_attack_pokemon, 
#     x="Name", 
#     y="Attack", 
#     color="Type 1",  
#     title="Top 10 Pokémon with Highest Attack",
#     labels={"Attack": "Attack value", "Name": "Pokemon"},
# )

# fig.show()












