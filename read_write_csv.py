# 读写CSV文件
# file_instance_csv = open(path_to_file, encoding='utf-8')
# csv_reader = csv.reader(file_instance_csv)
# for row in csv_reader:
#     print(row)
import csv
def read_csv(filename):
    file_instance = open(filename, encoding='utf-8')
    csv_reader = csv.reader(file_instance)
    for line in csv_reader:
        print(line)
    file_instance.close()

def write_csv(filename):
    file_instance = open(filename, 'w', encoding='utf-8',newline='')
    csv_writer = csv.writer(file_instance) # 写入一行
    header = ['Name', 'Chinese', 'English', 'Math']
    rows = [
        ['Zhangsan', 80, 87, 100],
        ['Lisi', 78, 79, 98],
        ['Wangwu', 67, 90, 88]
    ]
    csv_writer.writerow(header)
    csv_writer.writerows(rows)
    file_instance.close()


def dict_write_csv(filename):
    file_instance = open(filename, 'w', encoding='utf-8', newline='')
    # with open(filename, 'w', encoding='utf-8' , newline='') as file_instance:
    # 询问了DeepSeek为什么写入的时候会多加空行，发现是newline=''的原因，并且close（）方法存在资源泄露，推荐使用with语句来避免这个问题
    header = ['Name', 'Chinese', 'English', 'Math']
    csv_writer = csv.DictWriter(file_instance, header)
    rows = [{
        'Name': 'Zhangsan',
        'Chinese': 80,
        'English': 87,
        'Math': 100
    }, {
        'Name': 'Lisi',
        'Chinese': 78,
        'English': 79,
        'Math': 98
    }, {
        'Name': 'Wangwu',
        'Chinese': 67,
        'English': 90,
        'Math': 88
    }]
    csv_writer.writeheader()
    csv_writer.writerows(rows)
    file_instance.close()

if __name__ == "__main__":
    filename = 'students2.csv'
    #write_csv(filename)
    dict_write_csv(filename)
    read_csv(filename)
    print('Done')