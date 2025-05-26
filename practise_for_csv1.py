# 编写一个小的基于命令行交互的软件，能够增加、修改、查看学生的成绩记录以及能打印出学科平均分，并保存在CSV文件中。
# AI自动生成的
import csv

def add_student():
    student_name = input("请输入学生姓名：")
    student_score = input("请输入学生成绩：")
    with open('student_scores.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([student_name, student_score])

def modify_student():
    student_name = input("请输入要修改的学生姓名：")
    new_score = input("请输入新的成绩：")
    with open('student_scores.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    for i in range(len(rows)):
        if rows[i][0] == student_name:
            rows[i][1] = new_score
            break
    with open('student_scores.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

def view_student():
    with open('student_scores.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def print_average():
    with open('student_scores.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        total_score = 0
        count = 0
        for row in reader:
            total_score += float(row[1])
            count += 1
        average_score = total_score / count
        print("学科平均分：", int(average_score))

while True:
    print("1. 添加学生成绩")
    print("2. 修改学生成绩")
    print("3. 查看学生成绩")
    print("4. 计算学科平均分")
    print("5. 退出")
    choice = input("请输入您的选择：")
    if choice == '1':
        add_student()
    elif choice == '2':
        modify_student()
    elif choice == '3':
        view_student()
    elif choice == '4':
        print_average()
    elif choice == '5':
        break
    else:
        print("无效的选择，请重新输入")
