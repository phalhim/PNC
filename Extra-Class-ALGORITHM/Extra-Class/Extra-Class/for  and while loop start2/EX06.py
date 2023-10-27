number ="12345"
sum =0
result =0
while sum < len(number):
    if int(number[sum])%2 !=0:
        result +=int(number[sum])
    sum +=1
print(result)