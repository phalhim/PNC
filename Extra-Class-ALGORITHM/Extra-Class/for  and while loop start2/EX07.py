number ="12345678"
result =0
for i in range(len(number)):
    if int(number[i]) % 2 ==0 and int(number[i]) <6:
        result += int(number[i])
print(result)