#1 - how amny letter in string


text = "Welcome to Phnom Penh"
sum =0
for i in range(len(text)):
    if text[i] !=" ":
        sum+=1
print(sum)