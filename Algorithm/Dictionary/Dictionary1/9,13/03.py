students = [
    {'name':'HIM', 'class':'A', 'score':90},
    {'name':'Bopha', 'class':'A', 'score':70},
    {'name':'Tesla', 'class':'A', 'score':80},
    {'name':'Kunthea', 'class':'B', 'score':100},
    {'name':'Kolap', 'class':'B', 'score':90},
    {'name':'Vanna', 'class':'B', 'score':50},
    {'name':'Chompey', 'class':'C', 'score':40},
    {'name':'Romchong', 'class':'C', 'score':90},
]

text = "No one fail"
result =input('class: ')
for i in range(len(students)):
    if students[i]['class'] == result and students[i]['score'] <50:
            text =students[i]['name']
print(text)