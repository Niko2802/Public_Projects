import random


l = [random.randint(1, 5) for x in range(10)]
print(l)
# max_count = 0
# el_idx = 0
# for i in l:
#     if max_count < l.count(i):
#         max_count = l.count(i)
#         el_idx = l.index(i)
# print(l[el_idx])



print(max(l, key=l.count))
