def sum(arrays):
    result=0
    for i in range(len(arrays)):
        result += arrays[i]
    return result

def averages(numbers):
    total=0
    resultAverage=0
    for i in range(len(numbers)):
        total+=numbers[i]
    resultAverage=total/len(numbers)
    return resultAverage
number1 = eval(input("Enter array of number: "))
print (sum(number1))
print (averages(number1))