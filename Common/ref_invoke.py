'''
Created on 2020年9月14日

@author: qguan
'''
from Utils.HandleLogging import logger
from Common.KeyWords import KeyWordsMethod


# 创建实例对象
keyWords_method = KeyWordsMethod()

FAILED = "failed"
PASS = "pass"


@logger("反射字符串调用类方法")
def run_keywords_method(key_words, locator="", content="None"):
    """
           利用python反射机制
    keywords关键字实现类属性调用函数
    """
    if hasattr(keyWords_method, key_words):
        keyWords_function = getattr(keyWords_method, key_words)
        try:
            if content is "":
                if locator is "":
                    keyWords_function()
                else:
                    keyWords_function(locator)
            else:
                keyWords_function(locator, content)
        except:
            keyWords_function = getattr(keyWords_method, "quit_browser")
            keyWords_function()
            return FAILED
        else:
            return PASS
    else:
        raise AttributeError("该关键字:{}操作不存在!".format(key_words))
