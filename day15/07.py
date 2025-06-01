import os
# 如何防止实例变量被外部错误修改
# 编写setter和getter方法
# 引入property类

class Student():
    """docstring for Student."""
    def __init__(self, name:str, age:int):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age:int):
        if age < 0 or age > 150:
            raise Exception(f'Age {age} is not valid')
        self.__age = age
        
    def __str__(self) -> str:
        return f'Student(name={self.name}, age={self.__age})'
    
    age = property(fget = get_age, fset = set_age)

def main():
    student = Student('Tom', 18)
    # student.age = -2 # 实例变量可以被外部错误修改
    student.set_age(20) 
    print(student)


if __name__ == '__main__':
    main()