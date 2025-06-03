# __new__方法
# 函数动态参数列表
# __new__方法的定义原型
# __new__定义在object类当中，所有类的最终父类都是object类
# object.__new__(self,*agrgs,**kwargs)
# __new__方法的执行时刻
# __new__方法最佳实践
# 在什么情况下使用__new__方法，以及怎么用。
# 通常情况下定义了__new__就不用在定义__init__方法了


class SquareNumber(int):

    def __new__(cls, value: int):
        return super().__new__(cls, value**2)


class Student:

    def __new__(cls, first_name, last_name):
        obj = super().__new__(cls)
        obj.first_name = first_name
        obj.last_name = last_name
        return obj


def execute(*args,**kwargs):
    print(args)
    print(kwargs)


def main():
    execute("abc")
    execute("abc", "def")
    execute("abc", 12)
    execute("abc", 34, name="Tom", age=55)

    num = SquareNumber(2)
    print(num)
    print(type(num))
    print(isinstance(num, int))

    student = Student("Jack", "Ma")
    print(student.first_name)
    print(student.last_name)

if __name__ == '__main__':
    main()
