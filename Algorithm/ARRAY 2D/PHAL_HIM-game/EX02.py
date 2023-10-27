# arr = ["0","*","0","0","0"]
# def indexstar(arr):
#     index = 0
#     i = 0
#     while i<len(arr) and arr[i]!="*":
#         i+=1
#     index = i
#     return index
# star = indexstar(arr)
# arr[star] = 0
# arr[star-1] ="*"
# print(arr)

#------------"2"-----------------------------------------------------------------

grid = [0, "*", 0, 0, 0]
def getPositionCaptain(grid):
    for i in range(len(grid)):
        if str(grid[i]) == "*":
            return i
startGame = True
while startGame:
    positionCaptain = getPositionCaptain(grid)
    moveCaptain = input("L/R: ")
    if moveCaptain == "L" and positionCaptain > 0:
        grid[positionCaptain] = 0
        grid[positionCaptain - 1] = "*"
    elif moveCaptain == "R" and positionCaptain < len(grid)-1:
        grid[positionCaptain] = 0
        grid[positionCaptain + 1] = "*"
    print(grid)
    term = input("Do you want to stop? Yes/No: ")
    if term =="Yes":
        startGame =False