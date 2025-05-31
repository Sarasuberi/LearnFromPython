import os

# 私有属性与函数的用途
# 在面向对象的封装中，私有的属性与函数其根本目的是防止他们在类的外部被使用
# 在Python中并没有严格的权限限定符进行限制
# 主要通过命名来进行区分
# 如何定义私有属性与函数
# 在属性名或函数名前加上下划线或者两个下划线
class Student:
    def __init__(self, name, gender):
        self._name = name  # 保护属性，单下划线表示受保护
        self.__gender = gender  # 私有属性，双下划线表示私有

    def _change_gender(self):
        pass
    def __change_name(self):
        pass
# 如何访问私有属性与函数
s1 = Student("Tom","male")
s1._name = "Jack"  # 可以访问受保护属性
s1.__gender = "female"  # 不能访问私有属性
s1._change_gender()  # 可以访问受保护函数
s1.__change_name()  # 这一行会报错，不能访问私有函数

