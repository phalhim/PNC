#Counter letter output:{'a': 4, 'o': 3}
input1= ['banana','coconut','mango']
input2= ['a','o']
def counterarray(arr,val):
    dic = {}
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] ==val:
                count += 1
    return count
res = {}
for each in input2:
    res[each]=counterarray(input1,each)
print(res)

