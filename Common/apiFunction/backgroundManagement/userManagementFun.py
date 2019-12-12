# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.backgroundManagement.userManagementUrl import UserManagementUrl
from Common.config import header


def add_user_information(header_name, data):
    '''
    用户信息-新增
    :param data: 用户新增数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header_name, url=UserManagementUrl.user_add_url, data=data)
    return response


def user_bind_device(header_name, data):
    '''
    用户绑定设备
    :param data: 用户绑定设备数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header_name, url=UserManagementUrl.user_bind_device_url, data=data)
    return response


def delete_user(data):
    '''
    用户删除
    :param data: 用户删除数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.user_delete_url, data=data)
    return response


def receive_decoder(data):
    '''
    获取解码器
    :param data: 获取解码器数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.receive_decoder_url, data=data)
    return response


def receive_compile_and_start_time(data):
    '''
    获取编译和启动时间
    :param data: 获取编译和启动时间数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.receive_compile_and_start_time_url, data=data)
    return response


def user_receive_list(data):
    '''
    用户获取列表
    :param data: 用户获取列表数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.user_receive_list_url, data=data)
    return response


def receive_system_time(data):
    '''
    获取系统时间
    :param data: 获取系统时间数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.receive_system_time_url, data=data)
    return response


def user_is_online(data):
    '''
    根据用户id判断用户是否在线
    :param data: 根据用户id判断用户是否在线
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.user_isOnline_url, data=data)
    return response


def reset_user_password(data):
    '''
    重置用户密码
    :param data: 重置用户密码数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.reset_user_password_url, data=data)
    return response


def update_user(data):
    '''
    用户信息修改
    :param data: 用户信息修改数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.user_update_url, data=data)
    return response


def update_user_initialize_password(data):
    '''
    修改用户初始化密码
    :param data: 修改用户初始化密码数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.update_user_initialize_password_url, data=data)
    return response


def update_user_password(data):
    '''
    修改用户密码
    :param data: 修改用户密码数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=UserManagementUrl.update_user_password_url, data=data)
    return response


def according_user_update_user(data):
    '''
    根据用户名修改用户信息
    :param data: 根据用户名修改用户信息数据
    :return: response
    '''