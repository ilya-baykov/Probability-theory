def search_cnt(start_probability, probability: float = 0.99):
    def helper(current_probability: float = start_probability):
        nonlocal cnt, start_probability
        print(f" за {cnt} бросков вероятность стала равна: \t {current_probability}")
        if current_probability >= probability:
            return f"Итоговый ответ:    {cnt}"
        cnt += 1
        return helper(round((1 - start_probability) * current_probability + start_probability, 5))

    cnt = 1
    return helper


task_3_3 = search_cnt(1 / 12)
print(task_3_3())
