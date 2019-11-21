# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.backgroundManagement.deviceManagementUrl import DeviceManagementUrl
from Common.config import header


# 设备信息-新增
def add_device_information(data):
    request = requests.sessions
    response = request.session().post(headers=header, url=DeviceManagementUrl.add_device_url, data=data)
    return response

# 设备信息-删除
def



