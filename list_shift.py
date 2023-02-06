import random


l = [random.randint(1, 50) for x in range(10)]
new_list = []
print(l)
list_shift = int(input("Введите сдвиг: "))
new_list = l[list_shift:] + l[:list_shift]
print(new_list)
