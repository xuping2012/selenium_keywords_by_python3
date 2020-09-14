'''
# -*- encoding=utf-8 -*-
Created on 2020年9月14日上午11:56:24
@author: Joe
@file:Common.CaseStepList.py
'''

__author__ = "Joe"


class CaseStepList(object):
    '''
            根据测试用例读取的sheet页,所有执行步骤
    '''

    def __init__(self, step_title, step_keyword, step_locator, step_value, status=None, result=None, excute_time=None):
        '''
        Constructor
        '''
        self.step_title = step_title
        self.step_keyword = step_keyword
        self.step_locator = step_locator
        self.step_value = step_value
        self.status = status
        self.result = result
        self.excute_time = excute_time
