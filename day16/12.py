import os
# 方法重写
# 什么是方法重写
# 方法重写特指在子类中重新定义父类的方法。子类继承了父类的方法，但有时父类的方法并不满足子类的需求，此时就需要在子类中重写父类的方法。
# 方法重写
# 类属性重写
# 调用父类方法
# 子类中可以通过super()函数调用父类的方法，这样可以在子类中扩展或修改父类的行为。

class Person:
    color = 1 # 类属性
    def __init__(self):
        self.name = "Jack"
        
    def say(self):
        print("Hello from Person")
        
    def print_color(self):
        print(f"Person is {self.color}")

class Student(Person):
    color = 2  # 类属性重写
    def __init__(self):
        super().__init__() 
        self.school = "ABC High School"
    
    def say(self):
        super().say()
        print("Hello from Student")

class Worker(Person):
    pass

def render(person:Person):
    person.say()
    
def main():
    student = Student()
    student.say()  # 输出: Hello from Student
    
    person = Person()
    person.say()  # 输出: Hello from Person

    person = Student()
    person.say()  # 输出: Hello from Student
    
    render(student)  # 输出: Hello from Student
    render(Worker())  # 输出: Hello from Person
    
    print(student.color)  # 重写前输出: 1 ，重写后输出: 2
    student.print_color()  # 输出: Person is 2
    
    
if __name__ == '__main__':
    main()