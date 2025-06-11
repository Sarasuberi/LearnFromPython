# nonlocal范围
# 什么是nonlocal范围
# Built-in范围（整个程序）-> 模块A范围，模块B范围（python文件） -> nonlocal（函数） ->  local(函数中嵌套函数)
# nonlocal关键字
# 使用nonlocal关键字来制定使用nonlocal范围的变量

message = "module"

# nonlocal范围
def outer():
    message = "outer"
    # local 范围
    def inner():
        nonlocal message 
        message = "inner"
        print(f"inner:{message}")
    inner()
    print(f"outer:{message}")
outer()

print(message)