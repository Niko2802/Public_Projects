def left_num(n):
    if n < 10:
        return n
    else:
        return str(left_num(n // 10)) + " " + str(n % 10)


n = 123456
print(left_num(n))
