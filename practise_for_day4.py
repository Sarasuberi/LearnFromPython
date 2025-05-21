# 打印n到1的整数
input_num = int(input("请输入一个整数："))
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)
print_n_to_1(input_num)

# %%
num_str = input("请输入一个整数：")
def print_to_1(n):
    print(n)
    print_to_1(n-1) if n > 1 else 1


print_to_1(int(num_str))

# %%
# 数列求和
tip = 'please enter the number '
start_str = input(f'{tip}for start:')
step_str = input(f'{tip}for step:')
end_str = input(f'{tip}for end:')
result = 0


def sum_n(n: int):
    global result
    if n > int(end_str):
        print(result)
    else:
        result = result + n
        n = n + int(step_str)
        sum_n(n)


sum_n(int(start_str))

# %%
start_str = input("Please input the summary_n number ")
def summary_n(n):
    return n + summary_n(n - 1) if n > 1 else 1


summary_n(int(start_str))

# %%
# 求解n的阶乘
tip = 'Please input the number '
factorial_str = input(tip)
def factorial(n:int,result:int = 0):
    if n <= 1:
        print(result)
    else:
        result = n * (n-1)
        factorial(n-2,result)
factorial(int(factorial_str))

# %%
fs = input("Please input the number ")
def f(n:int):
    return n * f(n-1) if n > 1 else 1


f(int(fs))
# %%
