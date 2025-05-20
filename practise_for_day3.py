# for循环小练习
# 输入两个数，计算从第一个数累加到第二个数的总和。比如输入1和5就应该计算1+2+3+4+5的结果

sum = 0
tip = 'Please enter the number'
str_num1 = input(tip + '1:')
str_num2 = input(tip + '2:')
start = int(str_num1)
stop = int(str_num2) + 1
for i in range(start,stop):
    sum = sum + i
print(f'Summary:{sum}')

# %%
# while循环小练习
# 提示用户输入成绩，回车后打印成绩的优良等级，并继续等待用户输入下一个成绩，以此类推，直到用户输入exit退出程序。打印成绩的平均值并退出程序
sum = 0
count = 0
result = 0
running = True
tip = 'Please enter the grade , enter exit to quit:'
while running :
    str_input = input(tip)
    if str_input == 'exit':
        running = False
        if count > 0:
            result = sum / count
        print(f'Average:{result}')
    # 如果输入内容不是能识别的exit或者小于100的成绩，则提示用户重新输入
    # elif str_input != range(0,100):
    #   print('Someting was wrong ,Please enter the grade again')
    else:
        grade = int(str_input)
        sum = sum + grade
        count = count + 1
        if grade >= 90:
            print('Excellent')
        elif grade >= 75:
            print('Good')
        elif grade >= 60:
            print('Pass')
        else:
            print('Fail')
        

# %%
