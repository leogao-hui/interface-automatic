# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
import json
from Common.Log.log import log
from Common.config import json_dump
from Common.apiFunction.accountController.accountControllerFunction import AccountControllerFunction
from Common.apiFunction.smsController.smsControllerFunction import SmsControllerFunction
from Common.apiFunction.devOpsController.devOpsControllerFunction import DevOpsControllerFunction
from Common.Data.registerData import not_account_data, send_smsCode_data, register_common_data, register_repeat_data, have_account_data
from Common.operateDatabaseData import delete_database_data_test_ci


class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        cls.AccountControllerFunction = AccountControllerFunction()
        cls.SmsControllerFunction = SmsControllerFunction()
        cls.DevOpsControllerFunction = DevOpsControllerFunction()

    # 验证没有账户
    def test_not_have_account(cls):
        response = cls.AccountControllerFunction.account_check(not_account_data.account_check_data)
        cls.assertEqual(200, response.json()['status'])
        cls.assertEqual(False, response.json()['payload'])
        cls.assertEqual('成功', response.json()['message'])

    # 验证有账户
    def test_have_account(cls):
        cls.SmsControllerFunction.get_smsCode(have_account_data.have_account_data)
        sms_code = cls.DevOpsControllerFunction.get_sms(json_dump(have_account_data.get_entry_account_data)).json()['payload']['value']
        register_data = json_dump({
            "channel": "WS",
            "documentTypes": [
                "APP_REGISTRY"
            ],
            "password": "19961030gh",
            "phoneNum": have_account_data.have_account_data['phoneNum'],
            "smsCode": sms_code,
            "subChannel": "AND_DEFAULT"
        })
        cls.AccountControllerFunction.register_account(register_data)
        response = cls.AccountControllerFunction.account_check(have_account_data.have_account_data['phoneNum'])
        cls.assertEqual(200, response.json()['status'])
        cls.assertEqual(True, response.json()['payload'])
        cls.assertEqual('成功', response.json()['message'])

   # 正常获取验证码
    def test_get_smsCode_normal(cls):
        response = cls.SmsControllerFunction.get_smsCode(send_smsCode_data.send_smsCode_data_normal)
        cls.assertEqual(200, response.json()['status'])
        cls.assertEqual(True, response.json()['payload'])
        cls.assertEqual('成功', response.json()['message'])

    # # 获取验证码输入手机号为空
    # def test_get_smsCode_not_phoneNum(cls):
    #     response = cls.SmsControllerFunction.get_smsCode(send_smsCode_data.send_smsCode_data_empty)
    #     print(response.json())
    #     cls.assertEqual(False, response.json()['payload'])
    #     cls.assertEqual('500002', response.json()['status'])
    #     cls.assertEqual('成功', response.json()['message'])

    # 正常注册账号
    def test_register_account(cls):
        # 发送验证码
        cls.SmsControllerFunction.get_smsCode(register_common_data.register_common_data)
        # 获取验证码
        sms_code = cls.DevOpsControllerFunction.get_sms(json_dump(register_common_data.get_entry_common_data)).json() ['payload']['value']
        register_data = json_dump({
            "channel": "WS",
            "documentTypes": [
                "APP_REGISTRY"
            ],
            "password": "19961030gh",
            "phoneNum": register_common_data.register_common_data['phoneNum'],
            "smsCode": sms_code,
            "subChannel": "AND_DEFAULT"
        })
        response = cls.AccountControllerFunction.register_account(register_data)
        cls.assertEqual(200, response.json()['status'])
        cls.assertEqual(True, response.json()['payload'])
        cls.assertEqual('成功', response.json()['message'])

    # 注册账号重复
    def test_register_account_repeat(cls):
        # 发送验证码
        cls.SmsControllerFunction.get_smsCode(register_repeat_data.register_repeat_data)
        # 获取验证码
        sms_code_first = cls.DevOpsControllerFunction.get_sms(json_dump(register_repeat_data.get_entry_common_data)).json()['payload']['value']
        register_data_first = json_dump({
            "channel": "WS",
            "documentTypes": [
                "APP_REGISTRY"
            ],
            "password": "19961030gh",
            "phoneNum": register_repeat_data.register_repeat_data['phoneNum'],
            "smsCode": sms_code_first,
            "subChannel": "AND_DEFAULT"
        })
        cls.AccountControllerFunction.register_account(register_data_first)
        cls.SmsControllerFunction.get_smsCode(register_repeat_data.register_repeat_data)
        sms_code_twice = cls.DevOpsControllerFunction.get_sms(json_dump(register_repeat_data.get_entry_common_data)).json()['payload']['value']
        register_data_twice = json_dump({
            "channel": "WS",
            "documentTypes": [
                "APP_REGISTRY"
            ],
            "password": "19961030gh",
            "phoneNum": register_repeat_data.register_repeat_data['phoneNum'],
            "smsCode": sms_code_twice,
            "subChannel": "AND_DEFAULT"
        })
        response = cls.AccountControllerFunction.register_account(register_data_twice)
        cls.assertEqual(400102, response.json()['status'])
        cls.assertEqual('账户已存在', response.json()['message'])

    @ classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()




