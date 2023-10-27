a = [[1,2,3],[4,5,6],[7,8,9]]
x = 0
y = []
for i in range(len(a)):
    for j in range(len(a)):
        x += a[j][i]
    y.append(x)
    x =0
for i in range(len(y)):
    print(y[i],end=" ")
