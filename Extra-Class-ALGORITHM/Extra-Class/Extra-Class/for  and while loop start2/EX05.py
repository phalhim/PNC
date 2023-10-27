number ="12345"
count =0
for i in range(len(number)):
    if int(number[i]) %2!=0:
        count += int(number[i])
print(count)