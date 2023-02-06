# class A():
#     def __init__(self) -> None:
#         self.a = 11
#         self.b = 5
#         print("init A")
#     def test_a(self):
#         print(self.a)

# class B():
#     def __init__(self, x) -> None:
#         self.b = x
#         print("init B")
#     def test_b(self):
#         print(self.b)

# class Mixing():
#     def sum(self):
#         return self.a + self.b

# class C(A, Mixing):
#     def __init__(self) -> None:
#         super().__init__()

# c = C()
# print(c.a)
# print(c.sum())
# Демонстрация примеси

import abc

class BaseShape(abc.ABC):
    @abc.abstractmethod
    def perimeter(self):
        pass
    @classmethod
    def print_name(cls):
        print(cls.name)


class Triangle(BaseShape):
    name = "Triangle"
    def __init__(self, a, b, c) -> None:
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c

class Circle(BaseShape):
    name = "Circle"
    def perimeter(self):
        return 0


print("Start")
t = Triangle(10, 10, 10)
print(t.perimeter())

Triangle.print_name()
