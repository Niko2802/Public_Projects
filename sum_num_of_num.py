def sum_num(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_num(n//10)


n = 123456
print(sum_num(n))
