from enum import Enum, unique
# 枚举
# 为什么需要枚举
# 当代那种的数值不利于人来阅读的时候，总希望能够有一个既方便阅读又利于查错的方法
# 如何定义枚举
# 通过继承enum.Enum来定义枚举类
# 枚举成员的name和value
# 每个成员本身的变量名就是他的name，所赋值的整数就是他的value
# 通过neme和value获取枚举成员
# 遍历枚举成员
# 枚举本身是可以迭代的
# 枚举的继承
# 枚举是可以继承其他没有成员的枚举，有成员的枚举不能被继承

class Gender(Enum):
    MALE = 1    # 成员1
    FEMALE = 2  # 成员2
    
class Student:
    def __init__(self,gender:Gender) -> None:
        self.gender = Gender.MALE
        
def main():
    print(type(Gender.MALE))
    print(Gender.MALE.name)
    print(Gender.MALE.value)

    student = Student(Gender.FEMALE)
    
    if student.gender == Gender.FEMALE:
        print('female')
    else:
        print('male')
        
    s_gender = "MALE"
    student.gender = Gender[s_gender]
    print(student.gender)
    
    i_gender = 2
    print(Gender(i_gender))
    
    for gender in Gender:
        print(f"for:{gender}")
        
if __name__ == '__main__':
    main()