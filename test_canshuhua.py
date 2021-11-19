import unittest
from parameterized import parameterized
from login import login
from HTMLTestRunner import HTMLTestRunner


class TestLogin(unittest.TestCase):
    data = [("登录成功", 'admin', '123'), ('用户名不能为空', '', '123')]

    @parameterized.expand(data)
    def test_login(self, expand, x, y):
        self.assertEqual(expand, login(x, y))


# suite = unittest.TestSuite()
# suite.addTest(TestLogin('test_login'))
# runner = unittest.TextTestRunner()
# runner.run(suite)


