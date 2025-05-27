import csv
import os
from common.name_def import SUBJECT_NAME_SET
file = "csv_students.csv"

def load_data() -> dict:
    data = {}
    try:
        if os.path.exists(file):
            with open(file,"r",encoding="utf-8",newline="") as file_instance:
                csv_read = csv.DictReader(file_instance)
                for row in csv_read:
                    name = row.get("name")
                    data[name] = row
            return data
        else:
            with open(file,"w",encoding="utf-8",newline="") as file_instance:
                csv_write = csv.DictWriter(file_instance,fieldnames=["name","chinese","math","english"])
                csv_write.writeheader()
                print("File created")
                load_data()
    except Exception as e:
        print(f"List Error: {e}")
    except FileNotFoundError:
        print("File not found")



def save_data(data: dict) -> bool:
    try:
        with open(file, "w", encoding="utf-8", newline="") as file_instance:
            if len(data) > 0:
                rows = list(data.values())
                headers = SUBJECT_NAME_SET.union({"name"})
                csv.writer = csv.DictWriter(file_instance, headers)
                csv.writer.writeheader()
                csv.writer.writerows(rows)
                return True
            else:
                return False
    except Exception as e:
        print(f"Save_data Error: {e}")
