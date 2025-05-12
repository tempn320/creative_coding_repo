import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#### INTERACTIVE PLOTS WITH PLOTLY ####


### BAR CHART ###

df = pd.read_csv("women_totalinc.csv")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = df['Year'],
    y = df['Total Women'],
    mode= 'lines',

    line =dict(
        color = 'blue'
    )
)    
) 

fig.update_layout(
    title='Women Incarceration Over Time',
    xaxis_title='Year',
    yaxis_title='Total Incarceration',
    yaxis=dict(
    tick0=0, 
        dtick=20000))

                  

fig.show()