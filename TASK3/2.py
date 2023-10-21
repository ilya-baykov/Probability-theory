events = {}
cnt = 0
for i in range(1, 13):
    for j in range(1, 13):
        for z in range(1, 13):
            cnt += 1
            key = i + j + z
            events[key] = events.get(key, 0) + 1
sorted_events = dict(sorted(events.items(), key=lambda item: item[1], reverse=True))
answer_dict = {k: (v, round(v / cnt, 4)) for k, v in sorted_events.items()}
keys_list = list(answer_dict.keys())
for i in range(5):
    current_elem = keys_list[i]
    print(
        f"Сумма: {current_elem}, можно 'собрать' {answer_dict[current_elem][0]} способами; вероятность выпадения составляет около"
        f" {answer_dict[current_elem][1]}")
