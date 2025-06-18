import unittest
from mypj.assert_methods.my_service import MyService


class TestMyService(unittest.TestCase):
    def test_download_img(self):

        # Setup
        my_service = MyService()

        # Action
        result = my_service.download_img("http://xxxxxxx.com")

        # Assert
        # self.assertEqual(True,result)
        self.assertTrue(result)

    def test_download_img_with_exception(self):

        # Setup
        my_service = MyService()

        # Assert
        with self.assertRaises(Exception):
            # Action
            my_service.download_img(None)
