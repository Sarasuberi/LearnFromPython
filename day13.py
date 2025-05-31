import os

def cmd():
   # 当前工作目录
    # 获取当前路径 os.getcwd()函数
    # 改变当前路径 os.chdir()函数
    print("当前工作目录:", os.getcwd())
    change_path = os.chdir("mysub")
    print("改变后的工作目录:", os.getcwd())
    # 创建新文件夹 os.mkdir()函数
    os.mkdir("mysub2")
    # 重命名文件夹 os.rename()函数
    os.rename("mysub2", "new_mysub")
    # 删除文件夹 os.rmdir()函数
    os.rmdir("new_mysub")

# 遍历文件夹
def print_dir(root_dit:str):
    for root, dirs, files in os.walk(root_dit):
        print("当前目录:", root)
        print("子目录:", dirs)
        print("文件:", files)

if __name__ == '__main__':
    cmd()
    print_dir(".")
    print_dir("new_mysub")  
    print("操作完成！")