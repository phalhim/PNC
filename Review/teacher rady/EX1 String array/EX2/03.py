#3 - Replace banana by Jackfruit

arr = ["banana","Banana","Apple","coconut","mango","coconut"]
res = []
for i in range(len(arr)):
    if arr[i] =="banana" or arr[i] =="Banana":
        arr[i] ="Jackfruit"
    res.append(arr[i])
print(res)