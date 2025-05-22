import requests
from functools import reduce

salaries = [6000, 6800, 6300, 8000]
students = [('Jack', 23), ('Tom', 22), ('Lucy', 21)]
nums = [5,2,3,9]

# %%
# map()通过遍历每一个集合中的元素并对每个元素执行给定的操作，然后返回一个迭代器。
# lterator = map(function,list)
result = map(lambda x: x * 1.1, salaries)
print(list(result))
ages = list(map(lambda x: x[1], students))
print(ages)
#%%

# filter()函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新迭代器。
# lterator =  filter(function, iterable)
result = list(filter(lambda x: x > 6500, salaries))
print(result)
print(list(filter(lambda x: x[1] >= 22, students)))

# reduce()函数会对参数序列中的元素进行求解，并得到一个唯一结果。
# result = reduce(function, list)
print(reduce(lambda x, y: x + y, nums))

# 列表解析是对一个列表操作来生成新列表的过程
# [输出表达式 for 元素 in 列表]
print(list(map(lambda x: x * x, nums)))
print([x * x for x in nums])
print([x * x for x in nums if x < 9])

# %%
# 字典
student = {
    'name': 'Tom',
    'age': 23,
    'gender': 'male',
    'hobbies': ['basketball', 'football']
}
print(student['name'])
print(student.get('age'))
print(student.get('school'))
print(student.get('school', 'No School'))
print(student.get('age', 20))
student['age'] = 24
student['school'] = 'ABC'
del student['hobbies']
print(student)
dict.items(student)
dict.keys(student)
dict.values(student)
for data in student.items():
    print(type(data))
    print(data)
for key, value in student.items():
    print(key, value)
for data in student.items():
    print(data[0])
for s in student:
    print(s)
for s in student.values():
    print(s)
# %%