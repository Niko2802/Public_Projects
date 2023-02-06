def square(p1, p2):
    return (p2[0] - p1[0]) * (p2[1] - p1[1])


def lenght(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5


p1 = (int(input("x1: ")), int(input("y1: ")))
p2 = (int(input("x2: ")), int(input("y2: ")))

print(square(p1, p2))
print(lenght(p1, p2))
