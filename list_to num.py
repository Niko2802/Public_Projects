import sys
from re import X

# from num_lib import num_to_list, list_to_num
import num_lib as nl

n = int(input("Число: "))
l = nl.num_to_list(n)
print(l)
l.reverse()
n1 = nl.list_to_num(l)
print(sum(l))
print(n1 == n)


print(sys.argv)
