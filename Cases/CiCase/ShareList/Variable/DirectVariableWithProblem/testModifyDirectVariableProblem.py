# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import ci_url, println
from Common.addFunction import AddFunction
from Common.operateDatabaseData import add_database_data_ci, delete_database_data_test_ci


class TestModifyDirectVariableProblem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        add_func = AddFunction()
        height_data = {
            "variableName": "身高",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 250,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的身高是多少",
            "surveyItem[rank]": "100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        cls.direct_variable_problem_one = add_func.add_direct_variable_with_problem_ci(height_data)

        cls.url = '%s/api/rule/directVariable/%s' % (ci_url, cls.direct_variable_problem_one)
        cls.session = requests.session()

    # 修改直接变量题目名
    def test_modify_variable_title(self):
        modify_variable_name = {
            "variableName": "身高",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 250,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的身高是多少1",
            "surveyItem[rank]": "100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '修改直接变量题目名'
        self.session.put(url=self.url, data=modify_variable_name)
        response_get = self.session.get(url=self.url)
        modify_variable_title_get = response_get.json()['surveyItem']['title']
        if modify_variable_title_get == modify_variable_name['surveyItem[title]']:
            println(1, case_name)
            self.assertEqual(200, response_get.status_code)
        elif modify_variable_title_get != modify_variable_name['surveyItem[title]']:
            println(2, case_name)
            println(2, response_get.json())
            self.assertEqual(200, response_get.status_code)
        else:
            print('what fuck')

    # 修改直接变量题目取值范围最小值
    def test_modify_variable_range_least(self):
        modify_variable_name = {
            "variableName": "身高",
            "variableValueType": "numerical",
            "optionalValueMin": 0,
            "optionalValueMax": 250,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的身高是多少1",
            "surveyItem[rank]": "100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '修改直接变量题目取值范围最小值'
        self.session.put(url=self.url, data=modify_variable_name)
        response_get = self.session.get(url=self.url)
        modify_variable_range_get = response_get.json()['range']['min']
        if modify_variable_range_get == modify_variable_name['optionalValueMin']:
            println(1, case_name)
            self.assertEqual(200, response_get.status_code)
        elif modify_variable_range_get != modify_variable_name['optionalValueMin']:
            println(2, case_name)
            println(2, response_get.json())
            self.assertEqual(200, response_get.status_code)
        else:
            print('what fuck')

    # 修改直接变量题目取值范围最大值
    def test_modify_variable_range_largest(self):
        modify_variable_name = {
            "variableName": "身高",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 260,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的身高是多少",
            "surveyItem[rank]": "100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '修改直接变量题目取值范围最小值'
        self.session.put(url=self.url, data=modify_variable_name)
        response_get = self.session.get(url=self.url)
        modify_variable_range_get = response_get.json()['range']['max']
        if modify_variable_range_get == modify_variable_name['optionalValueMax']:
            println(1, case_name)
            self.assertEqual(200, response_get.status_code)
        elif modify_variable_range_get != modify_variable_name['optionalValueMax']:
            println(2, case_name)
            println(2, response_get.json())
            self.assertEqual(200, response_get.status_code)
        else:
            print('what fuck')

    # 修改直接变量题目拒绝答题
    def test_modify_variable_refuse(self):
        modify_variable_name = {
            "variableName": "身高",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 260,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的身高是多少",
            "surveyItem[rank]": "100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_not_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '修改直接变量题目拒绝答题'
        self.session.put(url=self.url, data=modify_variable_name)
        response_get = self.session.get(url=self.url)
        modify_variable_range_get = response_get.json()['surveyItem']['canRefuse']
        if modify_variable_range_get == modify_variable_name['surveyItem[canRefuse]']:
            println(1, case_name)
            self.assertEqual(200, response_get.status_code)
        elif modify_variable_range_get != modify_variable_name['surveyItem[canRefuse]']:
            println(2, case_name)
            println(2, response_get.json())
            self.assertEqual(200, response_get.status_code)
        else:
            print('what fuck')

    # 修改直接变量题目检测工具
    def test_modify_variable_detection_tools(self):
        modify_variable_name = {
            "variableName": "身高",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 260,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的身高是多少",
            "surveyItem[rank]": "100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_not_refuse",
            "surveyItem[device]": "device_two",
            "surveyItem[comment]": "",
        }
        case_name = '修改直接变量题目拒绝答题'
        self.session.put(url=self.url, data=modify_variable_name)
        response_get = self.session.get(url=self.url)
        modify_variable_range_get = response_get.json()['surveyItem']['device']
        if modify_variable_range_get == modify_variable_name['surveyItem[device]']:
            println(1, case_name)
            self.assertEqual(200, response_get.status_code)
        elif modify_variable_range_get != modify_variable_name['surveyItem[device]']:
            println(2, case_name)
            println(2, response_get.json())
            self.assertEqual(200, response_get.status_code)
        else:
            print('what fuck')

    # 修改直接变量题目方案组可用
    def test_modify_variable_solution_group_available(self):
        modify_variable_name = {
            "variableName": "身高",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 260,
            "isSolutionCanUse": "no",
            "surveyItem[title]": "您的身高是多少",
            "surveyItem[rank]": "100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_not_refuse",
            "surveyItem[device]": "device_two",
            "surveyItem[comment]": "",
        }
        case_name = '修改直接变量题目拒绝答题'
        self.session.put(url=self.url, data=modify_variable_name)
        response_get = self.session.get(url=self.url)
        modify_variable_range_get = response_get.json()['isSolutionCanUse']
        if modify_variable_range_get == modify_variable_name['isSolutionCanUse']:
            println(1, case_name)
            self.assertEqual(200, response_get.status_code)
        elif modify_variable_range_get != modify_variable_name['isSolutionCanUse']:
            println(2, case_name)
            println(2, response_get.json())
            self.assertEqual(200, response_get.status_code)
        else:
            print('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()




