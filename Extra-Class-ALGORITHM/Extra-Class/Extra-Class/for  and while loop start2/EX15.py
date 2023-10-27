number = "123456789"
result =0
for i in range(len(number)):
    if int(number[i]) %2 == 0 and int(number[i]) >=5 and int(number[i]) <= 9:
        result += int(number[i])
print(result)
        