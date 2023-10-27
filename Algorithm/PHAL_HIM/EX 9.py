n = input()
result =0
for i in range(len(n)):
    if n[i]=="a" or n [i] =="A":
        result += 1
if result>0:
    print(str(result) + "A in n")
else:
    print("A Not found")