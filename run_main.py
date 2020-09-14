# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Software: PyCharm
# @contact: 125197291@qq.com

"""
结合unittest测试框架执行testcases目录中所有符合测试用例规则的测试用例
"""

import os
import unittest

from Common.conf_dirs import case_path, report_path
from Libs.HTMLTestRunnerNew import HTMLTestRunner
from Utils.DateTimeFormat import DateTimeFormat

# 获取当前时间
dt_format = DateTimeFormat()
current_time = dt_format.hour_minute_seconds

# 测试报告目录
if not os.path.exists(report_path):
    os.mkdir(report_path)


def run_main():
    # unittest单元测试框架四步走
    # 1.创建测试套件
    suite = unittest.TestSuite()
    # 2.发现测试用例规则并加载到测试套件
    discover = unittest.defaultTestLoader.discover(
        case_path, pattern="test*.py")
    suite.addTest(discover)

    # 利用with上下文管理器
    with open(report_path + "/html_report_{}.html".format(current_time), "wb+") as bf:
        # 3.创建测试用例启动器
        runner = HTMLTestRunner(
            stream=bf, verbosity=2, title="我是测试报告标题", description="描述一下测试报告", tester="是我完成的")
        # 4.运行测试套件
        runner.run(suite)

if __name__ == '__main__':
    run_main()
