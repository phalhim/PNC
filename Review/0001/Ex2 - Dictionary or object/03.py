#3 - Following price how much money we can get after sell all fruit from stock

fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000}

]
sum = 0
for i in range(len(fruit_stock)):
    sum += fruit_stock[i]['quality'] * fruit_stock[i]['price']
print(sum)