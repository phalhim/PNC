arr = ["0","*","0","0","0"]
def indexstar(arr):
    index = 0
    i = 0
    while i<len(arr) and arr[i]!="*":
        i+=1
    index = i
    return index
star = indexstar(arr)
arr[star] = 0
arr[star+1] ="*"
print(arr)


#------------2----------------
grit =[0,"*",0,0,0]
index=0
for i in range(len(grit)):
    if str(grit[i]) == "*":
        grit[i] =0
        index =i
