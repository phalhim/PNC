number = "1234"
i = 0
sum =0
while i < len(number):
    if int(number[i]) % 2 ==0:
        sum += int(number[i])
    i +=1
print(sum)