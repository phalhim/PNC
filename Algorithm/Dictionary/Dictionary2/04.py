from collections import Counter
di = {"2021A": 20, "2021B": 30, "2021C": 15 }
dis = {"2021A": 15, "2021C": 10, "2021D": 99 }
sum =dict(Counter(di)+Counter(dis))
print(sum)


