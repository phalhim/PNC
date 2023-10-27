#Find the sum of all elements in a 2D array.
arr =[[1,2,3],[1,2,3]]
result = 0
for i in range(len(arr)):
    number = arr[i]
    for n in range(len(number)):
        result+= (number[n])
print(result)

