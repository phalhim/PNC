# arr = ['Meet', 'Know', 'Week', 'See', 'Eyes'] 
# res = ''
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] == "e" or arr[i][j] == "E":
#             res = arr[i][j]
#     print(arr[i])


# phrase = "I am learning Python !"

# phrase_to_list = phrase.split()

# print(phrase_to_list)
# print(type(phrase_to_list))




# programming_language = "Python asdf asdf"

# programming_language_list = list(programming_language)

# print(programming_language_list)



s = "i like this program very much"
words = s.split(' ')
string = []
for word in words:
    string.insert(0, word)
 
 
print(" ".join(string))