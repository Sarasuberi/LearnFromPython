import os

# 实例函数的定义
# 认识__init__()函数
# 定义实例变量
# 实例函数中访问实例变量
# 外部访问实例变量与函数

class Student:
    def __init__(self,name:str):  # __init__()函数是类的构造函数,在创建对象时自动调用,用来初始化
        self.name = name  
    def say_hello(self,msg): # self代表实例本身,只要是类的实例函数,必须有一个参数是self
        print(f"hello{msg}, {self.name}") 
        
def main():
    # 1.创建一个物理对象
    # 2.调用__init__初始化对象
    s1 = Student("Jack")
    s2 = Student("Tom")
    s1.say_hello(" world")  # 调用实例函数
    s2.say_hello(" Python") 
    s1.gender = "male"  
    print(s1.gender)
    # print(s2.gender)  # AttributeError: 'Student' object has no attribute 'gender'

if __name__ == '__main__':
    main()