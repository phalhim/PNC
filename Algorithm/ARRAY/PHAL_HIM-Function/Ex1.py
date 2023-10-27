def removeMinus(word):
    newWord = ""
    for i in range(len(word)):
        if word[i] != "-":
            newWord +=  word[i]
    return newWord
isinstanue = True
while isinstance:
    name = input("Enter name :")
    print(removeMinus(name))
    message = input("Do you want to continue? N/Y : ")
    if message == "N":
        isinstance = False
