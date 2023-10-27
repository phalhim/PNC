#Find the average of all elements in a 2D array.
arr =[[1,2,5],[1,9,3]]
result = 0
x =0
for i in range(len(arr)):
    number = arr[i]
    for n in range(len(number)):
        result+= (number[n])
    x = result / number[i]
print(x)