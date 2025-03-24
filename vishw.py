import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("2020nyc_incarceration_rates.csv")

### GUIDING QUESTIONS ###
# What are the 10 neighborhoods with the highest incarceration rates?
# What are the 10 neighborhoods with the lowest incarceration rates?
# Is there a trend between incarceration rates and total population?

### BAR CHART 1 ###

# top_nta_incrates = df.nlargest(10, "Imprisonment rate per 100,000")

# fig = px.bar(
#     top_nta_incrates, 
#     x="NTA\xa0", 
#     y="Imprisonment rate per 100,000", 
#     color="NTA code, 2020",  
#     title="Top 10 NYC Neighborhoods with Highest Incarceration Rates",
#     labels={"Incarceration Rate": "Attack value", "Neighborhood": "Pokemon"},
# )

# fig.show()

### BAR CHART 2 ###

# low_nta_incrates = df.nsmallest(10, "Imprisonment rate per 100,000")

# fig = px.bar(
#     low_nta_incrates, 
#     x="NTA\xa0", 
#     y="Imprisonment rate per 100,000", 
#     color="NTA code, 2020",  
#     title="10 NYC Neighborhoods with Lowest Incarceration Rates",
#     labels={"Incarceration Rate": "Rate Value", "Neighborhood": "NTA"},
# )

# fig.show()

### SCATTER PLOT ###

# fig = px.scatter(df, x="Total population, 2020", y="Imprisonment rate per 100,000", color="NTA\xa0",
#                 hover_name="NTA\xa0", title="Neighborhood (NTA) Imprisonment rate per 100,000 vs. Total Population")

# fig.show()
