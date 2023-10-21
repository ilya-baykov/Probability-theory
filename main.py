import math


def permutations(n: int = 1) -> int:
    return math.factorial(n)


def combinations(k: int = 1, n: int = 2) -> int:
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))


def placement(k: int = 1, n: int = 2) -> int:
    return math.factorial(n) // math.factorial(n - k)


# events = {}
# cnt = 0
# for i in range(1, 13):
#     for j in range(1, 13):
#         for z in range(1, 13):
#             cnt += 1
#             key = i + j + z
#             events[key] = events.get(key, 0) + 1
# sorted_events = dict(sorted(events.items(), key=lambda item: item[1], reverse=True))
# answer_dict = {k: (v, round(v / cnt, 4)) for k, v in sorted_events.items()}
# keys_list = list(answer_dict.keys())
# for i in range(5):
#     current_elem = keys_list[i]
#     print(current_elem, answer_dict[current_elem])

print(1 / 12)
print(1 / 12 + 11 / 12 * 1 / 12)
print(1 / 12 + 11 / 12 * 1 / 12 + 11 / 12 * 11 / 12 * 1 / 12 + 11 / 12 * 11 / 12 * 11 / 12 * 1 / 12)


def search_cnt(start_probability, probability: float = 0.99):
    def helper(current_probability: float = start_probability):
        nonlocal cnt, start_probability
        print(f" за {cnt} бросков вероятность стала равна: \t {current_probability}")
        if current_probability >= probability:
            return cnt
        cnt += 1
        return helper(round((1 - start_probability) * current_probability + start_probability, 3))

    cnt = 1
    return helper


task_3_3 = search_cnt(1 / 12)
print(task_3_3())
if __name__ == '__main__':
    pass
