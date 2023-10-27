#Find the maximum element in a 2D array.
arr =[[90],[80]]
minimumForArr = arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]>minimumForArr:
            minimumForArr = arr[i][j]
print(minimumForArr)