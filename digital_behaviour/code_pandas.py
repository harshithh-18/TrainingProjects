import pandas as pd
df =pd.read_csv("digital_b.csv")
print(df.head(5))
print(df.tail(5))
print(df.shape) 
print(df.columns)
print(df.describe())
print(df[["Date","Instagram_Minutes"]].head(5))
print(df["Study_Minutes"].mean())
print(df["Study_Minutes"].mean().round(2))
print(df["YouTube_Minutes"].max())
print(df["YouTube_Minutes"].min())
print(df[df["Instagram_Minutes"] > 100])
print(df["Study_Minutes"].max())
print(df.sort_values("Instagram_Minutes", ascending=False).head(5))


df["total_screen_time"] = df["Instagram_Minutes"] + df["YouTube_Minutes"] + df["WhatsApp_Minutes"] + df["LinkedIn_Minutes"] 
print(df["total_screen_time"])
print("Total Hours spent", df["total_screen_time"].sum()/60)
df["Digital_balance"]=df["Study_Minutes"]/df["total_screen_time"] 
print(df["Digital_balance"].round(2))
y = df.loc[df["Study_Minutes"].idxmax(), "Date"]
print(y)
df["day_type"]="normal"
df.loc[df["total_screen_time"]>300,"day_type"]="heavy"
print(df)
x=df[df["day_type"]=="heavy"].shape[0]
print(x)

z = df.loc[df["total_screen_time"].idxmax(), "Study_Minutes"]

print(z)
print(df["Digital_balance"].mean())
print(df["Digital_balance"].sum()/len(df["Digital_balance"]))
df.to_csv("my_analysis.csv")