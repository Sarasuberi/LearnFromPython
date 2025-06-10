# metaclass实例
# 创建一个metaclass使得如下代码能够工作
#class Student(object, metaclass=Human):
#    props = ["name", "age"]
# student = Student()
# print(student.name)
# print(student.age)
# student.name = "Tom"
# student.age = 30
# print(student.name)
# print(student.age)

class Prop:
    def __init__(self, attr):
        self._attr = f'_{attr}'

    def get(self, obj):
        if not hasattr(obj, self._attr):
            return None
             # raise AttributeError("object has no attribute %s" % self._attr)
        return getattr(obj, self._attr)

    def set(self, obj, value):
        setattr(obj, self._attr, value)

class Human(type):
    @staticmethod
    def __new__(mcs,*args, **kwargs):
        class_ = super().__new__(mcs, *args)
        for property_name in class_.props:
            prop = Prop(property_name)
            p_obj = property(fget=prop.get,fset=prop.set)
            setattr(class_,property_name,p_obj)
            setattr(class_,property_name,p_obj)
        return class_
    
class Student(object,metaclass=Human):
    props = ["name","age"]

student = Student()
print(student.name)
print(student.age)
student.name = "Jack"
student.age = 30
print(student.name)
print(student.age)