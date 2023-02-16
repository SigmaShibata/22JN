import csv
import random

namelist = []
with open("user_sample.csv", encoding="utf-8") as f:
    csvlist = csv.reader(f)
    for row in csvlist:
        if len(row) == 0 or len(row[0]) != 8:
            continue
        namelist.append(row[0] + "　　　" + row[1] + "　　　" + row[2])

random.shuffle(namelist)

for name in namelist:
    input("次の質問に答えてもらう人は？？？ -->")
    print()
    print(name)
    print()