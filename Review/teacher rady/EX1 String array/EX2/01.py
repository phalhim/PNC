#arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]
#1 - How many banana in list

arr = ["banana","Banana","Apple","coconut","mango","coconut"]
res =0
for i in range(len(arr)):
    if arr[i] =="banana" or arr[i] =="Banana":
        res += 1
print(res)