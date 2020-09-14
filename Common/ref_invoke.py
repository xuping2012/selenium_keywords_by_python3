'''
Created on 2020年9月14日

@author: qguan
'''
from Utils.HandleLogging import logger
from Common.KeyWords import KeyWordsMethod


# 创建实例对象
keyWords_method = KeyWordsMethod()


@logger("ref_invoke")
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
            return "failed"
        else:
            return "pass"
    else:
        #         print("该关键字:{}操作不存在!!!".format(key_words))
        raise AttributeError("该关键字:{}操作不存在!".format(key_words))
