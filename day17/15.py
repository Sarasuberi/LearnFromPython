from enum import Enum, unique

# 枚举别名和装饰器
# 枚举成员的别名
# 当枚举中的多个成员具有相同value的时候，只有一个能成为主要的成员，其他的都自动成为别名
# __members__
# __members__是一个枚举的类成员，记录着所有成员数据，包括了别名信息
# @enum.unique装饰器
# 当我们需要保证枚举中的成员必须具有唯一值的时候，可以使用@enum.unique来帮助约束

class Status(Enum):
    SUCCESS = 1
    OK = 1
    FAIL = 2
    ERROR = 2

@unique
class Gender(Enum):
    MALE = 1
    # FEMALE = 1
    FEMALE = 2


def main():
    for s in Status:
        print(s.name)

    print(Status.__members__)

    print(Status.OK == Status.SUCCESS)
    print(Status.FAIL is Status.ERROR)


if __name__ == '__main__':
    main()
