#_author:LEO GAO
#_project Encoding: UTF-8


import unittest
import warnings
from Common.Data.loginData import login_basic_data, normal_login_data
from Common.config import json_dump, get_header
from Common.operateDatabaseData import add_database_data_test_ci, delete_database_data_test_ci
from Common.apiFunction.System.systemConfigurationFun import login
from Common.apiFunction.backgroundManagement.userManagementFun import add_user_information


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)  # 去除requests中多余的warning
        delete_database_data_test_ci()  # 清空数据库
        add_database_data_test_ci()  # 新增配置数据
        # 登录管理员账号
        response = login(get_header(''), json_dump(login_basic_data.administrator_login_data))
        # 新增人员
        add_user_information(get_header(response.json()['d']['authorization']), json_dump(normal_login_data.add_user_data))


    def test_login(self):
        response = login(get_header(''), json_dump(normal_login_data.user_login_data))
        self.assertEqual(True, response.json()['s'])
        self.assertEqual('登录成功', response.json()['m'])
        self.assertEqual(normal_login_data.add_user_data.get('username'), response.json()['d']['user']['username'])
        self.assertEqual(normal_login_data.add_user_data.get('userrole'), response.json()['d']['user']['userrole'])




