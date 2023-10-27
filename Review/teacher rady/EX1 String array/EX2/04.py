#4 - Create new list with unique fruit

arr = ["banana","Banana","Apple","coconut","mango","coconut"]
res = []
for i in range(len(arr)):
    if arr[i].lower() not in res:
        res .append(arr[i])
print(res)