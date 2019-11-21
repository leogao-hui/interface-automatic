# author:LEO GAO
# project Encoding:UTF-8


import requests
from Common.apiUrl.System.systemConfigurationUrl import SystemConfigurationUrl
from Common.config import header


# 获取验证码
def receive_verification_code(data):
    '''

    :param data: 获取验证码数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=SystemConfigurationUrl.receive_verification_code_url, data=data)
    return response


# 登录
def login(data):
    '''

    :param data: 登录数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=SystemConfigurationUrl.login_url, data=data)
    return response


# 退出
def exit_login(data):
    '''

    :param data: 退出登录数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=SystemConfigurationUrl.exit_url, data=data)
    return response


# 业务重启
def business_restart(data):
    '''

    :param data: 业务重启数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=SystemConfigurationUrl.business_restart_url, data=data)
    return response
