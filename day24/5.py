# metaclass 元类
# metaclass就是一个用来创建其他class的类
# type就是所有类默认的metaclass
# 你可以在定义类的时候指定metaclass
# class Person(object,metaclass=type)
# 自定义metaclass

class Human(type):
    def __new__(mcs,*args,**kwargs):
        class_ = super().__new__(mcs,*args)
        #class_.freedom = True
        if kwargs:
            for name,value in kwargs.items():
                setattr(class_,name,value)
        return class_
        
        
class Student(object,metaclass=Human,country="China",freedom=True):
    pass

print(Student.freedom)

print(Student.country)