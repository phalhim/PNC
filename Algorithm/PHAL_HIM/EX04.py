number =int(input())
count=""
for i in range(number):
    if number[i] !=68:
        count ="ENTER NUMBER AGAIN"
    if number[i]== 68:
        count="YOU WON"
    else: 
        number[i]!=68 and number[i+1]!=68 and number[i+2]!=68
        count="YOU LOST"
print(count)