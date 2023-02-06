import time
import sys
sys.setrecursionlimit(10000)


def memoize(f):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper


def benchmark(f):
    def wrapper(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        print("Время выполения:", time.time() - s)
        return ret
    return wrapper


@benchmark
def hof_g(n):
    @memoize
    def r_hof_g(n):
        if n == 0:
            return 0
        return n - r_hof_g(r_hof_g(n-1))
    return r_hof_g(n)


print(hof_g(1000))
