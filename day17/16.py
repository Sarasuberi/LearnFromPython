from enum import Enum
from functools import total_ordering
from enum import auto

# 定制和扩展枚举
# 定制__str__函数
# 定制__eq__函数
# 定制__lt__函数
# @total_order装饰器
# 支持排序，可以用来做枚举的比较
# auto()函数
# 当希望程序自动按顺序来给枚举成员赋值的时候，可以使用auto()函数

@total_ordering
class Status(Enum):
    SUCCESS = 1
    FAIL = 2

    def __str__(self):
        return f"{self.name}({self.value})"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        if isinstance(other, str):
            return self.name == other.upper()
        if isinstance(other, Status):
            return self is other
        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        if isinstance(other, Status):
            return self.value < other.value
        return False


class Student(Enum):
    A = auto()
    B = auto()
    C = auto()

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        if isinstance(other, Student):
            return self.value < other.value
        return False


def main():
    for s in Status:
        print(s)

    print(Status.SUCCESS == 1)
    print(Status.SUCCESS == 'fail')

    print(Status.SUCCESS < 2)

    print(Student.A.value)
    print(Student.C.value)
    print(Student.B < Student.C)
    print(Student.A > Student.C)


if __name__ == '__main__':
    main()
