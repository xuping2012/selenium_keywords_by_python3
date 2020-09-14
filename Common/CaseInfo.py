'''
# -*- encoding=utf-8 -*-
Created on 2020年9月14日下午12:43:57
@author: Joe
@file:Common.CaseInfo.py
'''

__author__ = "Joe"


class CaseInfo(object):
    '''
             获取所有测试用例sheet页,一个sheet页一条用例,操作步骤略
    '''

    def __init__(self, sheet_name):
        '''
        Constructor
        '''
        self.sheet_name = sheet_name
