import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("digital_behaviour/digital_behaviour.csv")

df["Day_Label"]=[f"D{i+1}" for i in range(len(df))]
df['Screen Time'] = (
    df['Instagram_Minutes']
    + df['YouTube_Minutes']
    + df['WhatsApp_Minutes']
    + df['LinkedIn_Minutes']
)
plt.figure(figsize=(9, 6))
plt.bar(df['Day_Label'], df['Screen Time'], color="#993300")
plt.title("My Screen Time by Day")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.tight_layout()
plt.xticks()
plt.legend(["Screen Time"])
plt.savefig("digital_behaviour/screen_time_by_day.png")



plt.figure()
app_names = ["Instagram", "YouTube", "WhatsApp", "LinkedIn"]
app_totals = [
    sum(df['Instagram_Minutes']),
    sum(df['YouTube_Minutes']),
    sum(df['WhatsApp_Minutes']),
    sum(df['LinkedIn_Minutes'])
]
plt.bar(app_names, app_totals)
plt.title("Total Time by App")
plt.xlabel("App")
plt.ylabel("Minutes")
plt.savefig("digital_behaviour/total_time_by_app.png")



plt.figure()
plt.plot(df['Day_Label'], df['Study_Minutes'],marker="o", label="Study Minutes",color="green")
plt.plot(df['Day_Label'], df['Screen Time'],marker="o", label="Screen Time",color="blue")
plt.title("Study vs Screen Time")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.xticks(rotation=45)
plt.legend()
plt.savefig("digital_behaviour/study_vs_screen_time.png")



plt.figure()
plt.pie(
    app_totals,
    labels=app_names,
    autopct="%.1f%%",startangle=90,colors=["#6500F3", "#A024FF", "#CD88FA", "#FF00E1"]
)
plt.title("Share of App Time")
plt.savefig("digital_behaviour/share_of_app_time.png")