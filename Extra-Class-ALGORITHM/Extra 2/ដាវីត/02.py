# , បញ្ចូល array មួយបន្ទាប់មកចាប់លលខគូេលៅកនុង array បន្ទប់មកយកលៅបូក Ex: input [1,2,3,4,5,6,7,8]
arr =[1,2,3,4,5,6,7,8]
result = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        result += arr[i]
print(result)