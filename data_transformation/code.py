import pandas as pd
import numpy as np

df = pd.read_csv("data_transformation/datatransformation.csv")

Chat = df["Chat"].to_numpy()
Video = df["Video"].to_numpy()
Study = df["Study"].to_numpy()
Games = df["Games"].to_numpy()

print("Length:", len(Chat))


print("Chat total:", Chat.sum())
print("Chat average:", round(Chat.mean(), 1))

print("Video total:", Video.sum())
print("Video average:", round(Video.mean(), 1))

print("Study total:", Study.sum())
print("Study average:", round(Study.mean(), 1))

print("Games total:", Games.sum())
print("Games average:", round(Games.mean(), 1))


study_minus_games = Study - Games

best_day = np.argmax(study_minus_games)
worst_day = np.argmin(study_minus_games)

print("Best day:", best_day + 1)
print("Worst day:", worst_day + 1)


apps = ["Chat", "Video", "Study", "Games"]

for i in range(30):
    day_values = [
        Chat[i],
        Video[i],
        Study[i],
        Games[i]
    ]

    largest_position = np.argmax(day_values)

    print("Day", i + 1, "largest:", apps[largest_position])


daily_total = Chat + Video + Study + Games

Chat_share = (Chat / daily_total) * 100
Video_share = (Video / daily_total) * 100
Study_share = (Study / daily_total) * 100
Games_share = (Games / daily_total) * 100

print("Chat share:", Chat_share)
print("Video share:", Video_share)
print("Study share:", Study_share)
print("Games share:", Games_share)