def right_num(n):
    if n < 10:
        return n
    else:
        return str(n % 10) + " " + str(right_num(n // 10))


n = 123456
print(right_num(n))
