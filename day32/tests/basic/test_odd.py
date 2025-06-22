import pytest
from day32.mypj.basic.calculator import Calculator


@pytest.mark.parametrize("num,expected_out", [(1,True),(2,False)])
def test_odd(num:int,expected_out:bool):
    
    # Setup
    cal = Calculator()
    
    # Action
    actual_result = cal.is_odd(num)
    
    # Assert
    assert actual_result == expected_out