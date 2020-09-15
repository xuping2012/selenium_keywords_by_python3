# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Software: PyCharm
# @contact: 125197291@qq.com

import time

from Common.conf_dirs import test_xlsx
from Common.ref_invoke import run_keywords_method
from Utils.HandleExcel import HandleExcel
from Utils.HandleLogging import logger


class TestCase(object):
    """执行关键字测试用例程序入口"""

    def __init__(self):
        self.handle_excel = HandleExcel(
            file_path=test_xlsx + "/关键字驱动测试用例0.xlsx")

    @logger("main")
    def run_main(self):
        """运行主程序读取excel数据"""
        self.handle_excel.set_sheet_index_or_name()
        case_lines = self.handle_excel.get_max_rows
        for i in range(1, case_lines):
            is_run = self.handle_excel.get_cell(i, 2)
            if eval(is_run):
                key_words = self.handle_excel.get_cell(i, 3)
                locator = self.handle_excel.get_cell(i, 4)
                content = self.handle_excel.get_cell(i, 5)
                start = time.time()
                try:
                    res = run_keywords_method(
                        key_words=key_words, locator=locator, content=content)
                    execute_time = "{:.2f}s".format(time.time() - start)
                    self.handle_excel.write_cell_result(i, 6, res)
                except:
                    execute_time = "{:.2f}s".format(time.time() - start)
                    self.handle_excel.write_cell_result(i, 6, res, "red")
                finally:
                    self.handle_excel.write_cell_result(
                        i, 7, execute_time, "white")

if __name__ == '__main__':
    test = TestCase()
    test.run_main()
