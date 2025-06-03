# 多继承
# 多继承的语法
# 同名函数的继承问题
# 会继承第一个父类的同名函数

class Parent1:

    def render(self):
        print("parent1")
    def hello(self):
        print("Hello parent1")

class Parent2:
    def render(self):
        print("parent2")
    def hello(self):
        print("Hello parent2")


class Child(Parent1, Parent2):

    def render(self):
        Parent2.render(self)
    def hello(self):
        super().hello()


def main():
    child = Child()
    child.render()
    child.hello()


if __name__ == '__main__':
    main()
