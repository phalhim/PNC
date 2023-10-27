di = [{"name":"banana","price":2000,"quantity":2},
      {"name":"mango","price":2000,"quantity":1}]
sum = 0
for i in range(len(di)):
      sum =di[i]['price']*di[i]['quantity']
      print(sum)