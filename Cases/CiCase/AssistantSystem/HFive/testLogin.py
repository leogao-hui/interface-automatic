# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import ci_url, println
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.addFunction import AddFunction


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_func = AddFunction()
        # 新增团队
        team_data_one = {
            'name': '测试团队'
        }

        cls.teamId_one = add_func.add_team_ci(team_data_one)

        # 新增成员
        team_member_data_one = {
            'phone': '123456',
            'password': '123456',
            'name': '123456',
            'belongTeamId': cls.teamId_one,
            'identity': 'manager'
        }

        cls.clerkId_one = add_func.add_team_number_ci(team_member_data_one)

    def setUp(self):
        self.url = '%s/api/collection/login' % ci_url
        self.session = requests.session()

    # 正常登陆
    def test_normal_login01(self):
        body = {
            'account': '123456',
            'password': '123456'
        }
        case_name = '正常登陆'
        response = self.session.post(url=self.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # 账号不存在
    def test_abnormal_login01(self):
        body = {
            'account': '1',
            'password': '123456'
        }
        case_name = '账号不存在'
        response = self.session.post(url=self.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 密码错误
    def test_abnormal_login02(self):
        body = {
            'account': '123456',
            'password': '123'
        }
        case_name = '密码错误'
        response = self.session.post(url=self.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 账号必填
    def test_abnormal_login03(self):
        body = {
            'account': '',
            'password': '123'
        }
        case_name = '账号必填'
        response = self.session.post(url=self.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 密码必填
    def test_abnormal_login04(self):
        body = {
            'account': '123456',
            'password': ''
        }
        case_name = '密码必填'
        response = self.session.post(url=self.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()
