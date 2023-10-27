def getPrice(fruitName):
    if fruitName == "banana":
        return 2
    if fruitName == "apple":
        return 5
    if fruitName == "orange":
        return 1
print("banana price is: " + str(getPrice("banana")) + " dollars")
print("orange price is: " + str(getPrice("orange")) + " dollars")
print("apple price is: " + str(getPrice("apple")) + " dollars")
