# author:LEO GAO
# project Encoding:UTF-8

from Common.config import ci_url


class LogManagementUrl:

    # 获取日志信息列表
    receive_log_url = '%s/log/getpage' % ci_url

