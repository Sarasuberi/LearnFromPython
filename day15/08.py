import os
# @properth装饰器

class Student():
    """docstring for Student."""
    def __init__(self, name:str, age:int):
        self.name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age:int):
        if age < 0 or age > 150:
            raise Exception(f'Age {age} is not valid')
        self.__age = age
        
    def __str__(self) -> str:
        return f'Student(name={self.name}, age={self.__age})'
    
def main():
    student = Student('Tom', 18)
    student.age = -2 # 实例变量可以被外部错误修改
    print(student.age)


if __name__ == '__main__':
    main()