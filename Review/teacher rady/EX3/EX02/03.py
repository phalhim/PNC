#3 - add string to arr : ['welcome', 'to', 'phnom', 'penh']

text = "Welcome to Phnom Penh"
arr = []
for i in range(len(text)):
    for j in range(len(i)):
        arr.append(text)
print(arr)