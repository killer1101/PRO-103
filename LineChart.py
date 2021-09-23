import pandas as pd
import plotly.express as px

df = pd.read_csv("CopyData.csv")
fig = px.scatter(df, x="cases", y="date", color="country", title='Per Capita Income')
fig.show()
