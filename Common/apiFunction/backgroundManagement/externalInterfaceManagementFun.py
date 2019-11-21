# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.backgroundManagement.externalInterfaceManagementUrl import ExternalInterfaceManagementUrl
from Common.config import header


# 接口信息-新增
def add_interface_information(data):
    request = requests.session()
    response = request.post(headers=header, url=ExternalInterfaceManagementUrl.interface_information_add_url, data=data)
    return response


# 接口信息-列表
def receive_interface_information_list(data):
    request = requests.session()
    response = request.post(headers=header, url=ExternalInterfaceManagementUrl.interface_information_list_url, data=data)
    return response


# 获取新媒体地址
def receive_new_media_address(data):
    request = requests.session()
    response = request.post(headers=header, url=ExternalInterfaceManagementUrl.receive_new_media_address_url, data=data)
    return response


# 接口信息-修改
def update_interface_information(data):
    request = requests.session()
    response = request.post(headers=header, url=ExternalInterfaceManagementUrl.interface_information_update_url, data=data)
    return response

