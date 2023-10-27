def sum(numbers):
    result =[]
    for i in range(len(numbers)):
        if numbers[i] %2 ==0:
            result += [numbers[i] ]
    return result
numbers =eval(input("Enter have number: "))
print(sum(numbers))