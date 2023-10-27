number =int(input("Please enter the number:"))
count = 0
for i in range(number):
        for z in range(i+1):
            count = count+1
            print(count,end=" ")
        print("")