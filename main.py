import math


def permutations(n: int = 1) -> int:
    return math.factorial(n)


def combinations(k: int = 1, n: int = 2) -> int:
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))


def placement(k: int = 1, n: int = 2) -> int:
    return math.factorial(n) // math.factorial(n - k)


print(1 / 12)
print(1 / 12 + 11 / 12 * 1 / 12)
print(1 / 12 + 11 / 12 * 1 / 12 + 11 / 12 * 11 / 12 * 1 / 12 + 11 / 12 * 11 / 12 * 11 / 12 * 1 / 12)

if __name__ == '__main__':
    pass
