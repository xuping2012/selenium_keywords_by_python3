'''
# -*- encoding=utf-8 -*-
Created on 2020年9月14日下午3:59:51
@author: Joe
@file:AutoAutoTest1
'''

import time
import tkinter.filedialog

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


class Application(tkinter.Frame):
    """第④版selenium关键字驱动,测试用例设计与执行"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
#         self.pack()
        self.path = tkinter.StringVar()
        self.create_application()

    def create_application(self):
        #         self.master.geometry("600*300")
        #         输入框，标记，按键
        tkinter.Button(self.master, text="选择用例", command=self._selectPath).grid(
            row=0, column=1)
        # 输入框绑定变量path
        tkinter.Entry(self.master, textvariable=self.path).grid(
            row=0, column=2)
        tkinter.Button(self.master, text="开始测试", command=self.run_testcase, fg="green").grid(
            row=0, column=3)

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
                # cases = CaseInfo(case_name)
                # case_sheets.append(cases)
                setattr(testcase_info, "sheet_name", case_name)
                case_sheets.append(testcase_info)
        return case_sheets

    @logger("获取执行用例的step_info")
    def add_testcase_step_by_sheetname(self, case_sheet):
        """加载整个sheet的操作步骤"""
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
            caseStepList.append(casestep_info)
            # 原本在Common包下创建一个TestCaseStepInfo类来接收需要执行的测试用例sheet_name的所有测试步骤
            # step_info = CaseStepList(step_name, key_words, locator, content)
            # caseStepList.append(step_info)
        return caseStepList

    @logger("按步骤执行用例")
    def excute_testcases(self, caseStepList):
        """执行测试用例步骤"""
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
        """执行测试用例"""
        self.handle_excel = HandleExcel(file_path=self.path.get())
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

    # 打开文件并显示路径
    def _selectPath(self):
        # 选择文件path_接收文件地址
        self.path_ = tkinter.filedialog.askopenfilename()
        # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取
        # 注意：\\转义后为\，所以\\\\转义后为\\
        self.path_ = self.path_.replace("/", "\\")
        # path设置path_的值
        self.path.set(self.path_)

if __name__ == '__main__':

    root = tkinter.Tk()
    root.title('selenium关键字驱动')
    app = Application(master=root)
    app.mainloop()
