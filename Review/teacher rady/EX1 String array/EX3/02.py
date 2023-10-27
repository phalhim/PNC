#2 - How many "A" letter of each value [3,1,1, 0]


arr = ["banana","apple","mango", "Coconut"]
res = []
for i in range(len(arr)):
    result=0
    for j in range(len(arr[i])):
        if arr[i][j] =="a":
            result +=1
    res.append(result)
print(res)