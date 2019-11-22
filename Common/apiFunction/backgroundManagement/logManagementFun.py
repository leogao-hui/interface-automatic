# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.backgroundManagement.logManagementUrl import LogManagementUrl
from Common.config import header


def receive_log(data):
    '''
    获取日志
    :param data: 获取日志数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=LogManagementUrl.receive_log_url, data=data)
    return response
