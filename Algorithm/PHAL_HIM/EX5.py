def improve(number1,number2):
    if number1 > number2:
        return number1
    else:
        return number2
number1 =int(input())
number2 =int(input())
print("Maximum is " + str(improve(number2,number1)))
