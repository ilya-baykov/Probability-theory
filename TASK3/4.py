with open('surnames', 'r', encoding='UTF-8') as data:
    surnames = {}
    for surname in data.readlines():
        for letter in surname:
            if letter.lower() in 'ауоыэяюёие':
                surnames['vowels'] = surnames.get('vowels', 0) + 1
            else:
                surnames['consonants'] = surnames.get('consonants', 0) + 1

cnt_letters = sum(surnames.values())
probably = round(surnames['vowels'] / cnt_letters, 2)

print(probably)
