import os
# 面向对象的概念解释
# 类 -- 是描述一类对象的特征集合
# 对象 -- 是符合类定义特征的具体实例
# 属性 -- 分为类属性和实例属性
# 方法 -- 分为类方法和实例方法 
# 类的定义
class Student:
    pass
class Teacher:
    pass
# 对象的创建
student_1 = Student()  # 实例化对象
print(hex(id(student_1)))  # 以十六进制打印对象的内存地址
# isinstance（）函数
# isinstance() 函数用于判断一个对象是否是一个类类型的对象，返回布尔值
print(isinstance(student_1, Student))  # True
print(isinstance(student_1, Teacher))  # False
# Python中的类本身也是一个对象
print(type(Student))  # <class 'type'>

def main():
    pass
if __name__ == '__main__':
    main()