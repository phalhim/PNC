text = input()
number =-1
for i in range(len(text)-1):
    if text[i] =="K" and text[i+1]=="K":
        number=i
print(number)