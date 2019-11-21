# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.backgroundManagement.userManagementUrl import UserManagementUrl
from Common.config import header


# 用户信息-新增
def add_user_information(data):
    '''

    :param data: 用户新增数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.user_add_url, data=data)
    return response


# 用户绑定设备
def user_bind_device(data):
    '''

    :param data: 用户绑定设备数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.user_bind_device_url, data=data)
    return response


# 用户删除
def delete_user(data):
    '''

    :param data: 用户删除数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.user_delete_url, data=data)
    return response


# 获取解码器
def receive_decoder(data):
    '''

    :param data: 获取解码器数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.receive_decoder_url, data=data)
    return response


# 获取编译和启动时间
def receive_compile_and_start_time(data):
    '''

    :param data: 获取编译和启动时间
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.receive_compile_and_start_time_url, data=data)
    return response


# 用户获取列表
def user_receive_list(data):
    '''

    :param data: 用户获取列表
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.user_receive_list_url, data=data)
    return response