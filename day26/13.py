# 单例模式
# 什么是单例模式
# 单例模式的根本目的就是要让一个类只能制造出一个对象
# 单例的需求一般是针对需要共享数据的对象
# 1.工厂对象
# 2.数据库连接池对象
# 3.任何其他想要所有人共享的对象
# 单例模式，常见的实现方式有5种
# 使用模块，也就是import：最简单直接且安全，推荐使用
# 使用装饰器：不能被继承，不推荐使用
# 使用 classmethod ：不推荐使用
# 使用 new 方法：需要开发成员有共同的技术背景，对Python有足够的认识，不然代码会有BUG。
# 使用 metaclass：完美的单例实践，也推荐使用
# 视频中示例1的 装饰器，被装饰的类将无法被继承（因为被装饰的类变成了函数）
# 视频中示例2的 metaclass 示例也存在多线程的安全隐患，应该在元类的 __call__ 部分加锁
# 单纯使用普通类的 new 方法的时候，也是会涉及到继承问题
# 就是使用 _instance 会被子类继承，除非每个子类手动声明 _instance = None
# 而使用 __instance 的话，则会因为 python 的机制，导致使用 hasattr 判定的话，__instance 会变形为 _类名__instance。
# 单例模式代码实现


# 示例1
def singleton(cls):
    
    # 闭包的方式实现单例模式
    _instance = {}
    def inner(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]
        
        # 创建类并且添加对象__instance
        obj = cls(*args, **kwargs)
        _instance[cls] = obj
        return obj
    return inner

def singletons(cls):
    def inner(*args, **kwargs):
        
        # 如果类中含有__instance对象则直接返回对象，不创建新的
        if hasattr(cls,'__instance'):
            return getattr(cls,'__instance')
        
        # 创建类并且添加对象__instance
        obj = cls(*args, **kwargs)
        setattr(cls,'__instance',obj)
        return obj
    return inner

# 示例2
class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if hasattr(cls, '_instance'):
            return getattr(cls, '_instance')
        obj = super().__call__(*args, **kwargs)
        setattr(cls, '_instance', obj)
        return obj


# @singleton
# @singletons
class Person(metaclass=SingletonMeta):
    pass


p_1 = Person()
p_2 = Person()

print(p_1 is p_2)