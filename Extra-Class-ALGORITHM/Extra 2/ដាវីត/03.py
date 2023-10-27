#3 , បញ្ចូល array​ ចាប់អកាសេ "H" បន្ទាប់មករាប់ចាំន្ួន្នន្អកាសេលន្ោះ Ex:
text = ["Meang Heang" , "Sok Heang"]
result =0
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j]=="H":
            result += 1
print(result)

 
