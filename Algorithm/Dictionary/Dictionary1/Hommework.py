studentRecord = [
    {"studentName":"Seyla","class":"wep-a","algorithm":98,"html":90},
    {"studentName":"seyha","class":"wep-b","algorithm":80,"html":90},
    {"studentName":"Villa","class":"wep-a","algorithm":96,"html":92},
    {"studentName":"mengheang","class":"wep-a","algorithm":66,"html":54}
]
sumStudent = 0
sumClass = 0
average = 0
for i in range(len(studentRecord)):
    if studentRecord[i]["class"] == "wep-a":
        sumClass +=1
        sumStudent += studentRecord[i]["algorithm"]
    average = sumStudent/sumClass   
print(average)


