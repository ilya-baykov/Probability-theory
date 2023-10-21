
class PrimeDigits:
    def __init__(self, start: int = 1, stop: int = 100):
        self.start = start
        self.stop = stop

    def search_prime_number(self):
        prime_number = []
        for num in range(self.start, self.stop):
            if PrimeDigits.is_prime(num):
                prime_number.append(num)
        return prime_number

    @staticmethod
    def is_prime(digit: int):
        for num in range(2, digit):
            if digit % num == 0:
                return False
        return True


primer_digits_list = PrimeDigits(1, 1000)
