'''
# -*- encoding=utf-8 -*-
Created on 2020年9月14日下午3:59:51
@author: Joe
@file:AutoAutoTest1
'''

import time

from Common.conf_dirs import test_xlsx
from Common.ref_invoke import run_keywords_method
from Utils.HandleExcel import HandleExcel
from Utils.HandleLogging import logger

__author__ = "Joe"


class TestCaseStepInfo():
    """
            创建一个空类，
            使用内置属性方法setattr来设置该类的属性及值：setattr(obj,key,value)
            思考一个问题：创建使用完之后，是否需要delattr呢？
    """
    pass


class TestCase():
    """第三版selenium关键字驱动,测试用例设计与执行"""

    def __init__(self):
        self.handle_excel = HandleExcel(
            file_path=test_xlsx + "/YD测试用例.xls")

    @logger("获取执行用例的sheetname")
    def get_all_testcases_sheetname(self):
        """获取所有测试用例"""
        self.handle_excel.set_sheet_index_or_name("测试用例")
        case_lines = self.handle_excel.get_max_rows
        case_sheets = []
        for i in range(1, case_lines):
            # 创建一个对象来设置其属性，并讲需要数据赋给属性
            testcase_info = TestCaseStepInfo()
            case_name = self.handle_excel.get_cell(i, 3)
            is_true = self.handle_excel.get_cell(i, 4)
            if bool(case_name) and eval(is_true):
                # 原本在Common包下创建一个CaseInfo类来接收需要执行的测试用例的sheet_name
                # case = CaseInfo(case_name)
                # case_sheets.append(case)
                setattr(testcase_info, "sheet_name", case_name)
                case_sheets.append(testcase_info)
        return case_sheets

    @logger("获取执行用例的step_info")
    def add_testcase_step_by_sheetname(self, case_sheet):
        '''加载整个sheet的操作步骤'''
        caseStepList = []
        self.handle_excel.set_sheet_index_or_name(case_sheet)
        case_steps = self.handle_excel.get_max_rows
        for k in range(1, case_steps):
            # 创建一个对象来设置其属性，并讲需要数据赋给属性
            casestep_info = TestCaseStepInfo()
            step_name = self.handle_excel.get_cell(k, 1)
            key_words = self.handle_excel.get_cell(k, 2)
            locator = self.handle_excel.get_cell(k, 3)
            content = self.handle_excel.get_cell(k, 4)
            if key_words == "" or step_name == "":
                break
            setattr(casestep_info, "step_name", step_name)
            setattr(casestep_info, "key_words", key_words)
            setattr(casestep_info, "locator", locator)
            setattr(casestep_info, "content", content)
            # 原本在Common包下创建一个TestCaseStepInfo类来接收需要执行的测试用例sheet_name的所有测试步骤
            # step_info = TestCaseStepInfo(step_name, key_words, locator, content)
            # caseStepList.append(step_info)
            caseStepList.append(casestep_info)
        return caseStepList

    @logger("按步骤执行用例")
    def excute_testcases(self, caseStepList):
        '''执行测试用例步骤'''
        for i in range(len(caseStepList)):
            start = time.time()
            try:
                res = run_keywords_method(key_words=caseStepList[i].key_words, locator=caseStepList[
                                          i].locator, content=caseStepList[i].content)
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

    @logger("执行用例入口")
    def run_testcase(self):
        '''执行测试用例'''
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
