import os
# 类方法
# 类方法需要使用@classmethod装饰器来定义
# 类方法的第一个参数是类本身
class Student:
    school = "abc"
    @classmethod
    def get_instance(cls):
        print(f"Student {cls.school}")

Student.get_instance()  # 调用类方法获取类的实例
# 静态方法
# 静态方法需要使用@staticmethod装饰器来定义
# 静态方法只是定义在类范围内的一个函数而已
class School:
    @staticmethod
    def get_school_name():
        return "ABC School"

print(School.get_school_name())  # 调用静态方法获取的实例
