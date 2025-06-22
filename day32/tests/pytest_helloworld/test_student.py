import sys
import pytest
from mypj.domain.student import Student


# 定义一个函数，用于判断当前操作系统是否为Mac
def is_skip():
    # 返回当前操作系统是否为Mac
    return sys.platform.casefold() == "darwin".casefold()
    # 返回当前操作系统是否为Linux
    # return sys.platform.casefold() == "linux".casefold()
    # 返回当前操作系统是否为Mac
    # return sys.platform.casefold() == "mac".casefold()

@pytest.mark.skipif(is_skip(), reason="skip on mac")
def test_student():
    print("test_student __init__")
    
    # Action
    student = Student(id=1, name="Tom")
    
    # Assert
    assert student.name == "Tom"
    assert student.id == 1
    
class TestStudent():
    
    @pytest.mark.skip(reason="skip on mac")
    def test_student(self):
        # Action
        student = Student(id=2, name="Jack")

        # Assert
        assert student.name == "Jack"
        assert student.id == 2