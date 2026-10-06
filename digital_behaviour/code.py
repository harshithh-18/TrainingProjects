import csv

APP_NAME="Instagram"
minutes=[]
with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))

minutes= minutes[-7:]

total=sum(minutes)        
avg=total/len(minutes)
maximum=max(minutes)
minimum=min(minutes)

counter=0
for val in minutes:
    if val>avg:
        counter+=1

print(f"App: {APP_NAME}  Days: {len(minutes)}  Total: {total}  Lowest: {minimum}  Highest: {maximum}  Average: {avg}  Above Average: {counter}")

