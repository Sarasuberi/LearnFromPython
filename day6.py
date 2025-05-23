import sys
import day4 as d4
from day4 import greeting

greeting = d4.greeting
# set集合
# %%
# names = {'Jack', 'Tom', 'Jerry'}
# empty_set = set()定义一个空的set集合必须使用set（）函数
name_set = {'Jack', 'Tom', 'Jerry'}
print(name_set)
print('Jack' in name_set)
name_set.add('Evan')
print(name_set)
name_set.remove('Jack')
name_set.discard('Marry')  # discard删除不存在的元素不会报错
print(name_set)
name_set.pop()  # 随机删除一个元素,并且返回删除的元素
print(name_set)
# %%
# empty_set = set()
# print(empty_set.pop())
# %%
# fronzset()函数创建一个不能被修改的set集合
# new_set = frozenset(set)
frozenset_set = frozenset(name_set)
for index, item in enumerate(frozenset_set, 1):
    print(f'index:{index}, item:{item}')
# %%
# set集合的解析，并集，交集
grade_set_1 = {50, 70, 66, 74}  # 74*1.2=88.8
gtade_set_2 = {66, 80, 90}
new_grade_set = {int(x * 1.2) for x in grade_set_1 if x > 60}
print(new_grade_set)
res_1 = grade_set_1 | gtade_set_2  # |操作符只能合并set
res_2 = grade_set_1.union(gtade_set_2)  # union()可以合并set也可以合并list之类可迭代对象
res_3 = grade_set_1 & gtade_set_2  # &操作符只能交集set
res_4 = grade_set_1.intersection(
    gtade_set_2)  # intersection()可以交集set也可以交集list之类可迭代对象
print(f'res_1:{res_1}')
# %%
# set的其他集合
# 差集运算
res_5 = grade_set_1 - gtade_set_2  # -操作符只能差集set
res_6 = grade_set_1.difference(
    gtade_set_2)  # difference()可以差集set也可以差集list之类可迭代对象
# 对称差集运算 （并集-交集）
res_7 = grade_set_1 ^ gtade_set_2  # ^操作符只能对称差集set
res_8 = grade_set_1.symmetric_difference(
    gtade_set_2)  # symmetric_difference()可以对称差集set也可以对称差集list之类可迭代对象
# 子集运算
res_9 = grade_set_1 < gtade_set_2  # <操作符只能子集set
res_10 = grade_set_1.issubset(gtade_set_2)  # issubset()可以子集set也可以子集list之类可迭代对象
# 超集运算
res_11 = grade_set_1 > gtade_set_2  # >操作符只能超集set
res_12 = grade_set_1.issuperset(
    gtade_set_2)  # issuperset()可以超集set也可以超集list之类可迭代对象
# 不相交运算
res_13 = grade_set_1.isdisjoint(
    gtade_set_2)  # isdisjoint()可以不相交set也可以不相交list之类可迭代对象
print(f'res_5:{res_5}')
# %%
# 异常处理
# try: except: else: finally:
num = input("Enter a number: ")
try:
    ss = int(num)
    res = 10 / ss
    print(f'res:{int(res)}')
except ValueError as e:
    print('Please enter a number')
except ZeroDivisionError as e:
    print('Please enter a number not zero')
except Exception:
    print('Please enter a number')
else:
    print('No error')
finally:
    print('Done')


# %%
# 命令行参数
# sys.argv是个列表，包含命令行参数
def main():
    args = sys.argv[1:]  # sys.argv[0]是脚本名,从sys.agv[1]开始获取
    for arg in args:
        print(arg)


if __name__ == '__main__':
    main()
# %%
