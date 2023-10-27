# text =input()
# result =0
# for i in range(len(text)):
#     if text[i]=="a"or text[i]=="b" or text[i]=="c":
#         result+=1
# print(result)

# number =input()
# result =0
# sum =0
# for i in range(len(number)):
#     result += int(number[i])
# sum =result/int(number[0])
# print(sum)




# text = input()
# result = -1
# is_finished = False
# for index in range(len(text)) :
#     letter = text[index]
#     if letter == "K" and is_finished:
#         result = index
#         is_finished = True
# print(result)






# number=""
# text=""
# while text!="end":
#     text=input()
#     if text!="end" and (int(text))%2==0:
#         number+=text+":"
# print(number[:-1])



# text=input()
# result=0
# sum=-1
# for i in range(len(text)):
#     if text[i]=="KK":
#         result+=i
#         sum+=result
# print(sum)



# text = input()
# result = -1
# is_finished = False
# for index in range(len(text)) :
#     letter = text[index]
#     if letter == "K" and is_finished:
#         result+= index
#         is_finished = True
# print(result)



lenOfcher =""
for i in range(4):
    text = input()
    lenOfcher = lenOfcher +"-" +str(len(text)) 
print(lenOfcher)



rows = int(input())
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("x", end=' ')
    print("")
