# %%
# 操作文件
# open()函数 read()方法 write()方法 close()方法 readline()方法 readlines()方法
# open(path_to_file, mode)
# mode: 'r' 只读模式，'w' 写入模式会覆写，'a' 追加模式，'b' 二进制模式，'t' 文本模式，'+' 更新模式，'x' 创建模式
file_instance_read = open('E:\\VSCodePorject\\LearnFromPython\\sample.txt', 'r')
while True:
    line = file_instance_read.readline()
    if line == '':
        break
    print(f'while循环读文件\n {line}')
file_instance_read.close()
# %%
file_instance_write = open('E:\\VSCodePorject\\LearnFromPython\\sample.txt', 'a')
file_instance_write.write('This is new line.\n')
file_instance_write.close()
file_instance_write_read = open('E:\\VSCodePorject\\LearnFromPython\\sample.txt', 'r')
while True:
    line = file_instance_write_read.readline()
    if line == '':
        break
    print(f'write()方法:\n {line}')
file_instance_write_read.close()
# %%
import os.path as path
import os
from pathlib import Path
file_instance_create = open('new_file.txt', 'x')
file_instance_create.write('This is new file.\n')
file_instance_create.close()
print(path.exists('new_file.txt'))
print(path.isfile('new_file.txt'))# 检测是文件名还是路径名，如果是文件名返回true
print(path.isdir('new_file.txt'))# 检测是文件名还是路径名，如果是路径名返回true

path = Path('new_file.txt')
print(path.exists())
print(path.is_file())# 检测是文件名还是路径名，如果是文件名返回true
print(path.is_dir())# 检测是文件名还是路径名，如果是路径名返回true

os.rename('new_file.txt', 'new_file2.txt')
os.remove('new_file2.txt')