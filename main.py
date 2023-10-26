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


def poisson(_lambda: int = 1, count: int = 11, period: int = 3):
    return ((_lambda * period) ** count) * (math.e ** (-1 * _lambda * period)) / math.factorial(count)


if __name__ == '__main__':
    pass
