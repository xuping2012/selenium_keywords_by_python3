# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/11 13:13
# @Site    :
# @File    : conf_dirs.py
# @Software: PyCharm
# @contact: 125197291@qq.com


import os

basepath = os.path.abspath(os.path.dirname(__file__))

case_path = basepath.replace("Common", "TestCases")

report_path = basepath.replace("Common", "HTMLReports")

excel_path = basepath.replace("Common", "TestDatas")

screen_dir = basepath.replace("Common", "Screenshots")

log_dir = basepath.replace("Common", "Logs")

if __name__ == '__main__':
    print(screen_dir)
