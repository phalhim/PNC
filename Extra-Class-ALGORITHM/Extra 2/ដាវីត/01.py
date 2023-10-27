#1 ,​ បញ្ខូល array​ មួយបន្ទាប់មកបូកលលខទាំងអស់លៅកនុង array Ex: input [2,3,4,5,6]
def sum1(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum1(arr[1:])
 
arr = eval(input("Enter have number: "))
print(sum1(arr))
          