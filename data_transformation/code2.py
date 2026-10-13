import numpy as np
import pandas as pd

df = pd.read_csv('data_transformation/datatransformation.csv')
apps = np.array(["Chat","Video","Study","Games"])
# apps = np.array(df.columns)

arr = df[apps].to_numpy()

print(arr)

print(arr.shape)

per_app = arr.sum(axis=0)
per_day = arr.sum(axis = 1)

print(arr[:7])

per_app_average = np.round(arr.mean(axis = 0),1)

winners = apps[arr.argmax(axis=1)]

values, freq = np.unique(winners, return_counts=True)

print(dict(zip(values,freq.tolist())))  

shares = arr/per_day[:,None]*100

per_app_max=arr.max(axis=0)
share=arr/per_app_max[None,:]


weekend=(df['Day']%7==6)| (df['Day']%7==0)
print(df[weekend].mean(axis=0))
print(df[~weekend].mean(axis=0))


#single busiest day of the month and how many minutes it held.
print(per_day.argmax()+1, per_day.max())




























