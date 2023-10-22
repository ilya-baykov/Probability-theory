class PrimeGenerate:
    def __init__(self, start: int = 1, stop: int = 100):
        self.start = start
        self.stop = stop
        self.prime_list = self.__prime_list_generate()

    def __prime_list_generate(self) -> list[int]:
        return [num for num in range(self.start, self.stop + 1) if self.__is_prime(num)]

    @staticmethod
    def __is_prime(num):
        for divider in range(2, num):
            if num % divider == 0:
                return False
        return True

    def __str__(self):
        return f"Этот экземпляр хранит следующий список простых чисел: {self.prime_list}"


class DigitSumCalc:
    @staticmethod
    def digit_summ_calc(prime_lst: list[int]) -> dict:
        result = {}
        for num in prime_lst:
            summa_digit = 0
            for digit in str(num):
                summa_digit += int(digit)
            result[num] = summa_digit
        return result

    @staticmethod
    def filter_multiples_of_five(primer_dict: dict) -> list[int]:
        return [num for num, value in primer_dict.items() if value % 5 == 0]

    @staticmethod
    def first_digit(primer_lst: list[int], digit: int = 1) -> list[int]:
        return [num for num in primer_lst if str(num)[0] == str(digit)]

    @staticmethod
    def two_digit_number(primer_lst):
        return [num for num in primer_lst if 100 > num > 9]


class Analysis:
    @staticmethod
    def symmetric_difference(arr_1: list[int], arr_2: list[int]):
        return sorted(list(set(arr_1) ^ set(arr_2)))

    @staticmethod
    def difference(arr_1, arr_2):
        return sorted(list(set(arr_1).difference(set(arr_2))))


lst = PrimeGenerate(1, 1000).prime_list
probably_A = DigitSumCalc.filter_multiples_of_five(DigitSumCalc.digit_summ_calc(lst))
probably_B = DigitSumCalc.first_digit(lst)
probably_C = DigitSumCalc.two_digit_number(lst)

symmetric_difference_A_C = Analysis.symmetric_difference(probably_A, probably_C)
difference_B = Analysis.difference(symmetric_difference_A_C, probably_B)
print("События А:", probably_A)
print("События B:", probably_B)
print("События C:", probably_C)
print("*" * 300)
print("Симметричная разница мужду событиями А и событиями C:", symmetric_difference_A_C, sep='\n')
print("Разница между событиями (A sim_diff B) и Событиями B", difference_B, sep='\n')
print("Итоговая Вероятность искомого события составила ~ ", round(len(difference_B) / len(lst), 4))
