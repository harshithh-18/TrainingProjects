import csv
import numpy as np

APP_NAME="Instagram"
insta_list=[]
study_time=[]
with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_list.append(int(row["Instagram_Minutes"]))
        study_time.append(int(row["Study_Minutes"]))

insta_ar=np.array(insta_list[:7])
study_ar=np.array(study_time[:7])

total=insta_ar.sum()
average=insta_ar.mean()
maximum=insta_ar.max()
minimum=insta_ar.min()


print(f"App: {APP_NAME}  Days: {(insta_ar).size}  Total: {total}  Lowest: {minimum}  Highest: {maximum}  Average: {average}")

print(insta_ar[0])

print(insta_ar[-1])

print(insta_ar[2])

print(insta_ar[:3])

print(insta_ar[-2:])

print(insta_ar[1:4])

hours = insta_ar/60
print(hours)

difference = study_ar - insta_ar
print(difference)

above_hundred = insta_ar > 100
print(above_hundred)

print(insta_ar[above_hundred])

count_above_100 = np.sum(above_hundred)
print(count_above_100)

above_average = insta_ar > average
print(insta_ar[above_average])
