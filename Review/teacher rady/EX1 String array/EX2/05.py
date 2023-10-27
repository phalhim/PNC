#5 - Create new list store only letter "A" and "C" from list

arr = ["banana","Banana","Apple","coconut","mango","coconut"]
res = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (arr[i][j]=="A" or arr[i][j]=="a") or (arr[i][j]=="C" or arr[i][j]=="c") :
            if (arr[i][j] not in res):
                res.append(arr[i][j])
print(res)