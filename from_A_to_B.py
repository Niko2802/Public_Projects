def a_to_b(a, b):
    if a > b:
        if a == b:
            return b
        s = str(b) + " " + str(a_to_b(b+1, a))
        return s
    else:
        if a == b:
            return a
        s = str(a) + " " + str(a_to_b(a+1, b))
        return s


a = 20
b = 10
print(a_to_b(a, b))
