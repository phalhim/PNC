number =int(input())
result =0
for i in range(len(number)-1):
    if int(number[i]) ==20:
        cuont ="WON"
        result+=1
    if int(number[i]) >20:
        count ="LOST"
print(result)
