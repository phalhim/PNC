# arr = [["0","*","0","0","0"],
#        ["0","0","0","0","0"],
#        ["0","0","0","0","0"],
#        ["0","0","0","0","0",],
#        ["0","0","0","0","0"]]


# def instar(arr):
#     index =0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j] =="*":
#                 index = j                
#     return index
# def instarow(arr):
#     row = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j] =="*":
#                 row = i                
#     return row
# text = input()
# for each in text:
#     if each.upper()=="R":
#         row = instarow(arr)
#         index = instar(arr)
#         arr[row][index]="0"
#         arr[row][index+1]="*"
#     elif each.upper()=="L":
#         row = instarow(arr)
#         index = instar(arr)
#         arr[row][index]="0"
#         arr[row][index-1]="*"
#     elif each.upper()=="D":
#         row = instarow(arr)
#         index = instar(arr)
#         arr[row][index]="0"
#         arr[row+1][index]="*"
#     elif each.upper()=="U":
#         row = instarow(arr)
#         index = instar(arr)
#         arr[row][index]="0"
#         arr[row-1][index]="*"
# print(arr)



grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, "*", 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

grid[1]
def getPositionCaptian(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if str(grid[row][col]) == "*":
                return [row, col]

startGame = True
print(grid)
while startGame:
    positionCaptain = getPositionCaptian(grid)
    row = positionCaptain[0]
    col = positionCaptain[1]
    moveCaptain = input("L/R/D/U: ")
    if moveCaptain == "L" and col > 0:
        grid[row][col] = 0
        grid[row][col - 1] = "*"
    elif moveCaptain == "R" and col < len(grid[0])-1:
        grid[row][col] = 0
        grid[row][col + 1] = "*"
    elif moveCaptain == "U" and row > 0:
        grid[row][col] = 0
        grid[row - 1][col] = "*"
    elif moveCaptain == "D" and row  < len(grid) -1:
        grid[row][col] = 0
        grid[row + 1][col] = "*"
    
    print(grid)
    term = input("do you want to stop? Y/N")
    if term == "Y":
        startGame = False