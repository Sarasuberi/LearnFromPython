import os
# 常用的特殊方法
# __str__
# __str__方法用于返回一个描述对象本身的字符串，该描述主要面对用户
#
# __repr__
# __repr__方法用于返回一个描述对象本身的字符串，该描述主要目标是机器或者开发者
#
# __eq__
# __eq__方法用于判断两个对象是否相等，如果相等返回True，否则返回False
#
# __hash__
# __hash__方法用于返回一个对象的哈希值，该哈希值用于判断对象是否在集合中
#
# __bool__
# __bool__方法用于判断对象是否为真，如果为真返回True，否则返回False
# 如果类没有实现这个方法，那么__len__将会被用户求解布尔值
#
# __del__
# __del__方法用于在对象被销毁时自动调用，可以用于做一些清理工作
# 因为不知道对象何时被回收，所以不要依赖于这个方法去做一些重要的事情

class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        print('str is called')
        return f'{self.year}年{self.month}月{self.day}日'

    def __repr__(self):
        print('repr is called')
        return f'MyDate:{self.year}-{self.month}-{self.day}'
    
    def __eq__(self, other):
        print('eq is called')
        if not isinstance(other, MyDate):
            return False
        return self.year == other.year and self.month == other.month and self.day == other.day
    
    def __hash__(self):
        print('hash is called')
        return hash((self.year + self.month * 101 + self.day * 101))
    
    def __bool__(self):
        print('bool is called')
        return self.year > 2021 
    
    def __del__(self):
        print('del is called')
    
def main():
    my_date_1 = MyDate(2022, 11, 3)
    my_date_2 = MyDate(2022, 11, 3)
    my_date_5 = MyDate(2022, 11, 3)
    my_date_3 = my_date_1
    print(my_date_1)
    print(str(my_date_1))
    print(repr(my_date_1))
    
    my_date_5 = None
    
    print(my_date_1 is my_date_3)
    print(my_date_1 == my_date_2)
    
    date_set = set()
    date_set.add(my_date_1)
    print(hash(my_date_1))
    
    my_date_4 = MyDate(2020, 2, 1)
    print(bool(my_date_1))
    print(bool(my_date_4))          
    
if __name__ == '__main__':
    main()