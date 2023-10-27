# userarrays =['banana','cococnut','mango']
# x =userarrays[]
# for i in range(len(userarrays)):
#     x += userarrays[i]
#     # x.append(userarrays)
# print(x)


# grid =[0,1,0,0,0]
# index =0
# for i in range(len(grid)):
#     if grid[i] == 1:
#         index = i
# word =input()
# for char in word:
#     if char =="R":
#         grid[index] = 0
#         grid[index + 1] = 1
#         index +=1
#     else:
#         grid[index] = 0
#         grid[index - 1] = 1
#         index +=1

# print(grid)


# position = [1, 0, 0, 0, 0 ]
# text = input("We need one character to move the position of snake to right (R) :")

# sumOfR = 0
# sumOfL = 0
# for i in range(len(text)):
#     if text[i].upper() == "R":
#         sumOfR += 1
#     elif text[i].upper() == "L":
#         sumOfL += 1

# if sumOfR > sumOfL :
#     times = sumOfR -sumOfL
#     for i in range(len(position)):
#         if position[i] == 1 :
#             position[i] = 0
#             if times < 5 :
#                 position[times + 1] = 1
#             else:
#                 position[len(position)-1] = 1
# elif sumOfL > sumOfR:
#     times = sumOfL-sumOfR
#     for i in range(len(position)):
#         if position[i] == 1 :
#             position[i] = 0
#             if times < 2 :
#                 position[i - 1] = 1
#             else:
#                 position[0] = 1
# print(position)




# texts =['banana','cococnut','mango']
# result =[]
# for i in range(len(texts)):
#     result += texts[i]
# print(result)


arr1 = [[1,2,3],[4,5,6]]
arr2 = [[1,2,3],[4,5,6]]
res = "unequal"
if len(arr1)==len(arr2):
    res = "equal"
    for i  in range(len(arr1)):
        if len(arr1[i]) == len(arr2[i]):
            j = 0
            while res != "unequal" and j < len(arr1[i]):
                if arr1[i][j]==arr2[i][j]:
                    res = "equal"
                else:
                    res = "unequal"
                j+=1
        else:
            res = "unequal"
print(res)
