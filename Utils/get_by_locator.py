#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 1:56
# @Author  : Paulson
# @File    : get_by_local.py
# @Software: PyCharm
# @define  : function

from selenium.webdriver.common.by import By


class GetByLocator(object):
    """封装了selenium一些非关键字应用的方法，通过从excel测试用例中获取数据并返回元素到关键字中应用"""

    def __init__(self, driver):
        self.driver = driver

    def get_ele_locator(self, locator):
        """
        locator：By=value
        :return:ele
        """
        by, value = locator.split('=')
        if by not in By.__dict__.values():
            raise TypeError("不存在此查找元素方法")
        ele = self.driver.find_element(by, value)
        return ele

    def get_eles_locator(self, locator):
        """
        locator：By=value
        :return:ele
        """
        by, value = locator.split('=')
        if by not in By.__dict__.values():
            raise TypeError("不存在此查找元素方法")
        ele = self.driver.find_elements(by, value)
        return ele
