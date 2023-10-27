number ="123456789"
result = 0
sum =0
while result <len(number):
    if int(number[result]) >=5 and int(number[result])<=9:
        sum += int(number[result])
    result +=1
print(sum)