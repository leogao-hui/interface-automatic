# author:LEO GAO
# project Encoding:UTF-8


import requests
from Common.apiUrl.backgroundManagement.organizationalManagementUrl import OrganizationalManagementUrl
from Common.config import header


def organizational_information_add(data):
    '''
    组织架构信息新增
    :param data: 组织架构信息数据
    :return: response
    '''
    request = requests.session()
    response = request.post(url=OrganizationalManagementUrl.organizational_information_add_url, data=data)
    return response


def organizational_information_delete(data):
    '''
    组织架构信息删除
    :param data: 组织架构信息数据
    :return: response
    '''
    request = requests.session()
    response = request.post(url=OrganizationalManagementUrl.organizational_information_delete_url, data=data)
    return response


def organizational_information_drag_drop_change(data):
    '''
    组织架构信息-拖拽变更
    :param data: 组织架构信息-拖拽变更数据
    :return: response
    '''
    request = requests.session()
    response = request.post(url=OrganizationalManagementUrl.organizational_information_drag_drop_change_url, data=data)
    return response


def receive_organizational_tree(data):
    '''
    获取组织树
    :param data: 获取组织树数据
    :return: response
    '''
    request = requests.session()
    response = request.post(url=OrganizationalManagementUrl.receive_organizational_tree_url, data=data)
    return response


def organizational_information_update(data):
    '''
    组织架构信息-修改
    :param data: 组织架构信息-修改数据
    :return: response
    '''
    request = requests.session()
    response = request.post(url=OrganizationalManagementUrl.organizational_information_update_url, data=data)
    return response


