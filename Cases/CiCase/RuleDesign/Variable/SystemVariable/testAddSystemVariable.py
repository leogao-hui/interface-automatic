# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import get_system_variable_url_ci
from Common.operateDatabaseData import delete_database_data_test_ci


class TestAddSystemVariable(unittest.TestCase):

    def setUp(self):
        self.url = get_system_variable_url_ci
        self.session = requests.session()

    def test_normal_systemVariable_get_sex(self):
        body = {
            'name': '性别'
        }
        response = self.session.post(url=self.url, data=body)
        print(response.json())
        self.assertEqual(200, response.status_code)

    def test_normal_systemVariable_get_age(self):
        body = {
            'name': '年龄'
        }
        response = self.session.post(url=self.url, data=body)
        print(response.json())
        self.assertEqual(200, response.status_code)

    # 查看答题时是否出现带有系统变量的题目
    def test_01(self):
        pass

    # 当有系统变量时,查看可用变量查询,可用评估查询
    def test_02(self):
        pass

    # 查看直接变量时查看系统变量是否存在
    def test_03(self):
        pass

    #
    def test_04(self):
        pass

    def tearDown(self):
        delete_database_data_test_ci()
