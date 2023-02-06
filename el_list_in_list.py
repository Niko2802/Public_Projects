import random


l1 = [random.randint(1, 5) for x in range(5)]
l2 = [random.randint(1, 5) for x in range(5)]
l3 = []
print(l1)
print(l2)
l3 = [x for x in l1 if x not in l2]
print(l3)
