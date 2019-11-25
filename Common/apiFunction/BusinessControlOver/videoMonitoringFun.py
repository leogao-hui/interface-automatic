#_author:leo gao
#encoding:utf-8



import requests
from Common.apiUrl.BusinessControlOver.videoMonitoringUrl import VideoMonitoringUrl
from Common.config import header


def call_device(data):
    '''
    呼叫设备
    :param data: 呼叫设备数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoMonitoringUrl.call_device_url, data=data)
    return response