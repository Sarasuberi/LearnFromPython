# 使用正则表达式
# 什么是正则表达式
# 正则表达式是一个相对独立而特殊的语言
# 正则表达式提供了很多的格式与符号来定义字符串的模式，通过模式可以对字符串的内容进行
# 1.匹配验证
# 2.搜索
# 正则表达式相关的模块
# 通过引入re模块就可以使用Python提供的正则表达式的支持功能
# 查找与匹配函数


import re


def test_search():
    pattern = r"\d{2}"
    source = "I'm 80 years old."
    result = re.search(pattern, source)
    print(result)

def test_match():
    pattern = r"\d{2}"
    source = "80 years old."
    result = re.match(pattern, source)
    print(result)

def test_fullmatch():
    pattern = r"\d{2}"
    source = "809"
    result = re.fullmatch(pattern, source)
    print(result)

def test_findall():
    pattern = r"\d{2}"
    source = "8 09 aaa  89 laskdjf"
    result = re.findall(pattern, source)
    print(result)

def test_finditer():
    pattern = r"\d{2}"
    source = "8 09 aaa  89 laskdjf"
    it = re.finditer(pattern, source)
    for rs in it:
        # if re.fullmatch('09',source):
        print(rs)
        # break

def test_compile():
    pattern_str = r"\d{2}"
    pattern = re.compile(pattern_str)
    print(pattern.fullmatch("99"))


test_finditer()

test_compile()