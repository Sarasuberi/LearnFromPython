from pprint import pprint
# -*- coding: utf-8 -*-
# 什么是类变量
# 属于类本身这个对象的属性
# 所有该类的对象都共享类变量
# 定义类变量
class Student:
    student_count = 8  # 类变量，所有Student类的实例共享
print(Student.__name__)
# 取得类变量的值
# 直接取得类变量的值
print(Student.student_count)  # 输出: 8
# 如果没有这个类变量，会看到AttributeError
# print(Student.unknown)  # 输出: Error
print(getattr(Student, 'unknown',10))  # 输出默认值 10
# 使用getattr()函数获取类变量的值，如果不存在，返回None
print(getattr(Student, 'student_count'))  # 输出: 8
# 设置类变量的值
# 直接设置类变量的值
Student.student_count = 20  # 设置类变量的值
print(Student.student_count)  # 输出: 20
# 使用setattr()函数设置类变量的值
setattr(Student, 'student_count', 100)  # 使用setattr()函数设置类变量的值
print(Student.student_count)  # 输出: 100
# 如果类变量不存在，可以运行是添加
setattr(Student, 'newattribute', 'Hello')  # 如果类变量不存在，可以运行是添加
print(Student.newattribute)  # 输出: Hello
# 删除类变量
# del Student.student_count  # 删除类变量
# delattr(Student, 'newattribute')  # 使用delattr()函数删除类变量
# 类变量的存储
# 类变量全部存放在类变量__dict__字典中，但不要直接修改__dict__内容
pprint(Student.__dict__)  # 查看类的属性和方法

def main():
    pass

if __name__ == '__main__':
    main()