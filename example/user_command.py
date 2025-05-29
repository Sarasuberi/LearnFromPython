from define import *
from process_command import *

def get_user_command() -> str:
    print("=============================================")
    print("list: show a list")
    print("cc: clear the data")
    print("go: Start inputting parameters")
    print("exit: exit the program")
    while True:
        command = input("Please input commond: ")
        cmd = command.lower()
        if cmd not in COMMAND_LIST:
            print(f"{command} is not right commond")
        else:
            return cmd


def process_command(command: str, data: dict):
    if command == 'list':
        process_list(data)
    elif command == 'go':
        process_go(data)
    elif command == 'cc':
        process_cc(data)