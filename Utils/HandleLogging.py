# Author 十年如歌
# coding=utf-8
# @Time    : 2020/9/12 19:59
# @Site    :
# @File    : HandleLogging.py
# @Software: PyCharm
# @contact: 125197291@qq.com


import os
from Common.conf_dirs import log_dir
from functools import wraps
import logbook
from logbook.more import ColorizedStderrHandler

__author__ = "Joe"


if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    file_stream = True
else:
    file_stream = False


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
        os.path.join(log_dir, '%s.log' % name),
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
