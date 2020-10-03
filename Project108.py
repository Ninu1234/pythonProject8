import pandas as pd
import plotly.figure_factory as ff 
import csv 
df = pd.read_csv('project108.csv')
averagerating = df['Avg Rating'].tolist()
fig = ff.create_distplot([averagerating],['Avg Rating'],show_hist = False)
fig.show()