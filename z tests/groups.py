import pandas as pd;
import plotly.figure_factory as ff;
import plotly.graph_objects as go;
import csv;
import random;
import statistics;
df = pd.read_csv("data1.csv")
data = df["Math_score"]
mean_of_sample = statistics.mean(data)
print(mean_of_sample)
std = statistics.stdev(data)
print(std)
def random_mean(counter):
    data_set = []
    for x in range(0,counter):
        rand_index = random.randint(0,len(data)-1)
        random_index = data[rand_index]
        data_set.append(random_index)
    mean = statistics.mean(data_set)
    return mean
def show_figure(means_list):
    mean = statistics.mean(means_list)
    print(mean)
    std = statistics.stdev(means_list)
    first_std_start,first_std_end = mean-std,mean+std
    s_std_start,s_std_end = mean-(2*std),mean+(2*std)
    t_std_start,t_std_end = mean-(3*std),mean+(3*std)
    fig = ff.create_distplot([means_list],["when given i-pad"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
    fig.add_trace(go.Scatter(x = [mean_of_sample,mean_of_sample],y=[0,0.17],mode="lines",name="mean of sample"))
    fig.add_trace(go.Scatter(x=[s_std_end,s_std_end],y=[0,0.17],mode="lines",name=" sec Standard deviation end"))
    fig.add_trace(go.Scatter(x=[t_std_end,t_std_end],y=[0,0.17],mode="lines",name=" third Standard deviation end"))
    fig.show()

def setup():
    means_list = []
    for x in range(0,1000):
        lists = random_mean(100)
        means_list.append(lists)
    show_figure(means_list)

setup()