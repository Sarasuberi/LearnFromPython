import os
from action.action import Action
from action.creat_student_action import CreateStudentAction
from action.delete_student_action import DeleteStudentAction
# 抽象类
# 什么是抽象类
# 抽象类是一个不能被实例化的类，抽象方法是一个没有具体实现的方法，一个抽象类可以有或者没有抽象方法
# Python并没有直接支持抽象类，但是提供了一个模块abc来允许定义抽象类和抽象方法
# 感觉相当于是个模具，被继承之后无论里面实现了什么首先要实现已经被定义的抽象方法
# 如何定义抽象类
# 如何定义抽象方法
# 实例定义请看action文件夹

def execute_action(action: Action):
    action.execute()
    
def main():
    # action  = Action() # Action是一个抽象类，不能被实例化
    
    create = CreateStudentAction() # CreateStudentAction是一个具体类，可以被实例化
    delete = DeleteStudentAction() # DeleteStudentAction是一个具体类，可以被实例化
    
    execute_action(create)
    execute_action(delete)
    
if __name__ == '__main__':
    main()