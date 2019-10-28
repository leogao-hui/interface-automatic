# author:LEO GAO
# project Encoding:UTF-8

import unittest
import requests
from Common.config import add_direct_variable_url_ci
from Common.config import println
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.addFunction import AddFunction


class TestValidation(unittest.TestCase):

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
        cls.response_height_id = add_func.add_direct_variable_with_problem_ci(height_data)

        job_data = {
            "variableName": "职业",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": "休养或退休",
            "optionalValues[0][sort]": "1",
            "optionalValues[1][variableValue]": "专业技术人员",
            "optionalValues[1][sort]": "2",
            "optionalValues[2][variableValue]": "行政办公人员",
            "optionalValues[2][sort]": "3",
            "optionalValues[3][variableValue]": "服务业人员",
            "optionalValues[3][sort]": "4",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的职业是？",
            "surveyItem[rank]": "90",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "multiple_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "comment",
            "surveyItem[options][0][surveyItemValue]": "休养或退休",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "专业技术人员",
            "surveyItem[options][1][sort]": "2",
            "surveyItem[options][2][surveyItemValue]": "行政办公人员",
            "surveyItem[options][2][sort]": "3",
            "surveyItem[options][3][surveyItemValue]": "服务业人员",
            "surveyItem[options][3][sort]": "4",
            "surveyItem[preConditionItems][0][matchExp]": "身高>100",
            "surveyItem[preConditionItems][0][description]": "显示条件",
            "surveyItem[preConditionItems][0][comment]": "1111",

        }
        cls.response_job_id = add_func.add_direct_variable_with_problem_ci(job_data)

    def setUp(self):
        self.url = add_direct_variable_url_ci
        self.session = requests.session()

    def test_two_big_than_self(self):
        data = {
            "variableName": "体重",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 250,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的体重是多少",
            "surveyItem[rank]": "80",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[preConditionItems][0][matchExp]": "(身高>100)&(职业$1(休养或退休))",
            "surveyItem[preConditionItems][0][description]": "显示条件",
            "surveyItem[preConditionItems][0][comment]": "1111",
        }
        case_name = '显示条件中2道题目的序号都比自身的题目序号大，正常保存'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    def test_two_small_than_self(self):
        data = {
            "variableName": "体重1",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 250,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的体重是多少1",
            "surveyItem[rank]": "110",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[preConditionItems][0][matchExp]": "(身高>100)&(职业$1(休养或退休))",
            "surveyItem[preConditionItems][0][description]": "显示条件",
            "surveyItem[preConditionItems][0][comment]": "1111",
        }
        case_name = '显示条件中2道题目的序号都比自身的题目序号小，查看报错'
        response = self.session.post(self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    def test_big_small(self):
        data = {
            "variableName": "体重2",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 250,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的体重是多少2",
            "surveyItem[rank]": "95",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[preConditionItems][0][matchExp]": "(身高>100)&(职业$1(休养或退休))",
            "surveyItem[preConditionItems][0][description]": "显示条件",
            "surveyItem[preConditionItems][0][comment]": "1111",
        }
        case_name = '显示条件中一道题的序号比自身的序号小，一道比自身的序号大，查看报错'
        response = self.session.post(self.url, data=data)
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


