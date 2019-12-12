# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.backgroundManagement.deviceManagementUrl import DeviceManagementUrl
from Common.config import header


def add_device_information(header_name, data):
    '''
    设备信息-新增
    :param data: 设备信息-新增数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header_name, url=DeviceManagementUrl.add_device_url, data=data)
    return response


def delete_device_information(data):
    '''
    设备信息-删除
    :param data: 设备信息-删除数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=DeviceManagementUrl.delete_device_url, data=data)
    return response


def query_device_information(data):
    '''
    设备信息查询
    :param data: 设备信息查询数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=DeviceManagementUrl.device_information_query_url, data=data)
    return response


def receive_device_not_tied_to_user_list(data):
    '''
    设备未绑定用户列表获取
    :param data: 设备未绑定用户列表获取数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=DeviceManagementUrl.device_not_tied_to_user_list_url, data=data)
    return response


def receive_device_list(data):
    '''
    设备列表获取
    :param data: 设备列表获取数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=DeviceManagementUrl.device_receive__list_url, data=data)
    return response


def update_device_information(data):
    '''
    设备信息-修改
    :param data: 设备信息-修改数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=DeviceManagementUrl.device_update_url, data=data)
    return response


def synchronize_unified_device_information(data):
    '''
    设备信息-同步统一设备信息
    :param data: 设备信息-同步统一设备信息数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=DeviceManagementUrl.synchronize_unified_device_information_url, data=data)
    return response
