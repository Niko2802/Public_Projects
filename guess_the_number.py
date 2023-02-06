import random


x = random.randint(1, 100)
print(x)
n = 0
y = 0
cold = list(range(60, 100))
chilly = list(range(25, 60))
warm = list(range(10, 25))
hot = list(range(1, 10))
print("Я загадал число от 1 до 100, попробуй угадать!")
while x != y:
    n += 1
    y = int(input(f"Попытка {n}: "))
    if abs(x - y) in cold:
        print("Холодно")
    if abs(x - y) in chilly:
        print("Прохладно")
    if abs(x - y) in warm:
        print("Тепло")
    if abs(x - y) in hot:
        print("Горячо")
print(f"Угадано с {n} попытки")

# Сделать по границе диапазона