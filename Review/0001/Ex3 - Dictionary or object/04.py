#4 - Add fruit name to array

fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 0, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000},
  {'id': 4, 'name': 'Orange', 'quality': 0, 'price': 5000},
  {'id': 5, 'name': 'Apple', 'quality': 5, 'price': 3000},
  {'id': 6, 'name': 'Jackfruit', 'quality': 13, 'price': 6000},
]
result =[]
for i in range(len(fruit_stock)):
    result.append(fruit_stock[i]["name"])
print(result)
