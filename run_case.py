from HTMLTestRunner import HTMLTestRunner
import unittest
from loguru import logger

# 创建测试套件
suite = unittest.TestLoader().discover('.', pattern='test_*.py')

# 生成文件
filename = 'case_report.html'
with open(filename, 'wb') as f:
    # 需要传三个参数，第一个：文件名， 第二个生成报告的title， 第三个信息描述
    runner = HTMLTestRunner(f, title='登录测试报告', description='V1.0')
    # 运行测试套件
    runner.run(suite)

