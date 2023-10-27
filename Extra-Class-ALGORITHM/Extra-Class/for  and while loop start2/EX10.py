number = "12345678"
result =0
sum = 0
while result < len(number):
    if int(number[result]) % 2 !=0 and int(number[result])<5:
        sum += int(number[result])
    result +=1
print(sum)
    