from csv_store import *
from user_command import *

def main():
    csv_data = load_data()
    try:
        if csv_data is not None:
            while True:
                command = get_user_command()
                if command == 'exit' and csv_data is not None:
                    if not save_data(csv_data):
                        print("Data is not saved")
                    else:
                        break
                process_command(command, csv_data)
        else:
            print("The data is no information")
    except Exception as e:
        print(f"An error occurred:{e} ")


if __name__ == '__main__':
    main()
