'''
# -*- encoding=utf-8 -*-
Created on 2020年9月14日下午3:59:51
@author: Joe
@file:AutoTest1.py
'''

import time

from Common.CaseInfo import CaseInfo
from Common.CaseStepList import CaseStepList
from Common.conf_dirs import test_xlsx
from Common.ref_invoke import run_keywords_method
from Utils.HandleExcel import HandleExcel


__author__ = "Joe"


class TestCase():
    """第三版selenium关键字驱动,测试用例设计与执行"""

    def __init__(self):
        self.handle_excel = HandleExcel(
            file_path=test_xlsx + "/关键字驱动测试用例2.xls")

    def get_all_testcases_sheetname(self):
        """获取所有测试用例"""
        self.handle_excel.set_sheet_index_or_name("测试用例")
        case_lines = self.handle_excel.get_max_rows
        case_sheets = []
        for i in range(1, case_lines):
            case_name = self.handle_excel.get_cell(i, 3)
            is_true = self.handle_excel.get_cell(i, 4)
            if bool(case_name) and eval(is_true):
                cases = CaseInfo(case_name)
                case_sheets.append(cases)
        return case_sheets

    def add_testcase_step_by_sheetname(self, case_sheet):
        """加载整个sheet的操作步骤"""
        caseStepList = []
        self.handle_excel.set_sheet_index_or_name(case_sheet)
        case_steps = self.handle_excel.get_max_rows
        for k in range(1, case_steps):
            step_name = self.handle_excel.get_cell(k, 1)
            key_words = self.handle_excel.get_cell(k, 2)
            locator = self.handle_excel.get_cell(k, 3)
            content = self.handle_excel.get_cell(k, 4)
            if key_words == "" or step_name == "":
                break
            step_info = CaseStepList(
                step_name, key_words, locator, content)
            caseStepList.append(step_info)
        return caseStepList

    def excute_testcases(self, caseStepList):
        """执行测试用例步骤"""
        for i in range(len(caseStepList)):
            start = time.time()
            try:
                res = run_keywords_method(key_words=caseStepList[i].step_keyword, locator=caseStepList[
                                          i].step_locator, content=caseStepList[i].step_value)
                execute_time = "{:.2f}s".format(time.time() - start)
                self.handle_excel.write_cell_result(i + 1, 5, res)
            except:
                execute_time = "{:.2f}s".format(time.time() - start)
                self.handle_excel.write_cell_result(i + 1, 5, res, "red")
                return "failed"
            finally:
                self.handle_excel.write_cell_result(
                    i + 1, 6, execute_time, "white")
        return "pass"

    def run_testcase(self):
        """执行测试用例"""
        try:
            case_sheets = self.get_all_testcases_sheetname()
            for i in range(len(case_sheets)):
                caseStepList = self.add_testcase_step_by_sheetname(
                    case_sheets[i].sheet_name)
                start = time.time()
                result = self.excute_testcases(caseStepList)
                end = time.time()
                self.handle_excel.set_sheet_index_or_name("测试用例")
                execute_time = "%.2fs" % (end - start)
                if result == "pass":
                    self.handle_excel.write_cell_result(i + 1, 5, result)
                else:
                    self.handle_excel.write_cell_result(
                        i + 1, 5, result, "red")
                self.handle_excel.write_cell_result(
                    i + 1, 6, execute_time, "white")

        except:
            raise

if __name__ == '__main__':
    excute_case = TestCase()
    excute_case.run_testcase()