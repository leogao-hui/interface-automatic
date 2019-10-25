# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData
from Common.config import ci_url, println


class TestAddSolutionGroupSpecificDisplayVariables(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        add_func = AddFunction()

        # 新增直接变量常规
        height_data = {
            "variableName": "身高",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 250,
            "isSolutionCanUse": "no",
            "surveyItem[title]": "您的身高是多少",
            "surveyItem[rank]": "100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        cls.response_height_id = add_func.add_direct_variable_with_problem_ci(height_data)

        # 新增直接变量方案组可用
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

        # 新增计算变量常规
        calculation_variable_one_data = {
            'name': '计算变量一',
            'optionalValues[0][matchExpression]': '职业$1(休养或退休)',
            'optionalValues[0][content]': '身高+20',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.response_calculation_one_id = add_func.add_calculation_variable_ci(calculation_variable_one_data)

        # 新增计算变量方案组可用
        calculation_variable_two_data = {
            'name': '计算变量二',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '2',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.response_calculation_two_id = add_func.add_calculation_variable_ci(calculation_variable_two_data)

        # 新增量表变量常规
        scale_variable_one_data = {
            'name': '量表变量一',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][calcuRule]': 'sum',
            'optionalValues[0][rDirectVars][0][variableName]': '身高',
            'optionalValues[0][rDirectVars][0][valueCalcuRule]': 'max',
            'optionalValues[0][rDirectVars][0][comment]': 'aaaa',
            'optionalValues[0][rDirectVars][0][scoreItems][0][matchExp]': '*',
            'optionalValues[0][rDirectVars][0][scoreItems][0][score]': 20,
            'comment': 'aaa',
            'isSolutionCanUse': 'no'
        }
        # 新增量表变量方案组
        cls.response_scale_one_id = add_func.add_scale_variable_ci(scale_variable_one_data)

        scale_variable_two_data = {
            'name': '量表变量二',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][calcuRule]': 'sum',
            'optionalValues[0][rDirectVars][0][variableName]': '身高',
            'optionalValues[0][rDirectVars][0][valueCalcuRule]': 'max',
            'optionalValues[0][rDirectVars][0][comment]': 'aaaa',
            'optionalValues[0][rDirectVars][0][scoreItems][0][matchExp]': '*',
            'optionalValues[0][rDirectVars][0][scoreItems][0][score]': 20,
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        # 新增量表变量
        cls.response_scale_two_id = add_func.add_scale_variable_ci(scale_variable_two_data)

        # 新增信息结构
        add_func.add_information_structure_ci(CoreVersionData.information_structure_one_data)
        add_func.add_information_structure_ci(CoreVersionData.information_structure_two_data)

        # 新增根模板
        cls.rootTplId = add_func.add_root_template_ci(CoreVersionData.root_template_data)

        evaluate_one_data = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '标签二',
            'rank': 1,
            'name': '测试评估名1',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(计算变量二>50)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'no',
            'comment': '111'
        }
        evaluate_two_data = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '标签二',
            'rank': 2,
            'name': '测试评估名2',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(测试评估名1=匹配用结果项名1)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }
        # 新增评估项
        cls.evaluateItemId_one_id = add_func.add_evaluate_ci(evaluate_one_data)  # 常规
        cls.evaluateItemId_two_id = add_func.add_evaluate_ci(evaluate_two_data)  # 方案组可用

    def setUp(self):
        self.url = '%s/api/rule/solutionDisplayVariable' % ci_url
        self.session = requests.session()

    # 测试新增方案组专用显示变量
    def test_add_solution_group_specific_scaleVariable_normal(self):
        data = {
            'name': '方案组专用显示变量',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '11',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': '11',
            'module': 'movement_module'
        }
        case_name = '测试新增方案组专用显示变量'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用变量匹配表达式必填
    def test_add_solution_group_specific_scaleVariable_not_matchExpression(self):
        data = {
            'name': '方案组专用量表变量测试',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示变量匹配表达式必填'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组量表变量变量值内容必填
    def test_add_solution_group_specific_calculation_not_content(self):
        data = {
            'name': '方案组专用显示变量测试',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示变量变量值内容必填'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用变量优先级必填
    def test_add_solution_group_specific_calculation_not_priority(self):
        data = {
            'name': '方案组专用显示变量测试',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '1+1',
        'optionalValues[0][priority]': '',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用量表变量优先级必填'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用变量module必填
    def test_add_solution_group_specific_calculation_not_module(self):
        data = {
            'name': '方案组专用变量值内容变量测试',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '1+1',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': '11',
            'module': '',
            'comment': ''
        }
        case_name = '测试方案组专用量表变量comment必填'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用量表变量变量名重复
    def test_add_solution_group_specific_scaleVariable_name_repeat(self):
        data = {
            'name': '方案组专用量表变量测试',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '11',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '11',
            'module': 'movement_module'
        }
        self.session.post(url=self.url, data=data)
        data_two = {
            'name': '方案组专用量表变量测试',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '11',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '11',
            'module': 'movement_module'
        }
        case_name = '测试方案组专用量表变量变量名重复'
        response = self.session.post(url=self.url, data=data_two)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用量表变量适用条件中可以使用方案组可用直接变量-题目
    def test_add_solution_group_specific_scaleVariable_expression_have_scheme_available_group_variable(self):
        data = {
            'name': '方案组专用量表变量测试直接变量',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '职业$1(休养或退休)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用量表变量适用条件中可以使用方案组可用直接变量-题目'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中不可以使用常规直接变量-题目
    def test_add_solution_group_specific_scaleVariable_expression_have_conventional_variable(self):
        data = {
            'name': '方案组专用显示变量测试常规',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '身高>90',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示变量适用条件中不可以使用方案组可用直接变量-题目'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中可以使用方案组可用计算变量
    def test_add_solution_group_specific_scaleVariable_expression_have_scheme_available_group_calculation(self):
        data = {
            'name': '方案组专用显示变量测试计算变量',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '计算变量二>50',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示变量适用条件中可以使用方案组可用计算变量'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            println('what fuck')
    '''
    # 测试方案组专用显示变量适用条件中可以使用方案组专用计算变量
    def test_add_solution_group_specific_scaleVariable_expression_have_solution_group_calculation(self):
        data = {
            'name': '方案组专用显示变量测试计算变量专用一',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        self.session.post(url=self.url, data=data)
        data_two = {
            'name': '方案组专用显示变量测试计算变量专用二',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '方案组专用计算变量测试计算变量专用一>60',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示变量适用条件中可以使用方案组专用计算变量'
        response = self.session.post(url=self.url, data=data_two)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            println('what fuck')
        
    # 测试方案组专用显示适用条件中不可以使用常规计算变量
    def test_add_solution_group_specific_scaleVariable_expression_have_conventional_calculation(self):
        data = {
            'name': '常规计算变量测试计算变量',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '计算变量一>70',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示适用条件中不可以使用常规计算变量'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')
    '''
    # 测试方案组专用显示变量适用条件中可以使用方案组可用量表变量
    def test_add_solution_group_specific_scaleVariable_expression_have_scheme_available_group_scaleVariable(self):
        data = {
            'name': '常规计算变量测试计算变量可用方案组显示变量',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '量表变量二>60',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示变量适用条件中可以使用方案组可用量表变量'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中不可以使用常规量表变量
    def test_add_solution_group_specific_scaleVariable_expression_have_conventional_scaleVariable(self):
        data = {
            'name': '常规计算变量测试计算变量常规组量表变量',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '量表变量一>60',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示变量适用条件中不可以使用常规量表变量'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中不可以使用常规评估项
    def test_add_solution_group_specific_scaleVariable_expression_have_conventional_evaluate(self):
        data = {
            'name': '常规计算变量测试计算变量常规评估项',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '测试评估名1=匹配用结果项名1',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用显示变量适用条件中不可以使用常规评估项'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中中可以使用方案组可用评估项
    def test_add_solution_group_specific_scaleVariable_expression_have_scheme_available_group_evaluate(self):
        data = {
            'name': '常规计算变量测试计算变量方案组可用评估项',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '测试评估名2=匹配用结果项名1',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用计算变量计算表达式中可以使用方案组可用评估项'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中中可以使用*
    def test_add_solution_group_specific_scaleVariable_expression_have_star(self):
        data = {
            'name': '常规计算变量测试计算变量方案组可用评估项',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        case_name = '测试方案组专用计算变量计算表达式中可以使用*'
        response = self.session.post(url=self.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()


