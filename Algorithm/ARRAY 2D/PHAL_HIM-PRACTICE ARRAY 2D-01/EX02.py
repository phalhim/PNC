arr =[[50,20,40],[80,90,20],[40,49,88]]
for i in range(len(arr)):
    result =0
    for j in range(len(arr[i])):
        if arr[i][j] < 50:
            result+=1
    print("Student in row number "+ str(i)+ " fail " + str(result) + " subject")
