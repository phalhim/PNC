array =[11,3,4,32,3]
result = []
for i in range(len(array)):
    if len(str(array[i])) ==1:
        result.append(array[i])
print(result)