# author:LEO GAO
# project Encoding:UTF-8

'''
import unittest
import requests
from Common.addFunction import AddFunction
from Common.manyData import manyData
from Common.coreData import CoreData
from Common.config import front_url
import warnings


class TestImportantCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        add_func = AddFunction()
        warnings.simplefilter("ignore", ResourceWarning)

        # 新增直接变量
        add_func.add_direct_variable_with_problem_(manyData.height_data)
        add_func.add_direct_variable_with_problem_(manyData.job_data)
        add_func.add_direct_variable_with_problem_(manyData.tumor_data)
        add_func.add_direct_variable_with_problem_(manyData.treatment_stage_data)
        add_func.add_direct_variable_with_problem_(manyData.hobby_data)
        add_func.add_direct_variable_with_problem_(manyData.height_data_1)
        add_func.add_direct_variable_with_problem_(manyData.height_data_2)
        add_func.add_direct_variable_with_problem_(manyData.height_data_3)
        add_func.add_direct_variable_with_problem_(manyData.height_data_4)
        add_func.add_direct_variable_with_problem_(manyData.height_data_5)
        add_func.add_direct_variable_with_problem_(manyData.height_data_6)
        add_func.add_direct_variable_with_problem_(manyData.height_data_7)
        add_func.add_direct_variable_with_problem_(manyData.height_data_8)
        add_func.add_direct_variable_with_problem_(manyData.height_data_9)
        add_func.add_direct_variable_with_problem_(manyData.height_data_10)
        add_func.add_direct_variable_with_problem_(manyData.height_data_11)

        # 新增计算变量
        add_func.add_calculation_variable(CoreData.calculation_variable_one_data)
        add_func.add_calculation_variable(CoreData.calculation_variable_two_data)

        # 新增量表变量
        add_func.add_scale_variable(CoreData.scale_variable_one_data)

        # 新增信息结构
        add_func.add_information_structure(CoreData.information_structure_one_data)
        add_func.add_information_structure(CoreData.information_structure_two_data)

        # 新增根模板
        add_func.add_root_template(CoreData.root_template_data)

        # 新增评估项
        add_func.add_evaluate(CoreData.evaluate_one_data)

        # add_func.add_evaluate(manyData.evaluate_two_data)
        # add_func.add_evaluate(manyData.evaluate_three_data)

        # 新增评估版本
        add_func.add_evaluate_version(CoreData.evaluate_version_one_data)

        # 新增套餐
        add_func.add_combo(CoreData.combo_data)

        # 新增团队
        add_func.add_team(CoreData.team_data)

        # 新增团队人员
        add_func.add_team_number(CoreData.team_member_one_data)

    def setUp(self):
        # 新增建档
        url = '%s/api/collection/patient' % front_url
        filling_data = {
            'clerkId': 1,
            'comboId': 1,
            'name': '测试人',
            'phone': '13342423242',
            'sex': '男',
            'birthAt': '456',
            'representor': 'adadd',
            'nation': 'qdw',
            'address': 'dwdq',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        self.session = requests.session()
        response1 = self.session.post(url=url, data=filling_data)
        self.patientSurveyResultId = response1.json()['patientSurveyResultId']
        self.url = '%s/api/collection/patientSurveyResult/%s/nextSurveyItem' % (front_url, self.patientSurveyResultId)
        self.response = self.session.get(url=self.url)

    def test_TIME_answer01(self):
        # 提交第一题
        url_post = '%s/api/collection/patientSurveyResultItem' % front_url
        body_one = {
            'patientSurveyResultId': self.patientSurveyResultId,
            'surveyItemId': 1,
            'blankContent': 50,
        }
        response1 = self.session.post(url=url_post, data=body_one)
        self.assertEqual(200, response1.status_code)

        # 获取第二题
        url_get_next = '%s/api/collection/patientSurveyResult/%s/nextSurveyItem' % (front_url, self.patientSurveyResultId)
        par_get_next = {
            'surveyItemId': 1
        }
        response2 = self.session.get(url=url_get_next, params=par_get_next)
        self.assertEqual(204, response2.status_code)
        print(response2.elapsed.total_seconds())
'''

