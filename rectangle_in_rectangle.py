def rect_in_rect(r1, r2):
    return r1[0]**2 >= r2[0]**2 and r1[1]**2 >= r2[1]**2 and r1[2]**2 <= r2[2]**2 and r1[3]**2 <= r2[3]**2



r1 = (int(input("x1: ")), int(input("y1: ")), int(input("x2: ")), int(input("y2: ")))
r2 = (int(input("x1: ")), int(input("y1: ")), int(input("x2: ")), int(input("y2: ")))

print(rect_in_rect(r1, r2))

# Выделить точку в кортеж, функция точка в прямоугольнике.
