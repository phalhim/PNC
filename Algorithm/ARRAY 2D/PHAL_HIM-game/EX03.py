arr = [["0","0","0","0","0"],
       ["0","*","0","0","0"],
       ["0","0","0","0","0"],
       ["0","0","0","0","0",],
       ["0","0","0","0","0"]]

def instar(arr):
    index =0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] =="*":
                index = j  
                              
    return index
def instarow(arr):
    row = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] =="*":
                row = i   
                             
    return row
text = input()
for each in text:
    if each.upper()=="R":
        row = instarow(arr)
        index = instar(arr)
        arr[row][index]="0"
        arr[row][index+1]="*"
    elif each.upper()=="L":
        row = instarow(arr)
        index = instar(arr)
        arr[row][index]="0"
        arr[row][index-1]="*"
    elif each.upper()=="D":
        row = instarow(arr)
        index = instar(arr)
        arr[row][index]="0"
        arr[row+1][index]="*"
    elif each.upper()=="U":
        row = instarow(arr)
        index = instar(arr)
        arr[row][index]="0"
        arr[row-1][index]="*"
print(arr)