#3 - replace numebr > 3 with 0
arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]
for i in range(len(arr)):
    if arr[i]==3:
        arr[i] =0
print(arr)
