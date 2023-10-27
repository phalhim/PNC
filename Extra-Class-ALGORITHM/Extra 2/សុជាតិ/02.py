#2 សេលសេ function ដ លចាប់យកចាំន្ួន្អកាសេធាំ ន្ិងអកាសេតូច។
text ="I am a student at PNC"
count = 0
counts = 0
for i in range(len(text)):
    if text[i].lower():
        count += 1
    elif text[i].upper():
        counts += 1
print(count)
print(counts)