


# text =input()
# isinstance = False
# for i in range(len(text)):
#     if text[i] =="B":
#         isinstance = True
# print(isinstance)


text = input()
result = "wrong"
for i in range(len(text)-3):
    if text[i] =="[" and text[i+1] =="y":
        result = "ok"
    if text[i+2]=="y" and text[i+3]=="]":
        result ="ok"
    elif text[i] !="[" or text[i]!="y":
        result="wrong"
print(result)