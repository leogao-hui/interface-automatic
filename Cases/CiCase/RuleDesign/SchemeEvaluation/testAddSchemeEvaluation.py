# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData
from Common.config import ci_url, println


class TestAddSchemeEvaluation(unittest.TestCase):

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

        # 查看直接变量对应的id
        search_height_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_height_id)
        response_height_id = add_func.get_survey_item(url=search_height_url)
        search_job_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_job_id)
        response_job_id = add_func.get_survey_item(url=search_job_url)

        # 修改题目状态
        data_height = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '您的身高是多少',
            'groups[0][material][type]': '',
            'groups[0][material][url]': ''
        }
        height_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_height_id)
        add_func.modify_survey_item(url=height_url, data=data_height)

        data_job = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '您的职业是？',
            'groups[0][material][type]': '',
            'groups[0][material][url]': '',
            'groups[0][options][0][id]': '0',
            'groups[0][options][0][content]': '休养或退休',
            'groups[0][options][0][sort]': '0',
            'groups[0][options][0][displayContent]': '',
            'groups[0][options][0][canSelectedComment]': 'yes',
            'groups[0][options][0][orderInGroup]': '1',
            'groups[0][options][1][id]': '1',
            'groups[0][options][1][content]': '专业技术人员',
            'groups[0][options][1][sort]': '1',
            'groups[0][options][1][displayContent]': '',
            'groups[0][options][1][canSelectedComment]': 'yes',
            'groups[0][options][1][orderInGroup]': '1',
            'groups[0][options][2][id]': '1',
            'groups[0][options][2][content]': '行政办公人员',
            'groups[0][options][2][sort]': '2',
            'groups[0][options][2][displayContent]': '',
            'groups[0][options][2][canSelectedComment]': 'yes',
            'groups[0][options][2][orderInGroup]': '1',
            'groups[0][options][3][id]': '1',
            'groups[0][options][3][content]': '服务业人员',
            'groups[0][options][3][sort]': '3',
            'groups[0][options][3][displayContent]': '',
            'groups[0][options][3][canSelectedComment]': 'yes',
            'groups[0][options][3][orderInGroup]': '1',
        }
        job_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_job_id)
        add_func.modify_survey_item(url=job_url, data=data_job)

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

        # 新增计算变量方案组专用
        calculation_variable_three_data = {
            'name': '方案组专用计算变量',
            'optionalValues[0][matchExpression]': '*',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.response_calculation_three_id = add_func.add_solution_group_solution_calculationVariable(
            calculation_variable_three_data)

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
        cls.evaluateItemId_two_id = add_func.add_evaluate_ci(evaluate_two_data)

        # 新增方案项
        project_item_data = {
            'name': '方案项一',
            'module': 'movement_module'
        }
        cls.solutionItemId_one = add_func.add_project_item(project_item_data)

        # 新增食材
        food_data = {
            'serialNumber': 1,
            'name': '测试食材1',
            'aliases[0][name]': '别名1',
            'edibleCoefficient': 1,
            'color[0]': 'white',
            'giValue': 10,
            'status': 'solidState',
            'cookedFoodRation': 'not null',
            'cookedFoodRationPicture': '/a/b/c.jpg',
        }
        add_func.add_food_ci(food_data)

        cls.url = '%s/api/rule/solutionComposition' % ci_url
        cls.session = requests.session()

    # 正常新增方案评定
    def test_add_scheme_evaluation(cls):
        data = {
            'name': '测试方案评定',
            'solutionItemId': cls.solutionItemId_one,
            'conditionExpression': '*',
            'displayOrder': 1,
            'content': '[{"name":"方案评定结果","grade":"normal","displayContent":"具体显示内容","group":"1","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]},{"name":"方案评定结果2","grade":"anomaly","displayContent":"具体显示内容2","group":"2","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]}]',
            'comment': ''
        }
        case_name = '正常新增方案评定'
        response = cls.session.post(url=cls.url, data=data)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        else:
            print('what fuck')

    # 新增方案评定name为空
    def test_add_scheme_evaluation_name_null(cls):
        data = {
            'name': '',
            'solutionItemId': cls.solutionItemId_one,
            'conditionExpression': '*',
            'displayOrder': 1,
            'content': '[{"name":"方案评定结果","grade":"normal","displayContent":"具体显示内容","group":"1","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]},{"name":"方案评定结果2","grade":"anomaly","displayContent":"具体显示内容2","group":"2","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]}]',
            'comment': ''
        }
        case_name = '新增方案评定name为空'
        response = cls.session.post(url=cls.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 新增方案评定solutionItemId为空
    def test_add_scheme_evaluation_solutionItemId_null(cls):
        data = {
            'name': '测试',
            'solutionItemId': '',
            'conditionExpression': '*',
            'displayOrder': 1,
            'content': '[{"name":"方案评定结果","grade":"normal","displayContent":"具体显示内容","group":"1","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]},{"name":"方案评定结果2","grade":"anomaly","displayContent":"具体显示内容2","group":"2","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]}]',
            'comment': ''
        }
        case_name = '新增方案评定solutionItemId为空'
        response = cls.session.post(url=cls.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 新增方案评定solutionItemId不存在
    def test_add_scheme_evaluation_solutionItemId_not_exist(cls):
        data = {
            'name': '测试',
            'solutionItemId': int(cls.solutionItemId_one) - 1,
            'conditionExpression': '*',
            'displayOrder': 1,
            'content': '[{"name":"方案评定结果","grade":"normal","displayContent":"具体显示内容","group":"1","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]},{"name":"方案评定结果2","grade":"anomaly","displayContent":"具体显示内容2","group":"2","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]}]',
            'comment': ''
        }
        case_name = '新增方案组成solutionItemId不存在'
        response = cls.session.post(url=cls.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 新增方案评定conditionExpression为空
    def test_add_scheme_evaluation_conditionExpression_null(cls):
        data = {
            'name': '测试',
            'solutionItemId': cls.solutionItemId_one,
            'conditionExpression': '',
            'displayOrder': 1,
            'content': '[{"name":"方案评定结果","grade":"normal","displayContent":"具体显示内容","group":"1","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]},{"name":"方案评定结果2","grade":"anomaly","displayContent":"具体显示内容2","group":"2","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]}]',
            'comment': ''
        }
        case_name = '新增方案组成conditionExpression为空'
        response = cls.session.post(url=cls.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 新增方案评定content为空
    def test_add_solution_composition_content_null(cls):
        data = {
            'name': '测试',
            'solutionItemId': cls.solutionItemId_one,
            'conditionExpression': '',
            'displayOrder': 1,
            'content': '',
            'comment': ''
        }
        case_name = '新增方案组成content为空'
        response = cls.session.post(url=cls.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()



