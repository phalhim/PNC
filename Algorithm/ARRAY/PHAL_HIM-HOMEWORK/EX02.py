def sum(numbre):
    result1 =0
    for i in range(len(numbre)):
        result1 += numbre[i]
    return result1

number1 = eval(input("Enter have number1: "))
number2 = eval(input("Enter have number2: "))
print(sum(number1))
print(sum(number2))