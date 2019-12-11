#_author:LEO GAO
#_project Encoding: UTF-8


import unittest
import warnings
from Common.Data.loginData import login_basic_data, normal_login_data, not_account_login_data, \
    not_password_login_data, not_exist_account_login_data, wrong_password_login_data, \
    wrong_five_time_wrong_password_lock_account_login_data, after_lock_new_account_normal_login
from Common.config import json_dump, get_header
from Common.Log.log import log
from Common.operateDatabaseData import add_database_data_test_ci, delete_database_data_test_ci
from Common.apiFunction.System.systemConfigurationFun import login, exit_login
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
        add_user_information(get_header(response.json()['d']['authorization']),
                             json_dump(login_basic_data.add_user_data_one))
        add_user_information(get_header(response.json()['d']['authorization']),
                             json_dump(login_basic_data.add_user_data_two))
        add_user_information(get_header(response.json()['d']['authorization']),
                             json_dump(login_basic_data.add_user_data_three))

        add_user_information(get_header(response.json()['d']['authorization']),
                             json_dump(login_basic_data.add_user_data_four))
        exit_login(get_header(response.json()['d']['authorization']), json_dump(''))

    # 登录账号时，正常输入账号，密码，验证码，正常登录
    def test_normal_login(self):
        response = login(get_header(''), json_dump(normal_login_data.user_normal_login_data))
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json()['s'])
        self.assertEqual('登录成功', response.json()['m'])
        self.assertEqual(normal_login_data.add_user_data.get('username'), response.json()['d']['user']['username'])
        self.assertEqual(normal_login_data.add_user_data.get('userrole'), response.json()['d']['user']['userrole'])
        exit_login(get_header(response.json()['d']['authorization']), json_dump(''))
        case_name = '登录账号时，正常输入账号，密码，验证码，正常登录'
        if response.status_code == 200:
            log().info('%s 的接口is pass' % case_name)
        else:
            log().error('%s 的接口 is fail' % case_name, response.json())

    # 登录账号时，账号没填，正常输入密码，验证码，登录报错
    def test_not_account_login(self):
        response = login(get_header(''), json_dump(not_account_login_data.user_not_account_login_data))
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json()['s'])
        self.assertEqual('账号不能为空', response.json()['m'])
        case_name = '登录账号时，账号没填，正常输入密码，验证码，登录报错'
        if response.status_code == 200:
            log().info('%s 的接口is pass' % case_name)
        else:
            log().error('%s 的接口is fail' % case_name, response.json())

    # 登录账号时，密码没填，正常输入账号，验证码，登录报错
    def test_not_password_login(self):
        response = login(get_header(''), json_dump(not_password_login_data.user_not_password_login_data))
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json()['s'])
        self.assertEqual('密码不能为空', response.json()['m'])
        case_name = '登录账号时，密码没填，正常输入账号，验证码，登录报错'
        if response.status_code == 200:
            log().info('%s 的接口is pass' % case_name)
        else:
            log().error('%s 的接口is fail' % case_name, response.json())

    # 登录账号时，输入账号不存在，报错
    def test_not_exist_account(self):
        response = login(get_header(''), json_dump(not_exist_account_login_data.user_not_exist_account_login_data))
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json()['s'])
        self.assertEqual('登录信息有误，请确认后重新登录', response.json()['m'])
        case_name = '登录账号时，输入账号不存在，报错'
        if response.status_code == 200:
            log().info('%s 的接口is pass' % case_name)
        else:
            log().error('%s 的接口is fail' % case_name, response.json())

    # 登录账号时，输入密码错误，报错
    def test_wrong_password_login(self):
        response = login(get_header(''), json_dump(wrong_password_login_data.user_wrong_password_login_data))
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json()['s'])
        self.assertEqual('密码错误', response.json()['m'])
        case_name = '登录账号时，输入密码错误，报错'
        if response.status_code == 200:
            log().info('%s 的接口is pass' % case_name)
        else:
            log().error('%s 的接口is fail' % case_name, response.json())

    # 支持密码输入错误5次后，锁定账户5分钟
    def test_wrong_five_time_lock_account(self):
        for i in range(5):
            login(get_header(''), json_dump(wrong_five_time_wrong_password_lock_account_login_data.
                                            user_five_time_wrong_password_lock_account_login_data))
        response = login(get_header(''), json_dump(wrong_five_time_wrong_password_lock_account_login_data.
                                                   user_five_time_wrong_password_lock_account_login_data))
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json()['s'])
        self.assertEqual('您已5次输入密码错误，账户被锁定，请5分钟后再进行登录操作', response.json()['m'])
        case_name = '支持密码输入错误5次后，锁定账户5分钟'
        if response.status_code == 200:
            log().info('%s 的接口is pass' % case_name)
        else:
            log().error('%s 的接口is fail' % case_name, response.json())

    # 账号锁定时，输入新账号正常登录
    def test_after_lock_new_account_normal_login(self):
        for i in range(5):
            login(get_header(''), json_dump(after_lock_new_account_normal_login.
                                            user_five_time_wrong_password_lock_account_login_data))
        response = login(get_header(''), json_dump(after_lock_new_account_normal_login.new_account_data))
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json()['s'])
        self.assertEqual('登录成功', response.json()['m'])
        self.assertEqual('admin', response.json()['d']['user']['username'])
        self.assertEqual('管理员', response.json()['d']['user']['userrole'])
        exit_login(get_header(response.json()['d']['authorization']), json_dump(''))
        case_name = '登录账号时，正常输入账号，密码，验证码，正常登录'
        if response.status_code == 200:
            log().info('%s 的接口is pass' % case_name)
        else:
            log().error('%s 的接口 is fail' % case_name, response.json())

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()

