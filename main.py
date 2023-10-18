import math


def permutations(n: int = 1) -> int:
    return math.factorial(n)


def combinations(k: int = 1, n: int = 2) -> int:
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))


def placement(k: int = 1, n: int = 2) -> int:
    return math.factorial(n) // math.factorial(n - k)


