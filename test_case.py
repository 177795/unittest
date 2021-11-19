import unittest
from login import login
from parameterized import parameterized


class TestLogin(unittest.TestCase):
    # 实际工作中用到加就可以，不用可以不加
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('执行最开始的初始化')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('清空最终')
    #
    # # 初始化方法
    # def setUp(self) -> None:
    #     print("初始化结束")
    #
    # # 清空方法
    # def tearDown(self) -> None:
    #     print("初始化结束")

    def test_login1(self):
        self.assertEqual("登录成功", login('admin', '123'))
        print("用例执行完毕1")

    def test_login2(self):
        self.assertEqual("用户名不能为", login("", '123'))
        print("用例执行完毕2")


# 添加一条测试用例进入套件
# 创建测试套件
# suite = unittest.TestSuite()
# 向测试套件里面添加用例
# suite.addTest(TestLogin('test_login1'))
# 创建运行方法，verbosity = 2  表示打印用例运行的详细信息
# runner = unittest.TextTestRunner(verbosity=2)
# 运行套件里面的用例
# runner.run(suite)

# 添加多条用例进入套件，缺陷，当有几百条用例时，添加过于麻烦
# 创建套件
# suite = unittest.TestSuite()
# # 创建用例列表
# case_list = [TestLogin("test_login1"), TestLogin('test_login2')]
# # 将用例添加到套件中
# suite.addTests(case_list)
# # 创建TextTestRunner中的运行方法
# runner = unittest.TextTestRunner(verbosity=2)
# # 执行套件里面的用例
# runner.run(suite)
