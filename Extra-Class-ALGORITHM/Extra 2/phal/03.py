arr =[1,2,3,4,6,7,8]
x =[]
for i in range(len(arr)):
    if arr[i]%2 ==1:
        x.append(arr[i])
print(x)