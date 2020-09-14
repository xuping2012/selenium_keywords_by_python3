#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 1:56
# @Author  : Paulson
# @File    : get_by_local.py
# @Software: PyCharm
# @define  : function

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utils.HandleLogging import logger


class GetByLocator(object):
    """封装了selenium一些非关键字应用的方法，通过从excel测试用例中获取数据并返回元素到关键字中应用"""

    def __init__(self, driver):
        self.driver = driver

    @logger("等待元素可见")
    def wait_eleVisisble(self, locator, wait_time=30):
        """
                        显示等待元素可见
        :param locator:
        :param wait_time:
        :return:
        """
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator))

    @logger("查找元素")
    def get_ele_locator(self, locator):
        """
        locator：By=value
        :return:ele
        """
        by, value = locator.split('=')
        if by not in By.__dict__.values():
            raise TypeError("不存在此查找元素方法")
        try:
            self.wait_eleVisisble((by, value))
            ele = self.driver.find_element(by, value)
        except:
            raise NoSuchElementException
        else:
            return ele

    def get_eles_locator(self, locator):
        """
        locator：By=value
        :return:ele
        """
        by, value = locator.split('=')
        if by not in By.__dict__.values():
            raise TypeError("不存在此查找元素方法")
        eles = self.driver.find_elements(by, value)
        return eles
