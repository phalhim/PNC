array =[
{'name':' dyna',' subject':' Algorithm',' score':10},
{'name':' sokheang',' subject':' Html',' score':45},
{'name':' sreynang',' subject':' Algorithm',' score':89},
{'name':' phanit',' subject':' Algorithm',' score':49},
]
res = {}
def arrayDictionary(arrays):
    for i in range(len(arrays)):
        for j in range(len(array[i])):
            if array[j]["name"] =="dyna" and array[j]["name"]=="phanit":
                res =array[i][j]
    return res
print(arrayDictionary(res))