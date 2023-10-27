text=input()
sum =0
result="Lost"
for i in range(len(text)):
    if int(text[i]) <=20:         
        result="WON"
        sum= sum+int(len(text))
    else: 
        int(text[i]) > 20 
print(result)