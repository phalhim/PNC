arr = [[0,0,0],[0,3,0],[0,3,0]]
x = []
for i in range (len(arr)):
    x =[]
    for j in range(len(arr[i])):
        if arr[i][j]== 3 : 
           x.append(i)
           x.append(j)
    print(x)