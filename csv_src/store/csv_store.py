import csv
import os
from common.name_def import SUBJECT_NAME_SET

file = "csv_students.csv"


def load_data() -> dict:
    data = {}
    try:
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8",
                      newline="") as file_instance:
                csv_read = csv.DictReader(file_instance)
                for row in csv_read:
                    name = row.get("name")
                    data[name] = row
        else:
            with open(file, "w", encoding="utf-8",
                      newline="") as file_instance:
                csv_write = csv.DictWriter(
                    file_instance,
                    fieldnames=["name", "chinese", "math", "english"])
                csv_write.writeheader()
                print("File created")
                load_data()
        return data
    except Exception as e:
        print(f"List Error: {e}")
        return data


def save_data(data: dict) -> bool:
    if len(data) < 0:
        print("No data to save.")
        return False
    rows = list(data.values())
    try:
        with open(file, "w", encoding="utf-8", newline="") as file_instance:
            headers = SUBJECT_NAME_SET.union({"name"})
            csv_write = csv.DictWriter(file_instance, headers)
            csv_write.writeheader()
            csv_write.writerows(rows)
            return True
    except Exception as e:
        print(f"Save_data Error: {e}")
        return False