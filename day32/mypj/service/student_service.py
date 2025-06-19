from mypj.domain.student import Student


def find_student_by_id(id: int) -> Student:
    # query database
    return Student(1, 'Tom')


def save_student(student: Student):
    print(f'save student {student.id}:{student.name}')


def change_name(student_id: int, name: str):
    student = find_student_by_id(student_id)

    if student is not None:
        student.name = name
        save_student(student)
