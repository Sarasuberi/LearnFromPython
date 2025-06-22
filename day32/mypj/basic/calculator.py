class Calculator:
    def add(self, *args):
        result = 0
        for i in args:
            result += i
        return result

    def is_odd(self, num: int) -> bool:
        return num % 2 != 0
