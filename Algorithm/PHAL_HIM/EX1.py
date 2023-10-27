def numberOfUpperCases(word):
    count =0
    for i in range(len(word)):
        if word[i] == word[i].upper() and word[i] !=" ":
            count +=1
    return count
word =input("Enter :")
print(numberOfUpperCases(word))