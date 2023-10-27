#4 - Reverse each value in list ['ananab','elppa'...]

arr = ["banana","apple","mango", "Coconut"]
res = []
for i in range(len(arr)):
    result = ""
    for j in range(len(arr[i])):
        result += arr[i][-(j+1)]
    res.append(result)
print(res)