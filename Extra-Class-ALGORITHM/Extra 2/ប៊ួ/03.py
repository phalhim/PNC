# find number 2 and sum.
number = [1,3,4,2,3,4,5]
sum = 0
for i in range(len(number)):
    if number[i]%2 !=0:
        sum += number[i]
print(sum)