#Reverse Object output: {1: 'ananab', 2: 'ognam', 3: 'tunococ'}
# input= {1: 'banana', 2: 'mango', 3: 'coconut'}


# X = int(input())
# while X != 5:
#     print ('try again')
#     X = int(input())
# print(X)

# text = "ronan"
# print(text[:-2] )


fruits = ['apple', 'banana']
# res=fruits[1]
# print(res)

# fruits.insert(1, 'coconut')
# print(fruits)
# fruits.append('mango')

# fruits = ['apple', 'banana']
# fruits.pop(1)
# print(fruits)

# fruits=['a', 'b', 'c', 'd']
# res=fruits[0:4]
# print(res)



arr=['banana','coconut','mango']
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]=="a":
            arr[i][j] ="*"
print(arr)
        # else:
        #     res +=arr[i][j]
    # res.append(result)
    # res=''
# print(res)