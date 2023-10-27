text = "xx[y]x"
indexOfOpenBracket = -1
indexOfCloseBracket = -1
result = "OK"
for i in range(len(text)):
    if text[i] != "x" and text[i] != "[" and text[i] != "]" and text[i] != "y":
        result = "WRONG"
    if text[i] == "[":
        indexOfOpenBracket = i
    if text[i] == "]":
        indexOfCloseBracket = i
if result != "WRONG" and indexOfCloseBracket != -1 and indexOfOpenBracket != -1 and indexOfOpenBracket+1 != indexOfCloseBracket:
    for j in range(indexOfOpenBracket+1, indexOfCloseBracket, 1):
        if text[j] != "y":
            result = "WRONG"
else:
    result = "WRONG"
print(result)