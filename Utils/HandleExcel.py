# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Software: PyCharm
# @contact: 125197291@qq.com


import xlrd
from xlutils.copy import copy
import xlwt


from Common.conf_dirs import excel_path


class HandleExcel(object):
    """封装excel文件操作方法"""

    def __init__(self, file_path=None):
        """
                     初始化类属性：
        file_path:文件路径
        """
        self.file_path = file_path
        # 获取读工作簿对象
        self.rwb = self.open_workbook()
        self.sh = None
        # 复制读对象为写工作簿对象
        self.wb = copy(self.rwb)
        self.wsh = None
        # 初始化样式
        self.style = xlwt.XFStyle()
        # 设置背景色
        self.pattern = xlwt.Pattern()
        self.pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        # 设置了字体颜色字典
        self.colorDict = {
            "black": 0, "white": 1, "red": 2, "green": 3, "bule": 4, "yellow": 5}

    def set_style(self, color):
        """设置xlwd写入单元格样式,根据执行测试用例结果"""
        color_num = self.colorDict.get(color)
        # 设置背景色
        self.pattern = xlwt.Pattern()
        self.pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        # 根据不同的结果,设置不同的背景色
        self.pattern.pattern_fore_colour = color_num
        self.style.pattern = self.pattern
        return self.style

    def open_workbook(self):
        """打开excel文件,获取工作簿"""
        workbooks = xlrd.open_workbook(self.file_path)
        return workbooks

    @property
    def get_all_sheet_names(self):
        """获取测试用例所有sheet页"""
        sheet_names = self.rwb.sheet_names()
        return sheet_names

    @property
    def get_all_sheets(self):
        """获取测试用例所有sheet总个数"""
        sheet_nums = self.rwb.sheets()
        return sheet_nums

    def set_sheet_index_or_name(self, sheet=0):
        """设置当前要读取的sheet对象"""
        self.wsh = self.wb.get_sheet(sheet)
        if isinstance(sheet, int):
            self.rsh = self.rwb.sheet_by_index(sheet)
        elif isinstance(sheet, str):
            self.rsh = self.rwb.sheet_by_name(sheet)
        else:
            raise Exception("sheet must be integer or string!!!")

    @property
    def get_max_rows(self):
        """获取excel总行数"""
        rows = self.rsh.nrows
        return rows

    @property
    def get_max_cols(self):
        """获取excel总列数"""
        cols = self.rsh.ncols
        return cols

    def get_cell(self, row, cell):
        """获取单元格内容"""
        data = self.rsh.cell(row, cell).value
        return data

    def write_cell_result(self, row_no, col_no, result, color="white"):
        """
        xlwd写入结果文件
        row_no:行号, 从1开始的
        col_no:列号，从1开始的
        content:需要写入excel的内容
        """
        self.wsh.write(row_no, col_no, result, style=self.set_style(color))
        self.save_workbook()

    def save_workbook(self):
        """xlwd保存excel文件"""
        self.wb.save(self.file_path)

    @property
    def get_case_title(self):
        """获取表头"""
        cols = self.get_max_cols
        title = []
        for t in cols:
            title.append(t)
        return title

if __name__ == '__main__':
    handle_excel = HandleExcel(file_path=excel_path + "/关键字驱动测试用例.xls")

    # test write same data in excel
#     for sheet_name in range(len(handle_excel.get_all_sheets)):
#         handle_excel.set_sheet_index_or_name(sheet_name)
#         case_lines = handle_excel.get_max_rows
#         for i in range(1, case_lines):
#             handle_excel.write_cell_result(i, 7, "pass")

    # test get all sheet's data
    # or use get_all_sheet_names this property
#     for sheet_index in range(len(handle_excel.get_all_sheets)):
#         handle_excel.set_sheet_index_or_name(sheet_index)
#         case_lines = handle_excel.get_max_rows
#         for i in range(1, case_lines):
#             case_id = handle_excel.get_cell(i, 0)
#             print(case_id)
