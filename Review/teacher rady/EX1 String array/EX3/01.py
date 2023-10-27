#arr = ["banana","apple","mango", "Coconut"]
#1 - How many letter of each value[6,5,5,7]


arr = ["banana","apple","mango", "Coconut"]
res = []
for i in range(len(arr)):
    result=0
    for j in range(len(arr[i])):
        result +=1
    res.append(result)
print(res)