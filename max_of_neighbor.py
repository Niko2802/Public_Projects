import random


l = [random.randint(1, 50) for x in range(10)]
print(l)
l1 = ([l[i] for i in range(1, len(l)-1) if l[i-1] < l[i] > l[i+1]])
print(l1)
