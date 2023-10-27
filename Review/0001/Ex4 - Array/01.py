text = "hello world"
delattr = " "
arr =[]
split_string = text.split(delattr)
for char in text:
    arr.append(char)
print(split_string)
print(arr)
string = ''
for i in range(len(text)):
    if text[i] == " " or i == len(text)-1:
        if i == len(text):
            string += text[i]
        res = ''
        for j in range(len(string)):
            res += string[len(string)-(j + 1)]
        arr.append(res)
        string = ''
    else:
        string += text[i]
print(arr)