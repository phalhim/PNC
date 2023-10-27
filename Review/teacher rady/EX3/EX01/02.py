#2 - Sum all value seperated by space 

numberInString = "10 30 4 12"
sum =0
for i in range(len(numberInString)):
    if numberInString[i] ==" ":
        sum+=1
print(sum)