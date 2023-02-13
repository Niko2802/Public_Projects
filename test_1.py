class A():
    def __init__(self, val) -> None:
        self.val = val

    def __sub__(self, x):
        return A(self.val - x.val)
    
a1 = A(10)
a2 = A(5)
print((a1-a2).val)
a3 = a1 - a2
print(a3.val)
