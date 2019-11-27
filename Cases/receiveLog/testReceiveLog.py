#_author:leo gao
#encoding:utf-8

import unittest
import warnings
from Common.apiFunction.backgroundManagement.logManagementFun import receive_log
from Common.apiFunction.System.systemConfigurationFun import login
from Common.apiFunction.backgroundManagement.userManagementFun import add_user_information
from Common.Data.receiveLogData import wrong_login_log_data
from Common.config import json_dump, get_header
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_test_ci


class TestReceiveLog(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)  # 去除requests中多余的warning
        delete_database_data_test_ci()
        add_database_data_test_ci()

    # 账号密码输入错误，日志正常记录
    def test_wrong_login_log(self):
        # 登录管理员账号
        response = login(get_header(''), json_dump(wrong_login_log_data.administrator_login_data))
        # 新增人员
        add_user_information(get_header(response.json()['d']['authorization']),
                             json_dump(wrong_login_log_data.add_user_data))
        # 错误登录
        login(get_header(''), json_dump(wrong_login_log_data.user_wrong_password_login_data))
        login(get_header(''), json_dump(wrong_login_log_data.user_wrong_password_login_data))







