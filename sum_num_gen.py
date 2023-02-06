from functools import reduce

n = list(range(10))
res = reduce(lambda n1,n2: n1+n2, [x for x in n if x%2==0])
print(res)
