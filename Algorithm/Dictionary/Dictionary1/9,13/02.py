materials = [
  {'name': 'Computer', 'quantity': 20, 'retail_price': 400, 'quality': 'Good'},
  {'name': 'Computer', 'quantity': 10, 'retail_price': 200, 'quality': 'Not good'},
  {'name': 'Monitor', 'quantity': 20, 'retail_price': 1000, 'quality': 'Not good'},
  {'name': 'Keyboard', 'quantity': 10, 'retail_price': 150, 'quality': 'Good'},
  {'name': 'Speaker', 'quantity': 5, 'retail_price': 50, 'quality': 'Good'}
]
sum =0
for i in range(len(materials)):
    if materials[i]['quality'] =='Not good':
        sum += materials[i]['quantity']
print(sum)