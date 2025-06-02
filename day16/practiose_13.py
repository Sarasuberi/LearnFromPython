# 练习实例
# 大学里面的学生分为国内生和国际生
# 那么就可以定义Student类为抽象父类
# 定义DomesticStudent和InternationalStudent为子类来实现抽象的父类
from instance.Student import Student
from instance.International_student import International_student
from instance.Domestic_student import Domestic_student

def students(student: Student):
    student.nationality()
    
def main():
    
    students(International_student())
    students(Domestic_student())

if __name__ == '__main__':
    main()