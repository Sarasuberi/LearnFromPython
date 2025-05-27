from store.csv_store import save_data
from common.name_def import SUBJECT_NAME_SET

def process_list(data:dict):
    records = list(data.values())
    for record in records:
        print(record.get("name"))
        print(f"Chinese score: {record.get('chinese')}")
        print(f"Math score: {record.get('math')}")
        print(f"English score: {record.get('english')}")
        print(" ")

def process_add(data: dict):
    student_name = input("Please input the student name:")
    if student_name in data:
        print("The student name already exists.")
        return
    elif student_name == "":
        print("The student name cannot be empty.")
        return
    chinese_sorce = validate_score("chinese")
    second = validate_score("math")
    third = validate_score("english")
    new_data = {
        student_name: {
            "name": student_name,
            "chinese": chinese_sorce,
            "math": second,
            "english": third
        }
    }
    data.update(new_data)
    if save_data(data):
        print("Add successfully.")
    else:
        print("Add failed.")

def validate_score(subject:str):
    score = int(input(f"Please input the {subject} score:"))
    if score == "":
        return ValueError("Please enter score")
    if score > 100 or score < 0:
        return ValueError("Please enter right score")
    return score

def process_edit(data: dict):
    student_name = input("Please input the student name:")
    if student_name not in data:
        print(f"Student:{student_name} not exist!")
        return
    elif student_name == "":
        print("The student name cannot be empty.")
        return
    try:
        subject = input(
            "Please input the subject you want to edit (chinese, math, english):"
        )
        if subject == "":
            print("Subject cannot be empty.")
            return
        if subject not in SUBJECT_NAME_SET:
            print("Please enter the right subject name.")
            return
        data[student_name][subject] = validate_score(subject)
        print("Edit finished.")
    except Exception as e:
        print(f"Edit error: {e}")

def process_delete(data: dict):
    student_name = input("Please input the student name:")
    if student_name in data.keys():
        # data.pop(student_name)
        del data[student_name]
        print(f'Delete student:{student_name} successfully!')
    else:
        print(f'Student:{student_name} not exist!')

def process_average(data: dict):
    student_count = len(data)
    if student_count == 0:
        print("No student data.")
        return
    average_total = {}
    for socre in SUBJECT_NAME_SET:
        average_total[socre] = 0
    for record in data.values():
        for socre in SUBJECT_NAME_SET:
            average_total[socre] += int(record[socre])
    for subject in SUBJECT_NAME_SET:
        average = average_total[subject] / student_count
        print(f"Average of {subject} is: {average}")
