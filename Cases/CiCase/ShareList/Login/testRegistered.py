

import unittest
import requests
from Common.Log.log import log
from Common.apiFunction.accountController.accountControllerFunction import AccountControllerFunction


class TestRegisteredCount(unittest.TestCase):

    def setUp(self):
        self.AccountControllerFunction = AccountControllerFunction()

    # 测试密码登录
    def testlogin(self):
        self.assertEqual(200, self.AccountControllerFunction.login_with_password())
        log().info('测试密码登录pass')





