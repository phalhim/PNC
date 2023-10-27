#3 - Move banana to last index

arr = ["banana","apple","mango", "Coconut"]
for i in range(len(arr)):
    if arr[i] =="banana" or arr[i] =="Banana":
        arr.append(arr[i])
        arr.pop(i)
print(arr)