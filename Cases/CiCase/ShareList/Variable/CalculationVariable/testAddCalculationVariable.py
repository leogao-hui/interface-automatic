# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import ci_url , println
from Common.addFunction import AddFunction
from Common.operateDatabaseData import delete_database_data_test_ci
from Common.operateDatabaseData import add_database_data_ci


class TestAddCalculationVariable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()

    def setUp(self):
        self.add_func = AddFunction()
        self.url = '%s/api/rule/calcuVariable' % ci_url
        self.session = requests.session()

    # 测试正常新增计算变量
    def test_normal_calculationVariable_create01(self):
        body = {
            'name': '计算变量1',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '1+1',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        case_name = '测试正常新增计算变量'
        response = self.session.post(self.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # 测试计算变量包含计算变量
    def test_normal_calculationVariable_create02(self):
        '''
        url = '%s/api/rule/directVariable' % front_url
        body_one = {
            'name': '计算变量1',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '1+1',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        self.session.post(url=url, data=body_one)
        '''
        body_two = {
            'name': '测试计算变量',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '10',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        case_name = '测试计算变量包含计算变量'
        response = self.session.post(self.url, data=body_two)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # 测试计算变量表达式必填
    def test_abnormal_calculationVariable_create01(self):
        body_two = {
            'name': '测试计算变量1',
            'optionalValues[0][matchExpression]': '',
            'optionalValues[0][content]': '10',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        case_name = '测试计算变量表达式必填'
        response = self.session.post(self.url, data=body_two)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 测试计算变量内容必填
    def test_abnormal_calculationVariable_create02(self):
        body_two = {
            'name': '测试计算变量2',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        case_name = '测试计算变量内容必填'
        response = self.session.post(self.url, data=body_two)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 测试计算变量优先级必填
    def test_abnormal_calculationVariable_create03(self):
        body_two = {
            'name': '测试计算变量3',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '*',
            'optionalValues[0][priority]': '',
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        case_name = '测试计算变量优先级必填'
        response = self.session.post(self.url, data=body_two)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 测试计算变量变量名必填
    def test_abnormal_calculationVariable_create04(self):
        body_two = {
            'name': '',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '*',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        case_name = '测试计算变量变量名必填'
        response = self.session.post(self.url, data=body_two)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 测试计算变量中包含的变量名必填
    def test_abnormal_calculationVariable_create05(self):
        body_two = {
            'name': '',
            'optionalValues[0][matchExpression]': '身高>10',
            'optionalValues[0][content]': '*',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        case_name = '测试计算变量中包含的变量名必填'
        response = self.session.post(self.url, data=body_two)
        self.assertEqual(422, response.status_code)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 测试计算变量中用到搜索选择题 报错
    def test_abnormal_calculationVariable_have_searchChoiceVariable(self):
        direct_variable_data = {
            "variableName": "测试搜索选择题键值对",
            "variableValueType": "key_value",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试搜索选择题键值对型？",
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[rank]": "1600",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "search_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        self.add_func.add_direct_variable_with_problem_ci(direct_variable_data)
        body = {
            'name': '计算变量22',
            'optionalValues[0][matchExpression]': '测试搜索选择题键值对=1',
            'optionalValues[0][content]': '1+1',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        case_name = '测试计算变量中用到搜索选择题 报错'
        response = self.session.post(self.url, data=body)
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
