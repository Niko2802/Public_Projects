def akkerman(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return akkerman(m-1, 1)
    elif m > 0 and n > 0:
        return akkerman(m-1, akkerman(m, n-1))


m = 3
n = 5
print(akkerman(m, n))
