import requests

a = '12'
b = '23'
print(a + b)
a = input('Enter number of a:')
b = input('Enter number of b:')
print(a + b)
print(int(a) + int(b))

score = input('Enter your score:')
if int(score) >= 90:
    print('A')
elif int(score) >= 80:
    print('B')
elif int(score) >= 70:
    print('C')
elif int(score) >= 60:
    print('D')
else:
    print('E')
restal = 'RED' if int(score) >= 90 else 'BLUE' #三元运算符，相当于if else
print(restal)