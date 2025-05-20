import math
import json


a = 2
print("a的3次方是：" + str(a ** 3))
b = 10000
c = 10_000
print("b的值是：" + str(type(b)) + str(b) + ",c的值是：" + str(type(c)) + str(c))\

restal = ('')
print(bool(restal))

# 这里定义一个价格变化律
ratio = 1.2
price = 100 # 初始价格
price = price * ratio #提价

a = 1
b = 2
c = 3
if a == 1 and b == 2 and \
    c == 3:
    print('''\让一句话多行编写，
三个引号可以让字符串换行继续写，并且包含了反斜杠的换行符''')
    
age = 12
print(age)
print('添加一个age变量并且赋值12，变量类型是由后面的值决定')
age = 24
print(age)
print( '同一个变量可以被重复赋值并且覆写原值')
age = '二十三'
print(age)
print( '试一下修改变量的类型，可以这样但是容易引起内存溢出的问题，但是好像会被GC？')

msg = 'hello \\ world \n my fist \'python\' program'
print(msg)
desc = r'This is \ hello\ world'
print(desc)

greeting = 'hello'
name = 'world'
message = greeting + ', ' + name + '!'
print(message)
desc = 'asdfghjkl'\
    'qwertyuiop'
print(desc)
print(f'{greeting}, {name}!')
desc_length = len(desc)
print(desc_length)
print(desc[1])
print(desc[0:5])
print(desc[0:])
print(desc[:5])
print(desc[0:5:2])

