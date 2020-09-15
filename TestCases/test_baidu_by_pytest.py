# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Software: PyCharm
# @contact: 125197291@qq.com


import time

import pytest

from Common.HandleTestCase import HandleTestCase
from Common.conf_dirs import excel_path
from Utils.HandleLogging import logger


class TestCase():
    """执行关键字测试用例程序入口"""

    handle_testcase = HandleTestCase(
        case_name=excel_path + "/关键字驱动测试用例.xlsx")
    testcase_sheets = handle_testcase.get_all_testcases_sheetname()
    i = 1

    @logger("test_cases_by_keywords")
    @pytest.mark.parametrize("testcase_sheet", testcase_sheets)
    def test_cases_by_keywords(self, testcase_sheet):
        """运行主程序读取excel数据"""
        testcase_stepinfo = self.handle_testcase.add_testcase_step_by_sheetname(
            testcase_sheet.sheet_name)
        start = time.time()
        result = self.handle_testcase.excute_testcases(testcase_stepinfo)
        end = time.time()
        self.handle_testcase.handle_excel.set_sheet_index_or_name("测试用例")
        execute_time = "%.2fs" % (end - start)
        if result == "pass":
            self.handle_testcase.handle_excel.write_cell_result(
                self.i + 1, 5, result)
        else:
            self.handle_testcase.handle_excel.write_cell_result(
                self.i + 1, 5, result, "red")
        self.handle_testcase.handle_excel.write_cell_result(
            self.i + 1, 6, execute_time, "white")
if __name__ == '__main__':
    pytest.main()