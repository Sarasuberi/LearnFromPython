import unittest
from unittest.mock import patch,Mock
from mypj.service import student_service


class TestStudentService(unittest.TestCase):
    
    # 装饰器方式
    @patch("mypj.service.student_service.save_student")
    @patch("mypj.service.student_service.find_student_by_id")
    def test_change_name_decorator(self,find_student_mock,save_student_mock):
        # 逆序传参
        
        # Setup
        student = Mock(id=1,name='Tom')
        find_student_mock.return_value = student
        
        # Action
        student_service.change_name(1,'Jack')
        
        # Assert
        self.assertEqual(student.name,'Jack')
    
    # 上下文管理器方式
    # @patch("mypj.service.student_service.find_student_by_id")
    def test_change_name_contextmanager(self,find_student_mock):
        
        # Setup
        student = Mock(id=1,name='Tom')
        
        
        with patch("mypj.service.student_service.find_student_by_id") as find_student_mock,\
                patch("mypj.service.student_service.save_student") as save_student_mock:
            find_student_mock.return_value = student
            
            # Action
            student_service.change_name(1,'Jack')
            
            # Assert
            self.assertEqual(student.name,'Jack')
            
    
    # 手动方式
    @patch("mypj.service.student_service.find_student_by_id")
    def test_change_name_manual(self,find_student_mock):
        
        # Setup
        student = Mock(id=1,name='Tom')
        find_student_mock.return_value = student
        
        pather =  patch("mypj.service.student_service.save_student")
        pather.start()
            
        # Action
        student_service.change_name(1,'Jack')
        
        pather.stop()
            
        # Assert
        self.assertEqual(student.name,'Jack')