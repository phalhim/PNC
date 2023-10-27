#2 - if 1 mango = 2000៛ how much we can get money after sell all mango

fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000}
]
sum = 0
for i in range(len(fruit_stock)):
  if fruit_stock[i]['name'] == "Mango":
    sum = fruit_stock[i]["quality"] * fruit_stock[i]["price"]
print(sum)