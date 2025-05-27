from command.process_command import process_list,process_add,process_edit,process_delete,process_average
from common.name_def import COMMAND_LIST


def get_user_command() -> str:
    print("=============================================")
    print("list: add a list")
    print("add: add a student and grade")
    print("edit: edit a student and grade")
    print("delete: delete a student and grade")
    print("average: print the average grade of subject")
    print("exit: exit the program")
    while True:
        command = input("Please input commond: ")
        cmd = command.lower()
        if cmd not in COMMAND_LIST:
            print(f"{command} is not right commond")
        else:
            return cmd

def process_command(command:str,data:dict):
    if command == 'list':
        process_list(data)
    elif command == 'add':
        process_add(data)
    elif command == 'edit':
        process_edit(data)
    elif command == 'delete':
        process_delete(data)
    elif command == 'average':
        process_average(data)
