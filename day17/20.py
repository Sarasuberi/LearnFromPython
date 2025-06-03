# 异常类
# 常用的异常类继承关系
# 异常类的捕捉
# 在try...except语句中，可以使用特定的异常类来捕捉错误，也可以使用父类型的异常类来捕捉
# 同时处理多个异常
# raise异常
# 可以在代码中通过raise异常的方式来向调用者返回错误信息
# raise 异常类对象
# 自定义异常

class InvalidArgumentException(Exception):

    def __init__(self, *args):
        super().__init__(args)


def add(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise InvalidArgumentException("Argument is not int")

    return n1 + n2


def main():
    try:
        num = 2
        s = 10
        res = num / s

        print(res)

        names = ("Jack", "Tom")
        print(names[0])

        add("a", "b")
    except ArithmeticError:
        print("ArithmeticError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except InvalidArgumentException as iae:
        print(f"Argument is not valid: {iae}")
    except Exception as ex:
        print(f"Exception: {ex}")


if __name__ == '__main__':
    main()
