a = eval(input("Enter fo number array: " ))
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]== 7:
            a[i][j] = 8
print(a)