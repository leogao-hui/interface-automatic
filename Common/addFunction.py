# author:LEO GAO
# project Encoding:UTF-8


import requests
from .config import ci_url, add_direct_variable_url_ci, add_calculation_variable_url_ci, add_scale_variable_url_ci, \
add_display_variable_url_ci, add_information_structure_url_ci, add_root_template_url_ci, add_evaluate_url_ci, \
add_evaluate_version_url_ci, add_combo_url_ci, add_team_url_ci, add_team_member_url_ci, add_filling_url_ci, \
add_food_url_ci, add_food_label_library_url_ci, add_food_application_scene_library_url_ci, submit_question_url_ci,\
    generate_solution_url_ci, generate_evaluation_data_url_ci, add_solution_group_calculation_url_ci, get_system_variable_url_ci,\
    add_project_item_url_ci, add_solution_composition_url_ci, add_solution_group_display_url_ci, generate_report_url_ci,\
add_scheme_evaluation_url_ci


class AddFunction:

    # 获取系统变量
    def get_system_variable_ci(self, data):
        request = requests.session()
        response = request.post(url=get_system_variable_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['directVariableId']

    # 新增直接变量-题目接口
    def add_direct_variable_with_problem_ci(self, data):
        request = requests.session()
        response = request.post(url=add_direct_variable_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['directVariableId']

    # 修改直接变量-题目接口
    def modify_direct_variable_with_problem_ci(self, data):
        request = requests.session()
        url = '%s/api/rule/directVariable/%s' % (ci_url, data)
        response = request.put(url=url, data=data)
        print(response)

    # 新增计算变量接口
    def add_calculation_variable_ci(self, data):
        request = requests.session()
        response = request.post(url=add_calculation_variable_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['calcuVariableId']

    # 新增量表变量接口
    def add_scale_variable_ci(self, data):
        request = requests.session()
        response = request.post(url=add_scale_variable_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['scaleVariableId']

    # 新增显示变量接口
    def add_display_variable_ci(self, data):
        request = requests.session()
        response = request.post(url=add_display_variable_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['displayVariableId']

    # 新增信息结构接口
    def add_information_structure_ci(self, data):
        request = requests.session()
        response = request.post(url=add_information_structure_url_ci, data=data)
        print(response.status_code, response.json())

    # 新增根模板接口
    def add_root_template_ci(self, data):
        request = requests.session()
        response = request.post(url=add_root_template_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['rootTplId']

    # 新增评估项
    def add_evaluate_ci(self, data):
        request = requests.session()
        response = request.post(url=add_evaluate_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['evaluateItemId']

    # 新增评估版本
    def add_evaluate_version_ci(self, data):
        request = requests.session()
        response = request.post(url=add_evaluate_version_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['evVersionId']

    # 新增套餐
    def add_combo_ci(self, data):
        request = requests.session()
        response = request.post(url=add_combo_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['comboId']

    # 新增团队
    def add_team_ci(self, data):
        request = requests.session()
        response = request.post(url=add_team_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['teamId']

    # 新增成员
    def add_team_number_ci(self, data):
        request = requests.session()
        response = request.post(url=add_team_member_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['clerkId']

    # 新增建档
    def add_filing_ci(self, data):
        request = requests.session()
        response = request.post(url=add_filling_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['patientSurveyResultId']

    # 新增食材
    def add_food_ci(self, data):
        request = requests.session()
        response = request.post(url=add_food_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['foodMaterialId']

    # 新增食材标签
    def add_food_label_library(self, data):
        request = requests.session()
        response = request.post(url=add_food_label_library_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['foodMaterialTagId']

    # 新增食材应用场景库
    def add_food_application_scene_library(self, data):
        request = requests.session()
        response = request.post(url=add_food_application_scene_library_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['foodMaterialApplyScenarioId']

    # 提交题目
    def submit_question(self, data):
        request = requests.session()
        response = request.post(url=submit_question_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['patientSurveyResultItemId']

    # 生成报告
    def generate_report(self, data):
        request = requests.session()
        response = request.get(url=generate_report_url_ci, params=data)
        print(response.status_code)

    # 生成方案
    def generate_solution(self, data):
        request = requests.session()
        response = request.get(url=generate_solution_url_ci, params=data)
        print(response.status_code)

    # 测试数据构造
    def generate_evaluation_data(self, data):
        request = requests.session()
        response = request.get(url=generate_evaluation_data_url_ci, data=data)
        print(response.status_code)

    # 新增方案组专用计算变量
    def add_solution_group_solution_calculationVariable(self, data):
        request = requests.session()
        response = request.post(url=add_solution_group_calculation_url_ci, data=data)
        print(response.status_code)
        return response.json()['solutionCalcuVariableId']

    # 新增方案组专用量表变量
    def add_solution_group_solution_displayVariable(self, data):
        request = requests.session()
        response = request.post(url=add_solution_group_display_url_ci, data=data)
        print(response.status_code)
        return response.json()['solutionDisplayVariableId']

    # 新增方案项
    def add_project_item(self, data):
        request = requests.session()
        response = request.post(url=add_project_item_url_ci, data=data)
        print(response.status_code)
        return response.json()['solutionItemId']

    # 新增方案组成
    def add_solution_composition(self, data):
        request = requests.session()
        response = request.post(url=add_solution_composition_url_ci, data=data)
        print(response.status_code)
        return response.json()['solutionCompositionId']

    # 新增方案评定
    def add_scheme_evaluation(self, data):
        request = requests.session()
        response = request.post(url=add_scheme_evaluation_url_ci, data=data)
        print(response.status_code, response.json())
        return response.json()['solutionAssessmentId']

    # 修改题目状态
    def modify_survey_item(self, url, data):
        request = requests.session()
        response = request.put(url=url, data=data)
        print(response.status_code)

    # 获取题目
    def get_survey_item(self, url):
        request = requests.session()
        response = request.get(url=url)
        print(response.status_code)
        return response.json()['surveyItem']['id']


