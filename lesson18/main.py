from functools import lru_cache
from sys import getsizeof


@lru_cache(maxsize=1000)
def fibonacci(n):
    if (type(n) != int) or (n < 1) :
        raise TypeError("n must be a positive int")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for n in range(-5, 501):
    print(n, ":", getsizeof(fibonacci(n)), ":", fibonacci(n), )