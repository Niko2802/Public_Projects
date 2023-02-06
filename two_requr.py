def two_req(n):
    if n == 1:
        return "Yes"
    elif n < 1:
        return "No"
    n = two_req(n/2)
    return n

n = 128
print(two_req(n))
