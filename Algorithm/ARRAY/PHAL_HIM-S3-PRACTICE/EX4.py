def sumBetweenNumberTwo(numbers):
    isFoundNumberTwo = False
    total = 0
    for value in numbers:
        if value == 2:
            isFoundNumberTwo = not (isFoundNumberTwo and total !=0)
        elif isFoundNumberTwo :
            total += value
    return total
numbers = eval(input())
print(sumBetweenNumberTwo(numbers))
