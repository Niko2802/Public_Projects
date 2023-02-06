def min_max1(l):
    d_sorted = l.sort()
    return l[0], l[-1]




def min_max(l, d):
    d_sorted = l.sort()
    if d == "min":
        return l[0]
    else:
        return l[-1]


l = [1, 34, 13, 56, 11, 3, 61, 7]
print(min_max(l, "min"))
print(min_max(l, "max"))


min_1, max_1 = min_max1(l)
print(min_1)
print(max_1)

