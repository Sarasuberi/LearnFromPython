# 生成20页，每页54个不重复的题目，被乘数2-12，乘数2-99
# 每页分成3列，每列18题，竖向排列。
# 生成答案页，按页和题号顺序列出所有题目的乘积
# 同页题目不重复，不同页题目可重复
import csv
import random

# 生成题目
def generate_questions():
    questions = []
    for _ in range(20):
        for i in range(54):
            multiplier = random.randint(2, 99)
            multiplicand = random.randint(2, 12)
            question = f"{multiplicand} x {multiplier}"
            questions.append(question)
    return questions
questions = generate_questions()

# 生成答案
def generate_answers(questions):
    answers = []
    for question in questions:
        multiplicand, multiplier = map(int, question.split(' x '))
        answer = multiplicand * multiplier
        answers.append(answer)
    return answers

answers = generate_answers(questions)

# 生成试卷
def generate_exam(questions):
    exam = []
    for i in range(20):
        page_questions = questions[i*54:(i+1)*54]
        page_exam = []
        for j in range(0, 54, 18):
            page_exam.append(page_questions[j:j+18])
        exam.append(page_exam)
    return exam

exam = generate_exam(questions)

# 生成csv文件
def generate_csv(questions, answers, exam):
    with open('questions.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Page', 'Question', 'Answer'])
        for i in range(20):
            for j in range(54):
                writer.writerow([i+1, questions[i*54+j], answers[i*54+j]])

    with open('exam.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Page', 'Question'])
        for i in range(20):
            for j in range(54):
                writer.writerow([i+1, exam[i][j//18][j%18]])

generate_csv(questions, answers, exam)

if __name__ == '__main__':
    print("生成成功！")
