#_author:LEO GAO
#_project Encoding: UTF-8


import requests
import unittest
from Common.Log.log import log
from Common.apiFunction.accountController.accountControllerFunction import AccountControllerFunction
from Common.apiFunction.smsController.smsControllerFunction import SmsControllerFunction


class TestLoginCount(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.AccountControllerFunction = AccountControllerFunction()
        cls.SmsControllerFunction = SmsControllerFunction()

    # 测试密码登录
    def testlogin(cls):
        cls.assertEqual(200, cls.AccountControllerFunction.login_with_password())
        log().info('测试密码登录pass')