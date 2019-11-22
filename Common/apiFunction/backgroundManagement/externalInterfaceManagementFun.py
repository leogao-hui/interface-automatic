# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.backgroundManagement.externalInterfaceManagementUrl import ExternalInterfaceManagementUrl
from Common.config import header


def add_interface_information(data):
    '''
    接口信息-新增
    :param data: 接口信息-新增数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=ExternalInterfaceManagementUrl.interface_information_add_url, data=data)
    return response


def receive_interface_information_list(data):
    '''
    接口信息-列表
    :param data: 接口信息-列表数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=ExternalInterfaceManagementUrl.interface_information_list_url, data=data)
    return response


def receive_new_media_address(data):
    '''
    获取新媒体地址
    :param data: 获取新媒体地址数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=ExternalInterfaceManagementUrl.receive_new_media_address_url, data=data)
    return response


def update_interface_information(data):
    '''
    接口信息-修改
    :param data: 接口信息-修改数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=ExternalInterfaceManagementUrl.interface_information_update_url, data=data)
    return response

