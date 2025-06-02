from abc import ABC, abstractmethod

# 通过继承abc.ABC类来定义抽象类，并使用@abstractmethod装饰器来定义抽象方法
class Action(ABC):
    @abstractmethod
    def execute(self):
       pass