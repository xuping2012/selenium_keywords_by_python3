# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Software: PyCharm
# @contact: 125197291@qq.com


import unittest

from Utils.HandleExcel import HandleExcel
from Utils.HandleLogging import logger

from Common.conf_dirs import excel_path
from Common.ref_invoke import run_keywords_method


class TestCase(unittest.TestCase):
    """执行关键字测试用例程序入口"""

    def setUp(self):
        self.handle_excel = HandleExcel(
            file_path=excel_path + "/关键字驱动测试用例.xlsx")

    @logger("main")
    def test_cases_by_keywords(self):
        """运行主程序读取excel数据"""
        self.handle_excel.set_sheet_index_or_name()
        case_lines = self.handle_excel.get_max_rows
        for i in range(1, case_lines):
            is_run = self.handle_excel.get_cell(i, 2)
            if eval(is_run):
                #case_id = self.handle_excel.get_cell(i, 0)
                key_words = self.handle_excel.get_cell(i, 3)
                locator = self.handle_excel.get_cell(i, 4)
                content = self.handle_excel.get_cell(i, 5)
                if content == '':
                    if locator == '':
                        run_keywords_method(key_words)
                    else:
                        run_keywords_method(key_words, locator)
                else:
                    run_keywords_method(key_words, locator, content)

    @logger("main2")
    def run_main2(self):
        """运行主程序读取excel数据"""
        sheets = self.handle_excel.get_all_sheets
        for j in range(len(sheets)):
            self.handle_excel.set_sheet_index_or_name(j)
            case_lines = self.handle_excel.get_max_rows
            for i in range(1, case_lines):
                is_run = self.handle_excel.get_cell(i, 2)
                if eval(is_run):
                    #case_id = self.handle_excel.get_cell(i, 0)
                    #step_ame = self.handle_excel.get_cell(i, 1)
                    key_words = self.handle_excel.get_cell(i, 3)
                    locator = self.handle_excel.get_cell(i, 4)
                    content = self.handle_excel.get_cell(i, 5)
                    if content == '':
                        if locator == '':
                            run_keywords_method(key_words)
                        else:
                            run_keywords_method(key_words, locator)
                    else:
                        run_keywords_method(key_words, locator, content)
