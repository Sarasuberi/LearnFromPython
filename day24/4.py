# type类
# 任何class在内存里就是一个type类的对象
# Python使用type类来创建其他的class
# type（class_name，paremts,clss_dict）
# 理论上来讲，可以使用type来动态创建class

class Student:
    def greeting(self):
        print('Hello Student')

print(type(Student)) # <class 'type'>
print(isinstance(Student, type)) # True

class_body = """
def greeting(self):
        print('Hello Students')
"""
class_dict = {}
exec(class_body,globals(),class_dict)

ss = type("Students", (object,), class_dict) # <class '__main__.Students'>
Customer = type("Customer", (object,), dict(greeting=lambda self: print('Hello Customer'))) # <class '__main__.Customer'>

s = ss()
s.greeting() # Hello Students

c = Customer()
c.greeting()