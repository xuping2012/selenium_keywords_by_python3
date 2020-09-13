# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 19:42
# @Site    : 
# @File    : HandleLogging.py
# @Software: PyCharm
# @contact: 125197291@qq.com


import os
from functools import wraps
import logbook
from logbook.more import ColorizedStderrHandler

__author__ = "Joe"

check_path = '..'

LOG_DIR = os.path.join(check_path, 'Logs')

file_stream = False

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True

def get_logger(name='selenium关键字驱动执行测试用例日志输出', file_log=file_stream, level="DEBUG"):
    """
    :param name:
    :param file_log:
    :param level:
    :return:get logger Factory function
    """
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(LOG_DIR, '%s.log' % name),
        date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)

LOG = get_logger(file_log=file_stream, level='INFO')


def logger(param):
    """
    fcuntion from logger meta
    :param param:
    :return:
    """
    def wrap(function):
        """
        logger wrapper
        :param function:
        :return:
        """
        @wraps(function)
        def _wrap(*args, **kwargs):
            """
            wrap tool
            :param args:
            :param kwargs:
            :return:
            """
            LOG.info("当前执行方法名:{}".format(param))
            if args:
                LOG.info("开始执行：{}".format(args[1:]))
            if kwargs:
                LOG.info("全部kwargs参数信息 , {}".format(str(kwargs)))
            return function(*args, **kwargs)
        return _wrap
    return wrap