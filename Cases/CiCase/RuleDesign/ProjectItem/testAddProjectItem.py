# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import ci_url
from Common.config import println
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci


class TestAddProjectItem(unittest.TestCase):

    def setUp(self):
        delete_database_data_test_ci()
        add_database_data_ci()
        self.url = '%s/api/rule/solutionItem' % ci_url
        self.session = requests.session()

    # 正常新增方案项
    def test_add_solution_item(self):
        data = {
            'name': '方案项一',
            'module': 'movement_module'
        }
        response = self.session.post(url=self.url, data=data)
        case_name = '正常新增方案项'
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            self.assertEqual(200, response.status_code, response.json())
        else:
            print('what fuck')

    # 方案项变量名为空
    def test_add_solution_item_name_null(self):
        data = {
            'name': '',
            'module': 'movement_module'
        }
        response = self.session.post(url=self.url, data=data)
        case_name = '方案项变量名为空'
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案项所属模块为空
    def test_add_solution_item_module_null(self):
        data = {
            'name': '测试方案项',
            'module': ''
        }
        response = self.session.post(url=self.url, data=data)
        case_name = '方案项所属模块为空'
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    def tearDown(self):
        delete_database_data_test_ci()



