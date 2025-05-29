import random
from define import *
from csv_store import save_data

questions = []
answers = []
symbol = []
def process_list(data:dict):
    records = list(data.values())
    for record in records:
        print(record.get("page"))
        print(f"Number: {record.get('number')}")
        print(f"Formula: {record.get('formula')}")
        print(f"Answer: {record.get('answer')}")
        print(" ")

def process_cc(data: dict):
    try:
        data.clear()  # 清空数据字典
        if save_data(data):
            print("数据清空成功.")
            # print("Data cleared successfully.")
    except Exception as e:
        print("数据清空失败")
        # print("Failed to clear data.")
        print(f"Error: {e}")


def process_go(data: dict):
    max_number = int(input("请输入最大值: "))
    quantity = int(input("请输入题目数量: "))
    number = int(input("请输入计算项数: "))

    # 验证输入
    if number == 0:
        print("项数不能为0！")
        return
    if number > 5:
        print("请输入5以下的数字")
        return

    symbol = []  # 存储运算符
    for i in range(1, number):  # 运算符数量 = 操作数 - 1
        operator = input(f"请输入第 {i}个运算符: ")
        #operator = input(f"Enter the operator {i}: ")
        if operator not in OPERATOR:
            print("无效的运算符")
            #print("Invalid operator")
            return
        symbol.append(operator)

    questions = []  # 存储所有题目
    answers = []    # 存储所有答案

    # 生成题目及答案
    # 设置答案的最大值，如果超过就跳过这题
    max_result = int(input("请输入答案的最大值: "))
    for _ in range(quantity):
        # 生成单个题目
        question_str = ""

        # 生成第一个操作数
        num = random.randint(0, max_number)
        question_str += str(num)

        # 生成后续操作数和运算符
        for j in range(number - 1):  # 运算符数量 = 操作数 - 1
            op = random.choice(symbol)# 随机选择运算符
            # 根据运算符生成合适的操作数
            if op == '/':
                num = random.randint(1, max_number)
            elif op == '*':
                num = random.randint(1, max_number)
            else:
                num = random.randint(0, max_number)

            question_str += ' ' + op + ' ' + str(num)

        # 计算当前题目的答案
        try:
            # 使用更安全的计算方式
            # eval函数会执行字符串中的代码，如果字符串中包含恶意代码，可能会导致安全问题
            result = safe_eval(question_str)
            if result > max_result:
                # del question_str
                print(f"跳过了{question_str} 个因为答案大于最大值的题")
                # print(f"Skip question: {question_str} (answer exceeds maximum)")
                continue
            else:
                questions.append(question_str + ' = ')  # 字符串拼接等号
                answers.append(result)
        except ZeroDivisionError:
            print(f"跳过了{question_str} 个因为0的题")
            # print(f"Skip question: {question_str} (zero division error)")
        except Exception as e:
            print(f"跳过了{question_str} 个因为其他问题的的题")
            # print(f"Skip question: {question_str} (Error: {e})")

    # 将问题及答案存入data字典
    for i in range(len(questions)):
        data[i] = {
            'formula': questions[i],
            'answer': answers[i],
            'page': f'Page:{i // 100 + 1}',  # 每100题一页
            'number': i + 1
        }

    print(f"成功生成了{len(questions)}个题 ")
    # print(f"{len(questions)} sets of questions generated successfully")

# 更安全的计算函数
def safe_eval(expression):
    """安全计算数学表达式"""
    # 限制允许的运算符
    allowed_chars = set("0123456789+-*/. ()")
    if not set(expression) <= allowed_chars:
        raise ValueError("含有错误的字符")
        # raise ValueError("Invalid characters in expression")

    # 使用更安全的计算方式
    return eval(expression, {"__builtins__": None}, {})
