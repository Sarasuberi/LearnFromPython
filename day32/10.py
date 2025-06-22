# congtest.py
# congtest.py的用途
# 是的fixture可以被多个文件中的测试用例复用
# congtest.py要卸载tests文件夹下
# 引用所需方法后，pytest会自动调用
# 方式1：直接讲fixture放在conftest.py中
# 方式2：将fixture放在tests文件夹下的其他文件中，并在conftest.py中引用

# 关联 tests\fixtures\male_student_fixture.py和mypj\domain\student.py


import pytest
from mypj.domain.student import Student
from tests.fixtures.male_student_fixture import male_student_fixture


@pytest.fixture
def female_student_fixture():
    student = Student(id=2, name="Mary")
    yield student