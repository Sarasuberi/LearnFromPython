import pytest

from mypj.domain.student import Student


@pytest.fixture
def male_student_fixture():
    student = Student(id=1, name="Jack")

    yield student