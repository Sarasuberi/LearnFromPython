# 编写一个小的基于命令行交互的软件，能够增加、修改、查看学生的成绩记录以及能打印出学科平均分，并保存在CSV文件中。
# 自己写的
import csv

FILENAEM = "practise_for_csv1_myself.csv"
def list_cvs():
    try:
        with open(FILENAEM, "r",newline='') as file_instance:
            csv_reader = csv.reader(file_instance)
            #print("\t".join(next(csv_reader)))
            for row in csv_reader:
                print("\t".join(row))

    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)

def add_cvs():
    try:
        new_rows = []
        with open(FILENAEM, "r",newline='',encoding="utf-8") as file_instance:
            csv_reader = csv.reader(file_instance)
            headers = next(csv_reader)
            student_name = input("Please input the student name:")
            if student_name == "":
                print("Student name cannot be empty!")
                return
            first_score = validate_score(headers[1])
            second_score = validate_score(headers[2])
            third_score = validate_score(headers[3])
            new_rows.append([student_name, first_score, second_score, third_score])
        with open(FILENAEM, "a", newline='',encoding= "utf-8") as file_instance:
            csv_writer = csv.writer(file_instance)
            csv_writer.writerows(new_rows)
            print("Add successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)

def validate_score(subject):
    # 输入科目成绩
    score = input(f"Please input the {subject} score:")
    # 如果输入为空，则抛出异常
    if score == "":
        return ValueError("Please enter right score")
    # 返回成绩
    return score

def edit_cvs():
    student_name = input("Please input the student name:")
    if student_name == "":
        print("Student name cannot be empty!")
        return
    update_rows = []
    found = False
    try:
        with open(FILENAEM, "r", newline='') as file_instance:
            csv_reader = csv.reader(file_instance)
            headers = next(csv_reader)# 跳过表头
            for row in csv_reader:
                if row[0] == student_name:
                    found = True
                    print(f'chinese score is {row[1]},  english score is {row[2]},   math score is {row[3]}')
                    subject = input(
                        "Please input the subject(chinese,english,math):").lower()
                    if subject not in ["chinese", "english", "math"]:
                        print("Invalid subject")
                        return
                    new_score = input(
                        f"Please input the new score:")
                    if new_score == "":
                        print("Score cannot be empty!")
                        return
                    index = headers.index(subject)# 获取科目索引
                    row[index] = new_score
                update_rows.append(row)
                if not found:
                    print("Student not found!")
                    return
        with open(FILENAEM, "w", newline='') as file_instance:
            csv_writer = csv.writer(file_instance)
            csv_writer.writerow(headers)
            csv_writer.writerows(update_rows)
        print("Update successfully!")
    except Exception as e:
        print("Operation filed:", e)

def delete_cvs():
    student_name = input("Please input the student name:")
    try:
        new_rows = []
        found = False
        with open(FILENAEM, "r", newline='',encoding='utf-8') as file_instance:
            csv_reader = csv.reader(file_instance)
            rows = list(csv_reader)
            for row in rows:
                if row[0] == student_name:
                    found = True
                else:
                    new_rows.append(row)
            if not found:
                print("Student not found!")
                return
        with open(FILENAEM, "w", newline='', encoding='utf-8') as file_instance:
            csv_writer = csv.writer(file_instance)
            csv_writer.writerows(new_rows)
            print("Delete successfully!")
    except FileNotFoundError as e:
        print("File not found!", e)

def average_cvs():
    try:
        total_score_chinese = 0
        total_score_english = 0
        total_score_math = 0
        count = 0
        with open(FILENAEM, "r",newline='',encoding="utf-8") as file_instance:
            csv_reader = csv.reader(file_instance)
            for row in csv_reader:
                total_score_chinese += int(row[1])
                total_score_english += int(row[2])
                total_score_math += int(row[3])
                count += 1
            if count == 0:
                print("No data!")
        print(f"Chinese average:{ int(total_score_chinese / count)}")
        print(f"English average:{ int(total_score_english / count)}")
        print(f"Math average:{ int(total_score_math / count)}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Operation completed")

if __name__ == "__main__":
    while True:
        print("  ")
        print("list: add a list")
        print("add: add a student and grade")
        print("edit: edit a student and grade")
        print("delete: delete a student and grade")
        print("average: print the average grade of subject")
        print("exit: exit the program")
        choice = input("Please input command:")
        if choice == "list":
            list_cvs()
        elif choice == "add":
            add_cvs()
        elif choice == "edit":
            edit_cvs()
        elif choice == "delete":
            delete_cvs()
        elif choice == "average":
            average_cvs()
        elif choice == "exit":
            break
        else:
            print("Invalid command, please try again.")
