# Mixin模式
# 什么是Mixin模式
# Mixin通常翻译为“混入”模式
# 一般讲通用功能抽取封装入Mixin类
# 凡是需要Mixin类功能的类都去通过多继承来获得Mixin类的功能
# Mixin实例
# 编写两个Mixin类，一个实现将对象转换成dict，另一个实现将对象转换成json
import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.to_dict())
    
class DictMixin:
    def to_dict(self):
        return self.__convert_dict(self.__dict__)
    
    def __convert_dict(self,attrs:dict):
        result = {}
        for key,value in attrs.items():
            result[key] = self.__convert_value(value)
        return result
    
    def __convert_value(self,value):
        if isinstance(value,DictMixin):
            return value.to_dict()
        elif isinstance(value,dict):
            return self.__convert_dict(value)
        elif isinstance(value,list):
            return [self.__convert_value(v) for v in value]
        elif hasattr(value,'__dict__'):
            return self.__convert_dict(value.__dict__)
        else:
            return value

class MapMixin:
    def __getitem__(self,key):
        return self.__dict__[key]
    
    def __setitem__(self,key,value):
        self.__dict__[key] = value
        
class Student(MapMixin,DictMixin,JsonMixin):
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        
s = Student("Jack",20)

print(s["name"])
print("dict:")
print(s.to_dict())
print("json:")
print(s.to_json())