# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Software: PyCharm
# @contact: 125197291@qq.com

from Utils.HandleExcel import HandleExcel
from Utils.HandleLogging import logger
from Common.KeyWords import KeyWordsMethod
from Common.conf_dirs import excel_path


class TestCase(object):
    """执行关键字测试用例程序入口"""

    def __init__(self):
        self.handle_excel = HandleExcel(file_path=excel_path+"/关键字驱动测试用例.xlsx")
        self.keyWords_method = KeyWordsMethod()

    @logger("main")
    def run_main(self):
        """运行主程序读取excel数据"""
        self.handle_excel.set_rsheet_index_or_name()
        case_lines = self.handle_excel.get_max_rows
        for i in range(1, case_lines):
            is_run = self.handle_excel.get_cell(i, 2)
            if eval(is_run):
                case_id = self.handle_excel.get_cell(i, 0)
                key_words = self.handle_excel.get_cell(i, 3)
                locator = self.handle_excel.get_cell(i, 4)
                content = self.handle_excel.get_cell(i, 5)
                if content == '':
                    if locator == '':
                        self.run_keywords_method(key_words)
                    else:
                        self.run_keywords_method(key_words, locator)
                else:
                    self.run_keywords_method(key_words, locator, content)

    @logger("main2")
    def run_main2(self):
        """运行主程序读取excel数据"""
        sheets = self.handle_excel.get_all_sheets
        for j in range(len(sheets)):
            self.handle_excel.set_rsheet_index_or_name(j)
            case_lines = self.handle_excel.get_max_rows
            for i in range(1, case_lines):
                is_run = self.handle_excel.get_cell(i, 2)
                if eval(is_run):
                    case_id = self.handle_excel.get_cell(i, 0)
                    step_ame = self.handle_excel.get_cell(i, 1)
                    key_words = self.handle_excel.get_cell(i, 3)
                    locator = self.handle_excel.get_cell(i, 4)
                    content = self.handle_excel.get_cell(i, 5)
                    if content == '':
                        if locator == '':
                            self.run_keywords_method(key_words)
                        else:
                            self.run_keywords_method(key_words, locator)
                    else:
                        self.run_keywords_method(key_words, locator, content)

    @logger("关键字反射调用函数")
    def run_keywords_method(self, key_words, locator=None, content=None):
        """
        利用python反射机制
        keywords关键字
        """
        if hasattr(self.keyWords_method, key_words):
            keyWords_function = getattr(self.keyWords_method, key_words)
            if content is None:
                if locator is None:
                    keyWords_function()
                else:
                    keyWords_function(locator)
            else:
                keyWords_function(locator, content)
        else:
            print("该关键字:{}操作不存在!!!".format(key_words))


if __name__ == '__main__':
    test = TestCase()
    test.run_main()
