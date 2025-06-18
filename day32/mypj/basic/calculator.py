class Calculator:
    def add(self, *args):
        result = 0
        for i in args:
            result += i
        return result
