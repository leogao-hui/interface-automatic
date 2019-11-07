# author:LEO GAO
# project Encoding:UTF-8

import logging
import os
import time

dir = os.path.dirname((os.path.abspath(__file__)))

def log():
    # 声场logger对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 日志以屏幕形式输出
    console = logging.StreamHandler()

    #text = logging.FileHandler("%s/%s.log" % (dir, time.strftime('%Y-%m-%d %H:%M:%S')))#日志以文件格式输出

    # 把handle对象绑定到logger
    logger.addHandler(console)
    #logger.addHandler(text)

    # 生成formatter对象
    console_formatter = logging.Formatter('%(name)s - %(asctime)s - %(module)s - %(levelname)s - %(message)s')
    file_formatter = logging.Formatter('%(name)s - %(asctime)s - %(module)s - %(levelname)s - %(message)s')

    console.setFormatter(console_formatter)
    #text.setFormatter(file_formatter)

    return logger