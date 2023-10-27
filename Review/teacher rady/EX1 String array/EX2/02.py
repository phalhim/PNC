#2 - How many letter "o" in list

# រៀបជាចំនួន​ "o" គិតជាលេខ--------------------------------------------------------------------
# arr = ["banana","Banana","Apple","coconut","mango","coconut"]
# res =0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] =="o":
#             res +=1
# print(res)


#រៀបចំនួន 'o' មួយពាក្យៗ​ ហើយចេញជាអារេ-----------------------------------------------
arr = ["banana","Banana","Apple","coconut","mango","coconut"]
res = []
for i in range(len(arr)):
    resultForarray = 0
    for j in range(len(arr[i])):
        if arr[i][j] =="o":
            resultForarray +=1
    res.append(resultForarray)
print(res)