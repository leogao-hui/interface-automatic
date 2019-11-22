# author:LEO GAO
# project Encoding:UTF-8


import requests
from Common.apiUrl.System.systemConfigurationUrl import SystemConfigurationUrl
from Common.config import header


def receive_verification_code(data):
    '''
    获取验证码
    :param data: 获取验证码数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=SystemConfigurationUrl.receive_verification_code_url, data=data)
    return response


def login(data):
    '''
    登录
    :param data: 登录数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=SystemConfigurationUrl.login_url, data=data)
    return response


def exit_login(data):
    '''
    退出
    :param data: 退出登录数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=SystemConfigurationUrl.exit_url, data=data)
    return response


def business_restart(data):
    '''
    业务重启
    :param data: 业务重启数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=SystemConfigurationUrl.business_restart_url, data=data)
    return response


