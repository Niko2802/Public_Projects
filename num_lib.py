def list_to_num(l):
    x = 0
    k = 10 ** (len(l) - 1)
    for i in l:
        x += i * k
        k = k // 10
    return x


def num_to_list(n):
    l = []
    while n > 0:
        l.insert(0, n % 10)
        n = n // 10
    return l
if __name__ == "__main__":
    print("num_lib")

    print(101 == list_to_num([1, 0, 1]))
    print(1 == list_to_num([0, 0, 1]))
    