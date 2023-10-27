for i in range(2):
    print(i)
    for x in range(i+1):
        print(x)
        for z in range(i - x):
            print("text")
    