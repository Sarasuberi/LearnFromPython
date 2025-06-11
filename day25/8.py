# 变量范围
# 范围的划分
# 原则上来讲变量分全局范围和本地范围
# Built-in范围（整个程序）-> 模块A范围，模块B范围（python文件） -> 本地范围（函数）
# 变量的查找顺序
# 从小到大的搜索顺序    本地范围（函数） -> 模块A范围，模块B范围（python文件）-> Built-in范围（整个程序）
# global关键字
# global 变量

count = 10
print(count)

def greeting(flag:bool):
    if flag:
        count = 20
    # 如果是false的话会报错 cannot access local variable 'count' where it is not associated with a value
    # 如果在函数中定义了同名变量，无论是否执行到了定义那行，都会使用函数内的变量
    # 如果需要使用全局变量需要使用global关键字
    # 使用全局关键字如果出错了比较难以排查，谨慎使用
    print(count)
    
greeting(False)
print(count)