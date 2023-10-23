import math


def permutations(n: int = 1) -> int:
    return math.factorial(n)


def combinations(k: int = 1, n: int = 2) -> int:
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))


def placement(k: int = 1, n: int = 2) -> int:
    return math.factorial(n) // math.factorial(n - k)


def bernoulli(count: int = 5, favorable_events: int = 5, probability: float = 0.5):
    return combinations(favorable_events, count) * (probability ** favorable_events) * (
            1 - probability) ** (count - favorable_events)


if __name__ == '__main__':
    ...
