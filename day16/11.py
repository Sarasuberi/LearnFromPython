import os
# 类的继承
# 类继承的定义
# isinstance()返回True或False，判断一个对象是否是某个类的实例
# issubclass()返回True或False，判断一个类是否是另一个类的子类

class Person:
    def __init__(self):
        print("Person's __init__ called")
        self.name = "Jack"

class Student(Person):
    def __init__(self):
        super().__init__() # 执行父类的__init__方法
        print("Student's __init__ called")
        self.school = "ABC High School"

class Stone:
    pass

def main():
    student = Student()
    print(student.name)  # 输出: Jack
    print(student.school)  # 输出: ABC High School
    
    print(isinstance(student, Student))  # 输出: True
    print(isinstance(student, Person))   # 输出: True
    
    person = Person()
    print(isinstance(person, Student))  # 输出: False
    
    print(issubclass(Student, Person))  # 输出: True
    print(issubclass(Person, Student))  # 输出: False
    print(issubclass(Student, Student))  # 输出: True
    
    print(isinstance(Stone, Person))  # 输出: False
    print(issubclass(Stone, Student))  # 输出: False

if __name__ == '__main__':
    main()