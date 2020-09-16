# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Site    : keywordsmethod
# @File    : KeyWords.py
# @Software: PyCharm
# @contact: 125197291@qq.com

import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common.conf_dirs import screen_dir
from Utils.DateTimeFormat import DateTimeFormat
from Utils.HandleLogging import logger
from Utils.find_element_by_locator import FindElementByLocator


# 获取当前系统时间
dt_format = DateTimeFormat()
curTime = dt_format.hour_minute_seconds


class KeyWordsMethod(object):
    """
            先封装selenium关键字方法，类似pom中的basepage
    """

    @logger("打开浏览器")
    def open_browser(self, *args):
        """打开浏览器"""
        browser = args[0]
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == 'ff':
            self.driver = webdriver.Firefox()
        self.browser_driver = FindElementByLocator(self.driver)

    @logger("打开网址")
    def get_url(self, *args):
        """打开 url"""
        url = args[0]
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

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

    @logger("截图")
    def save_screenshots_png(self):
        """
                        截图保存
        :return:
        """
        if not os.path.exists(screen_dir):
            os.mkdir(screen_dir)
        filename = screen_dir + "/images_{}.png".format(curTime)
        self.driver.save_screenshot(filename)

    @logger("元素定位")
    def get_element(self, *args):
        """
                        通用页面元素定位方式
        :param args:
        :return:
        """
        key = args[0]
        ele = self.browser_driver.fnd_ele_by_locator(key)
        return ele

    @logger("多个元素定位")
    def get_elements(self, *args):
        """
                        通用页面元素定位方式
        :param args:
        :return:
        """
        key = args[0]
#         browser_driver = FindElementByLocator(self.driver)
        try:
            eles = self.browser_driver.get_eles_locator(key)
        except:
            raise NoSuchElementException
        else:
            return eles

    @logger("切换frame操作窗口")
    def switch_frame(self, *args):
        """
                        切换frame窗口
        :param args:
        :return:
        """
        key = args[0]
        self.driver.switch_to.frame(self.get_element(key))

    @logger("输入文本内容")
    def element_send_keys(self, *args):
        """
                        定位元素对象进行输入内容
        :param args:
        :return:
        """
        key, value = args[0], args[1]
        try:
            self.get_element(key).send_keys(value)
        except:
            raise ValueError("值有误!")

    @logger("点击元素")
    def click_element(self, *args):
        """点击元素"""
        key = args[0]
        self.get_element(key).click()

    @logger("断言")
    def assert_text(self, *args):
        """
                    断言：内容是否存在页面源码中
        :param args:
        :return:
        """
        text = args[1]
        if text:
            try:
                assert text in self.driver.page_source
            except:
                self.save_screenshots_png()
                raise AssertionError("断言失败!")
        else:
            raise ValueError("未输入断言文本内容")

    @staticmethod
    def sleep_time():
        """强制等待"""
        time.sleep(2)

    @logger("关闭浏览器")
    def quit_browser(self):
        """退出浏览器，关闭session"""
        self.driver.quit()
