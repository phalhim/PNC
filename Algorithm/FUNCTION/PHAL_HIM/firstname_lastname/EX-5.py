array1 = [
 {"subject": "html", "class": "WEP-B", "teacher-id":45},
 {"subject": "html", "class": "WEP-A", "teacher-id" :36},
 {"subject": "algorithm", "class": "WEP-B", "teacher-id": 36},
]
array2 = [
 {"teacher-id": 36, "first-name": "rady", "last-name": "Y"},
 {"teacher-id": 45, "first-name": "ronan", "last-name": "the best"},
]
name = ''
def arrayDictinary(arr,val):
    for i in range(len(arr)):
        if arr[i]["subject"] =="algorthm" and arr[i]["teacher-id"] == 69:
            name +=arr[i]
    return name
