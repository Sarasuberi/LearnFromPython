# dataclass
# 为何需要dataclass
# 存放很多需要反复使用的数据之类的类
# 使用dataclass
# 属性的缺省值
# age:int = 18
# 不可变对象    
# frozen=True
# 定制属性的行为
# 通过使用field()来定制属性的特征
# 排序
# 在dataclass中排序只会按照第一个参数进行排序，有三种方案实现
# 第一种直接把需要排序的参数放在最前面
# 第二种在最前面添加一个用以排序的参数，然后在init中赋值
# 第三种在排序中使用key方法指定

import operator
from dataclasses import dataclass,field

# @dataclass(frozen=True)
@dataclass(order=True)
class Student:
    sort_index:int = field(init=False,repr=False)
    name:str
    age:int = 18
    independet:bool = field(default=False,init=False,repr=False,hash=False,compare=False,metadata=None)
    
    def __post_init__(self):
        self.independet = self.age > 18
        self.sort_index = self.age
    
s1 = Student("Jack",20)
print(s1)

s2 = Student("Tom")
print(s2)

print(s1 == s2)

students = [s2,s1]
sort_student = sorted(students)
print(students)
print(f"sort:{students.sort()}")
print(f"sort_student:{sort_student}")

students.sort(key=operator.attrgetter('age'))
print(f'students_operator:{students}')