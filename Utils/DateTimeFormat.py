# Author 十年如歌
# coding=utf-8
# @Software: PyCharm
# @contact: 125197291@qq.com


import time
from datetime import timedelta, date
import locale


class DateTimeFormat(object):
    """处理时间格式"""

    @staticmethod
    def date_time_chinese():
        """
        return: the current time str-format for YYYY年mm月dd日 HH时MM分SS秒
        """
        locale.setlocale(locale.LC_CTYPE, "chinese")
        return time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime())

    def get_current_time(self, is_cn=False):
        """return current time for is_cn"""
        if not is_cn:
            return self.current_time
        else:
            return self.date_time_chinese()

    @staticmethod
    def date_chinese_ymd(self):
        u"returns the current time string,format for YYYY年mm月dd日"
        locale.setlocale(locale.LC_CTYPE, "chinese")
        return time.strftime(r"%Y年%m月%d日", time.localtime())

    @property
    def current_time(self):
        "returns the current time string,format for YYYY-mm-dd HH:MM:SS"
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    @property
    def year_month_day(self):
        "returns the current time string,format for YYYY-mm-dd"
        return time.strftime("%Y-%m-%d", time.localtime())

    @property
    def hour_minute_seconds(self):
        """
        :return: the current time string,format for HH:MM:SS
        """
        return time.strftime("%H-%M-%S", time.localtime())

    @property
    def year(self):
        """
        :return:the current time string,format for Year
        """
        return time.strftime("%Y", time.localtime())

    @property
    def month(self):
        """
        :return:the current time string,format for month
        """
        return time.strftime("%m", time.localtime())

    @property
    def day(self):
        """
        :return:the current time string,format for day
        """
        return time.strftime("%d", time.localtime())

    @property
    def hour(self):
        """
        :return:the current time string,format for Hour
        """
        return time.strftime("%H", time.localtime())

    @property
    def minute(self):
        """
        :return:returns the current time string,format for minute
        """
        return time.strftime("%M", time.localtime())

    @property
    def seconds(self):
        """
        :return:the current time string,format for seconds
        """
        return time.strftime("%S", time.localtime())

    def str_to_tuple(self, stime, dateformat):
        """
        :stime:"%Y-%m-%d %H:%M:%S"
        :dateformat:"%Y-%m-%d %H:%M:%S"
        :return:the string variable into time tuples
        """
        return time.strptime(stime, dateformat)

    def add_date(self, day_num):
        """
        :param day_num:
        :return:in the current date increase days(a time interval)
        """
        today = date.today()
        times = today + timedelta(days=day_num)
        return times

    def sub_date(self, day_num):
        """
        :param day_num:
        :return:in the current date decrease days(one time interval)
        """
        today = date.today()
        times = today - timedelta(days=day_num)
        return times


if __name__ == "__main__":
    test = DateTimeFormat()
    t = test.get_current_time(True)
    print(test.str_to_tuple("2020-09-12 12:12:21"))
