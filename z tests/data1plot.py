import pandas as pd;
import plotly.figure_factory as ff;
import statistics;
import plotly.graph_objects as go;
df = pd.read_csv("data1.csv")
data = df["Math_score"]
mean = statistics.mean(data)
print(mean)
std = statistics.stdev(data)
first_std_start,first_std_end = mean-std,mean+std
s_std_start,s_std_end = mean-(2*std),mean+(2*std)
t_std_start,t_std_end = mean-(3*std),mean+(3*std)
fig = ff.create_distplot([data],["when given i-pad"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_start,first_std_start],y=[0,0.17],mode="lines",name="Standard deviation"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="Standard deviation"))
fig.add_trace(go.Scatter(x=[s_std_start,s_std_start],y=[0,0.17],mode="lines",name="Standard deviation"))
fig.add_trace(go.Scatter(x=[s_std_end,s_std_end],y=[0,0.17],mode="lines",name="Standard deviation"))
fig.add_trace(go.Scatter(x=[t_std_start,t_std_start],y=[0,0.17],mode="lines",name="Standard deviation"))
fig.add_trace(go.Scatter(x=[t_std_end,t_std_end],y=[0,0.17],mode="lines",name="Standard deviation"))
fig.show()
