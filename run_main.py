# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Software: PyCharm
# @contact: 125197291@qq.com


import unittest

from Common.conf_dirs import case_path,report_path
from Libs.HTMLTestRunnerNew import HTMLTestRunner
from Utils.DateTimeFormat import DateTimeFormat

suite = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
suite.addTest(discover)

dt_format=DateTimeFormat()
current_time=dt_format.hour_minute_seconds

with open(report_path+"/html_report_{}.html".format(current_time), "wb+") as bf:
#     第三步创建测试用例启动器
    runner = HTMLTestRunner(stream=bf, verbosity=2, title="我是测试报告标题", description="描述一下测试报告", tester="是我完成的")
    # 第四步运行测试套件
    runner.run(suite)
    # 关闭报告文件 使用with上下文管理器则不需要此操作
    # f.close()