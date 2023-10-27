#Ex7 - Array 2D
input = [3,4, 5, 1]
ouput: [
  [1, 2, 3],
  [1, 2, 3, 4],
  [1, 2, 3, 4, 5],
  [1]
]
res =  []
for each in input:
    result = []
    for j in range(each):
        result.append(j+1)
    res.append(result)
print(res)