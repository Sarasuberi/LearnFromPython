import unittest
from unittest.mock import patch,MagicMock
from mypj.service.product_service import ProductService

class TestProductService(unittest.TestCase):

    def setUp(self)->None:
           self.service = ProductService()
       
    def tearDown(self)->None:
        self.service = None
    
    @patch('mypj.service.product_service.urlopen')
    @patch('mypj.service.product_service.Requests.__new__')
    def test_download_img_with_exception(self,request_mock,urlopen_mock):
        
        # Setup
        url = "https://www.baidu.com/a.jpg"
        urlopen_return_mock = MagicMock()
        webfile_mock = MagicMock()
        urlopen_mock.return_value = urlopen_return_mock
        urlopen_return_mock.__enter__.return_value = webfile_mock
        webfile_mock.read.return_value = None
        
        # Assert
        with self.assertRaises(Exception):
            # Action
            self.service.download_img(url)
    
    @patch('builtins.open')
    @patch('os.path.basename')
    @patch('mypj.service.product_service.urlopen')
    @patch('mypj.service.product_service.Requests.__new__')
    def test_download_img_with_success(self,request_mock,urlopen_mock,base_name_mock,open_mock):
        
        # Setup
        url = "https://www.baidu.com/a.jpg"
        urlopen_return_mock = MagicMock()
        webfile_mock = MagicMock()
        urlopen_mock.return_value = urlopen_return_mock
        urlopen_return_mock.__enter__.return_value = webfile_mock
        webfile_mock.read.return_value = "Not None"
        base_name_mock.return_value = "a.jpg"
        
        # Action
        result = self.service.download_img(url)
            
        # Assert
        self.assertEqual(result, "Download image successfully, a.jpg")
