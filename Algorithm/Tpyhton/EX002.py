text =input()
result="SORTED"
for i in range(len(text)-1):
    if text[i]>text[1+i]:
        result ="NOT SORTED"
print(result)

