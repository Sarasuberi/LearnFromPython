import requests
# %%
#range()函数的三种参数用法
range_a = range(10) #生成0到n-1的整数序列
range_b = range(1,10) #生成1开始到10-1的整数序列
range_c = range(1,10,2) #生成1开始到10-1，步长为2的整数序列
print(type(range_a))
print(f"range_a:{range_a}")
print(f"range_b:{range_b}")
print(f"range_c:{range_c}")

# %% 
#for循环
for index in range(5): #有点类似foreach？ 
    restul = index + 2
    print(restul)
    print("end of for loop")

# %%
#while循环
i = 0
while i < 11:
    print(i)
    i += 1
    print("end of while loop")

# %%
# break,continue,pass
# break中断循环    
for index in range(1,11): 
    restul = index + 2
    if restul > 7:
        break
    print(restul)
    print("end of break loop")
# continue跳过本次循环
for index in range(1,11):
    restul = index + 2
    if restul == 7:
        continue
    print(restul)
    print("end of continue loop")
# pass占位符，暂时什么都不干，等待后续补充
for index in range(1,11):
    restul = index + 2
    if restul > 7:
        pass
    print(restul)
    print("end of pass loop")
# %%