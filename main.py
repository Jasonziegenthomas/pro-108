import csv 
import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv('data.csv')
fig = ff.create_distplot([df['Mobile Brand'].tolist()],['Height'],show_hist=False)
fig = ff.create_distplot([df['Avg Rating'].tolist()],['Weight'],show_hist=False)
fig.show()
