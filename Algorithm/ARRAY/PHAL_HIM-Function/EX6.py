numbers =eval(input())
newNumbers = []
for value in numbers:
    if value % 2 ==0:
        newNumbers.append(value)
print(newNumbers)



numbers =eval(input())
newNumbers = []
for value in numbers:
    if value % 2 !=0:
        newNumbers.append(value)
print(newNumbers)