#_author:LEO GAO
#_project Encoding: UTF-8


import unittest
from Common.config import json_dump
from Common.apiFunction.accountController.accountControllerFunction import AccountControllerFunction
from Common.apiFunction.smsController.smsControllerFunction import SmsControllerFunction
from Common.apiFunction.devOpsController.devOpsControllerFunction import DevOpsControllerFunction
from Common.Data.loginWithPasswordData import login_public_data ,login_normal_data, login_account_not_exist_data, \
    login_wrong_password_data, login_not_have_password_data
from Common.operateDatabaseData import delete_database_data_test_ci


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.AccountControllerFunction = AccountControllerFunction()
        cls.SmsControllerFunction = SmsControllerFunction()
        cls.DevOpsControllerFunction = DevOpsControllerFunction()

        # 发送验证码
        cls.SmsControllerFunction.get_smsCode(login_public_data.login_public_data)
        # 获取验证码
        sms_code = \
            cls.DevOpsControllerFunction.get_sms(json_dump(login_public_data.get_entry_account_data)).json()['payload'][
                'value']
        register_data = json_dump({
            "channel": "WS",
            "documentTypes": [
                "APP_REGISTRY"
            ],
            "password": "19961030gh",
            "phoneNum": login_public_data.login_public_data['phoneNum'],
            "smsCode": sms_code,
            "subChannel": "AND_DEFAULT"
        })
        # 注册
        cls.AccountControllerFunction.register_account(register_data)

    # 正常登陆
    def test_normal_login(cls):
        response = cls.AccountControllerFunction.login_with_password(json_dump(login_normal_data.login_normal_data))
        cls.assertEqual('成功', response.json()['message'])
        cls.assertEqual(200, response.json()['status'])

    # 用户名不存在
    def test_account_not_exist_login(cls):
        response = cls.AccountControllerFunction.login_with_password(
            json_dump(login_account_not_exist_data.login_account_not_exist_data))
        cls.assertEqual(400106, response.json()['status'])
        cls.assertEqual('账户未找到!', response.json()['message'])

    # 密码错误
    def test_wrong_password(cls):
        response = cls.AccountControllerFunction.login_with_password(
            json_dump(login_wrong_password_data.login_wrong_password_data))
        cls.assertEqual(400107, response.json()['status'])
        cls.assertEqual('登录密码错误', response.json()['message'])

    # 密码字段没传
    def test_not_have_password(cls):
        response = cls.AccountControllerFunction.login_with_password(
            json_dump(login_not_have_password_data.login_not_have_password_data))
        cls.assertEqual(500002, response.json()['status'])
        cls.assertEqual('[Validation Error][{\"field\":\"password\",\"message\":\"登陆密码不能为空\"}]',
                        response.json()['message'])

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()


