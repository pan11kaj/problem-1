import csv;
import pandas as pd;
import plotly.figure_factory as ff;
import statistics;
df = pd.read_csv("data.csv")
data = df["Math_score"]
fig = ff.create_distplot([data],["Math numbers"],show_hist = False)
fig.show()
mean = statistics.mean(data)
std = statistics.stdev(data)
print(mean,std)

