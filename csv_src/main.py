from command.user_command import get_user_command, process_command
from store.csv_store import *


def main():
    student_data = load_data()
    try:
        if student_data is not None:
            while True:
                command = get_user_command()
                if command == 'exit' and student_data is not None:
                    if not save_data(student_data):
                        print("Data is not saved")
                    else:
                        break
                process_command(command, student_data)
        else:
            print("The data is no information")
    except Exception as e:
        print(f"An error occurred:{e} ")

if __name__ == '__main__':
    main()
