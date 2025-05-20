# 用户输入一个成绩，打印出成绩的优良等级 
# <0或者>100：无效成绩
# 0~59:不及格
# 60~75:及格
# 76~85:良好
# 86~100:优秀

score = int(input("请输入成绩："))

if score < 0 or score > 100:
    print("无效成绩")
elif score <= 59:
    print("不及格") 
elif score <= 75:
    print("及格")
elif score <= 85:
    print("良好")
else:
    print("优秀")


tip = 'Please input your grade:' #用变量存储可能重复使用的内容，方便使用
str_grade = input(tip)
grade = int(str_grade)
if grade < 0 or grade > 100:   
    print('Invalid grade')
elif grade < 60:
    print('Fail')
elif grade < 76:
    print('Pass')
elif grade < 86:
    print('Good')
else:
    print('Excellent')