number = "12345"
n=0
for i in range(len(number)):
    if int(number[i]) %2 ==0:
        n += int(number[i])
print(n)