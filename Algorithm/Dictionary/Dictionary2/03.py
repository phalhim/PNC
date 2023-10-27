di = [{"name": "Bunthoeun","score": 90},
    {"name": "Kunthy","score": 75},
    {"name": "Sreymom","score": 95}
]
count=0
for i in range(len(di)):
    if di[i]<=75:
        count+=1

print(count)
        