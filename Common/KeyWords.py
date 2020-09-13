# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 12:53
# @Site    : keywordsmethod
# @File    : KeyWords.py
# @Software: PyCharm
# @contact: 125197291@qq.com

import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from Utils.get_by_locator import GetByLocator
from Utils.DateTimeFormat import DateTimeFormat

# 获取当前系统时间
dt_format = DateTimeFormat()
curTime = dt_format.get_current_time()


class KeyWordsMethod(object):
    """先封装selenium关键字方法，类似pom中的basepage"""

    def open_browser(self, *args):
        """打开浏览器"""
        browser = args[0]
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == 'ff':
            self.driver = webdriver.Firefox()

    def get_url(self, *args):
        """打开 url"""
        url = args[0]
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def wait_eleVisisble(self, locator, wait_time=30):
        """
        显示等待元素可见
        :param locator:
        :param wait_time:
        :return:
        """
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator))

    @property
    def save_screenshots_png(self):
        """
        截图保存
        :return:
        """
        filename = screen_dir + "/images_{}.png".format(curTime)
        return self.driver.save_screenshot(filename)

    def get_element(self, *args):
        """
        通用页面元素定位方式
        :param args:
        :return:
        """
        key = args[0]
        locator = key.split("=")
        browser_driver = GetByLocator(self.driver)
        try:
            self.wait_eleVisisble(tuple(locator))
            ele = browser_driver.get_ele_locator(key)
        except:
            raise NoSuchElementException
        else:
            return ele

    def get_elements(self, *args):
        """
        通用页面元素定位方式
        :param args:
        :return:
        """
        key = args[0]
        locator = key.split("=")
        browser_driver = GetByLocator(self.driver)
        try:
            eles = browser_driver.get_eles_locator(key)
        except:
            raise NoSuchElementException
        else:
            return eles

    def switch_frame(self, *args):
        """
        切换frame窗口
        :param args:
        :return:
        """
        key = args[0]
        self.driver.switch_to.frame(self.get_element(key))

    def element_send_keys(self, *args):
        """
        定位元素对象进行输入内容
        :param args:
        :return:
        """
        key, value = args[0], args[1]
        self.get_element(key).send_keys(value)

    def click_element(self, *args):
        """点击元素"""
        key = args[0]
        self.get_element(key).click()

    def assert_word(self, *args):
        """
        断言：内容是否存在页面源码中
        :param args:
        :return:
        """
        try:
            assert word in self.driver.page_source
        except:
            self.save_screenshots_png()
            raise AssertionError("断言失败!")

    @staticmethod
    def sleep_time():
        """强制等待"""
        time.sleep(3)

    def quit_browser(self):
        """退出浏览器，关闭session"""
        self.driver.quit()
