#_author:leo gao
#encoding:utf-8


import requests
from Common.apiUrl.BusinessControlOver.callTogetherUrl import CallTogetherUrl
from Common.config import header


def receive_organizational_tree(data):

    '''
    获取组织树
    :param data: 获取组织树数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=CallTogetherUrl.receive_organizational_tree_url, data=data)
    return response



