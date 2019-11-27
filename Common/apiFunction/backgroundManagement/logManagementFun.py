# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.backgroundManagement.logManagementUrl import LogManagementUrl


def receive_log(header_data, data):
    '''
    获取日志
    :param data: 获取日志数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header_data, url=LogManagementUrl.receive_log_url, data=data)
    return response

