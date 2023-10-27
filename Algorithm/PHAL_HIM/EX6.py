def improve(text1):
    result = ""
    lastIndex = len(text1) - 1
    for i in range(len(text1)):
        result += text1[lastIndex - i]
    return result
text1=input()
print(improve(text1))