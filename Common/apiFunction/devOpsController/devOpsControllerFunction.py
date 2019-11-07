#_author:LEO GAO
#_project Encoding: UTF-8


import requests
from Common.apiUrl.devOpsController.devOpsControllerUrl import get_sms_url
from Common.config import header


class DevOpsControllerFunction:

    def get_sms(self, data):
        request = requests.session()
        response = request.post(headers=header, url=get_sms_url, data=data)
        return response