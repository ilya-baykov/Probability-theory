from main import poisson

answer = 1
for count_call in range(0, 11):
    answer -= poisson(1, count_call, 3)
    print(f"С вероятностью {round(answer, 4)} поступит больще {count_call} вызовов ")
print()
print("Вероятность того , что за 3 часа поступит более 10 вызовов равна: ", round(answer, 6))
