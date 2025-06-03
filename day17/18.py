from day17.student_1 import Student1
from day17.student_2 import Student2

# 描述符
# 类属性定义时的麻烦
# 描述符的规定
# 描述符是一个特殊的类，要求至少实现如下方法中的一个，一般是get和set
# __set_name__(self, owner, name)
# __get__(self, instance, owner)
# __set__(self, instance, value)
# __delete__(self, instance)
# 实例演示
# 关联18.py  student_1.py student_2.py和required_string.py


def main():
    student_1 = Student1("Jack", "Ma")
    # student_1.last_name = ""

    student_2 = Student2()
    student_2.first_name = "Jack"  # first_name.__set__(student_2, "Jack")
    student_2.last_name = ""


if __name__ == '__main__':
    main()
