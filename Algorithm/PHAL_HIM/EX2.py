def getComment(grade):
    if grade > 10:
        return "Good"
    else:
        return "Bad"
print(getComment(18) + getComment (8))
