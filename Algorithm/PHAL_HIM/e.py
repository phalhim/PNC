# print(len("45"))
# print(len([45]))
# print( len("ronan, pnc") )
# print( len( ["ronan","pnc"] ) )



# array = [1, 2, 3, 4, 5]
# for index in range(len(array)):
#     value = array[index]
#     print("hello " + str(value))


# array = [1, 2, 3, 4, 5]
# for value in array:
#     print("hello " + str(value))




# list1 = [5, 4, 7, 3, 1]
# list2 = list1

# list1[0] = 99

# print(list1[0])
# print(list2[0])



# a = 5
# b = a
# a = 7
# print(b)


# a = [18,24]
# b = a
# a[1]=3
# print(b[1])

#8/30/2023---------------------------------------------------------
# a =[[1,2,3],[4,5,6]]
# print(a[1])

# a = [[1,2,3],[4,5,6]]
# x = ""
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         x+= str(a[i][j])
# print(x)


# a = [[1,2,3],[4,5,6]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])


# a = [[1,2,3],[4,5,6]]
# x = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         x+= int(a[i][j])
# print(x)





a = [[5,3,8,4],[3,8,7,1],[1,4,6,3]]
for i in range(len(a)):
    for j in range(len(a[i])):
        if j == 7:
            print(a[1][2])