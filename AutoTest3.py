'''
# -*- encoding=utf-8 -*-
Created on 2020年9月14日下午3:59:51
@author: Joe
@file:AutoTest1.py
'''

import time
import tkinter.filedialog

from Common.CaseInfo import CaseInfo
from Common.CaseStepList import CaseStepList
from Common.ref_invoke import run_keywords_method
from Utils.HandleExcel import HandleExcel


__author__ = "Joe"


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
