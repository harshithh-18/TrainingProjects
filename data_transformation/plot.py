import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
apps = ["Chat", "Video", "Study", "Games"]
df = pd.read_csv("data_transformation/datatransformation.csv")
usage=df[apps].to_numpy()
days=df["Day"].to_numpy()
per_day=usage.sum(axis=1)
shares=usage/per_day[:,None]*100
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(11,8))
for i,app in enumerate(apps):
    ax1.plot(days,usage[:,i],marker="o",markersize=3,linewidth=1.6,label=app)
fig.savefig("data_transformation/usage.png")    