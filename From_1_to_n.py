def from_1_to_n(n):
    if n == 1:
        return "1"
    return from_1_to_n(n-1) + " " + str(n)


n = 100
print(from_1_to_n(n))


def ar_req(a, p, n):
    if n == 1:
        return a
    return p + ar_req(a, p, n-1)

a = 5
p = 3
n = 12
print(ar_req(a, p, n))
