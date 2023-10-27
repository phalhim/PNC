#Count number
#Output: [ { 2: 4} , {3: 2} ]

input1= [2, 2, 3, 5, 2, 3, 2, 5, 8]
input2= [2, 3]
def numcheck(arr,val):
    dic  = {}
    count= 0 
    for i in range(len(arr)):
        if arr[i]==val:
            count+=1
            dic[arr[i]]=count
    return dic
res = []
for each in input2:
    res.append(numcheck(input1,each))
print(res)

