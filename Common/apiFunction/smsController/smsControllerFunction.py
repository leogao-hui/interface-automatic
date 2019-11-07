#_author:LEO GAO
#_project Encoding: UTF-8

import requests
from Common.config import header
from Common.apiUrl.smsController import smsControllerUrl


class SmsControllerFunction:

    def get_smsCode(self, data):
        '''

        :param data: case数据
        :return: response
        '''
        request = requests.session()
        response = request.get(headers=header, url=smsControllerUrl.send_sms_url, params=data)
        return response
