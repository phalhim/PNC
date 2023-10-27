
array01 =[2,4,3,2,5]
array02 =[2,8,3,9,5]
result1numbers = []
result2numbers = []
for i in range(len(array01)):
    if array01[i]%2==0:
        result1numbers.append(array01[i])
print(result1numbers)
for j in range(len(array02)):
    if array02[j] %2 !=0:
        result2numbers.append(array02[j])
print(result2numbers)
