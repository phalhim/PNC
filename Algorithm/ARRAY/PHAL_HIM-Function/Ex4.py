def sumFromTo(number1,number2):
    count=0
    for i in range(number1,number2+1):
        count+=i
    return count
number1=int(input())
number2=int(input())
print(sumFromTo(number1,number2))