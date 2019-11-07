#_author:LEO GAO
#_project Encoding: UTF-8

import requests
from Common.config import header
from Common.apiUrl.accountController.accountControllerUrl import account_check_url,login_with_pw_url, account_register_url


class AccountControllerFunction:

    # 验证账户存在
    def account_check(self, data):
        '''

        :param data: case数据
        :return: response
        '''
        request = requests.session()
        response = request.post(headers=header, url=account_check_url, data=data)
        return response

    # 密码登录
    def login_with_password(self, data):
        '''

        :param data: case数据
        :return: response
        '''
        request = requests.session()
        response = request.post(headers=header, url=login_with_pw_url, data=data)
        return response

    # 用户注册
    def register_account(self, data):
        '''

        :param data: case数据
        :return: response
        '''
        request = requests.session()
        response = request.post(headers=header, url=account_register_url, data=data)
        return response
