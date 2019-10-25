# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData
from Common.config import ci_url, println
import warnings


class TestValidationExpression(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        add_func = AddFunction()
        warnings.simplefilter("ignore", ResourceWarning)
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
            'isSolutionCanUse': 'no'
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

        solution_group_available_display_variable_data_one = {
            'name': '显示变量一',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '量表变量二=20',
            'optionalValues[0][content]': '显示内容',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': 'comment',
            'isSolutionCanUse': 'no',
            'comment': '111'
        }
        cls.display_one = add_func.add_display_variable_ci(solution_group_available_display_variable_data_one)

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
                       '"content":[{"表达式":"(测试评估名1$1(匹配用结果项名1))","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }

        # 新增评估项
        cls.evaluateItemId_one_id = add_func.add_evaluate_ci(evaluate_one_data)  # 常规
        cls.evaluateItemId_two_id = add_func.add_evaluate_ci(evaluate_two_data)  # 用户组可用

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

        cls.url = '%s/api/rule/validate/matchExpression' % ci_url
        cls.session = requests.session()

    # 常规评估项在评估项表达式中使用
    def test_add_evaluate_expression_have_evaluate_conventional(cls):
        params = {
            'expression': '(测试评估名1$1(匹配用结果项名1))',
            'type': 'library'
        }
        case_name = '常规评估项在评估项表达式中使用'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        else:
            print('what fuck')

    # 用户组可用评估项在评估项表达式中使用
    def test_add_evaluate_expression_have_evaluate_solution_group_available(cls):
        params = {
            'expression': '(测试评估名2$1(匹配用结果项名1))',
            'type': 'library'
        }
        case_name = '用户组可用评估项在评估项表达式中使用'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        else:
            print('what fuck')

    # 验证中文
    def test_add_solution_group_specific_calculation_expression_chinese(cls):
        params = {
            'expression': '职业$1（休养或退休）',
            'type': 'solution_calcu_condition'
        }
        case_name = '验证中文'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用直接变量（常规） pass
    def test_add_food_label_library_expression_not_in_direct_variable_conventional(cls):
        params = {
            'expression': '(身高>60)&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用直接变量（常规）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用直接变量（方案组可用） pass
    def test_add_food_label_library_expression_not_in_direct_variable_solution_group_available(cls):
        params = {
            'expression': '(职业$1(休养或退休))&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用直接变量（方案组可用）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用计算变量（常规）pass
    def test_add_food_label_library_expression_not_in_calculation_variable_conventional(cls):
        params = {
            'expression': '(计算变量一>50)&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用计算变量（常规）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用计算变量（方案组可用） pass
    def test_add_food_label_library_expression_not_in_calculation_variable_solution_group_available(cls):
        params = {
            'expression': '(计算变量二>50)&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用计算变量（方案组可用）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用计算变量（方案组专用） pass
    def test_add_food_label_library_expression_not_in_calculation_variable_solution_group_specific(cls):
        params = {
            'expression': '(方案组专用计算变量>50)&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用计算变量（方案组专用）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用量表变量（常规）pass
    def test_add_food_label_library_expression_not_in_scale_variable_conventional(cls):
        params = {
            'expression': '(量表变量一>50)&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用量表变量（常规）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用量表变量（方案组可用） pass
    def test_add_food_label_library_expression_not_in_scale_variable_solution_group_available(cls):
        params = {
            'expression': '(量表变量二>50)&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用量表变量（方案组可用）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用评估项（常规） pass
    def test_add_food_label_library_expression_not_in_evaluate_conventional(cls):
        params = {
            'expression': '(测试评估名1=匹配用结果项名1)&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用评估项（常规）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用评估项（方案组可用）pass
    def test_add_food_label_library_expression_not_in_evaluate_solution_group_available(cls):
        params = {
            'expression': '(测试评估名2=匹配用结果项名1)&(状态=固态)',
            'type': 'food_material '
        }
        case_name = '在食材标签的定量标准中不能使用评估项（方案组可用）'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用this pass
    def test_add_food_label_library_expression_not_in_this(cls):
        params = {
            'expression': '(this$1(匹配用结果项名1))&(状态=固态)',
            'type': 'food_material'
        }
        case_name = '在食材标签的定量标准中不能使用this'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用* pass
    def test_add_food_label_library_expression_not_in_star(cls):
        params = {
            'expression': '*',
            'type': 'food_material'
        }
        case_name = '在食材标签的定量标准中不能使用*'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用方案组可用直接变量-题目  pass
    def test_add_solution_group_specific_calculation_expression_have_scheme_available_group_variable(cls):
        params = {
            'expression': '职业$1(休养或退休)',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用方案组可用直接变量-题目'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        else:
            print('what fuck')

    # 测试方案组专用计算变量适用条件中不可以使用常规直接变量-题目
    def test_add_solution_group_specific_calculation_expression_have_conventional_variable(cls):
        params = {
            'expression': '身高>90',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中不可以使用常规直接变量-题目'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用方案组可用计算变量  pass
    def test_add_solution_group_specific_calculation_expression_have_scheme_available_group_calculation(cls):
        params = {
            'expression': '计算变量二>50',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用方案组可用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        else:
            print('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用方案组专用计算变量 pass
    def test_add_solution_group_specific_calculation_expression_have_solution_group_calculation(cls):
        params = {
            'expression': '方案组专用计算变量>60',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用方案组可用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        else:
            print('what fuck')

    # 测试方案组专用计算变量适用条件中不可以使用常规计算变量
    def test_add_solution_group_specific_calculation_expression_have_conventional_calculation(cls):
        params = {
            'expression': '计算变量一>70',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中不可以使用常规计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用方案组可用量表变量
    def test_add_solution_group_specific_calculation_expression_have_scheme_available_group_scaleVariable(cls):
        params = {
            'expression': '量表变量二>60',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用方案组可用量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中不可以使用常规量表变量
    def test_add_solution_group_specific_calculation_expression_have_conventional_scaleVariable(cls):
        params = {
            'expression': '量表变量一>60',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中不可以使用常规量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中不可以使用常规评估项
    def test_add_solution_group_specific_calculation_expression_have_conventional_evaluate(cls):
        params = {
            'expression': '测试评估名1=匹配用结果项名1',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中不可以使用常规评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用方案组可用评估项 pass
    def test_add_solution_group_specific_calculation_expression_have_scheme_available_group_evaluate(cls):
        params = {
            'expression': '测试评估名2=匹配用结果项名1',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用方案组可用评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用* pass
    def test_add_solution_group_specific_calculation_expression_have_star(cls):
        params = {
            'expression': '*',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用*'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中不可以使用this  pass
    def test_add_solution_group_specific_calculation_expression_have_this(cls):
        params = {
            'expression': 'this$1(匹配用结果项1)',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中不可以使用this'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中不可以使用食材属性营养素  pass
    def test_add_solution_group_specific_calculation_expression_have_food_nutrients(cls):
        params = {
            'expression': '(GI值=10)&(状态=固态)',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中不可以使用食材属性营养素'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用=,!=,>,>=,<,<=,=n,$n,$$n pass
    def test_add_solution_group_specific_calculation_expression_have_simple(cls):
        params = {
            'expression': '$$1((职业$1(休养或退休,专业技术人员)),(计算变量二<=30),(职业=1(行政办公人员,专业技术人员)),(量表变量二>=40),(测试评估名2!=匹配用结果项名1))',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用='
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用$0,!$n,!$,$$-n  pass
    def test_add_solution_group_specific_calculation_expression_have_simple_two(cls):
        params = {
            'expression': '$$-1((职业$0(休养或退休,专业技术人员)),(职业!$(休养或退休,专业技术人员)),(职业!$1(行政办公人员,专业技术人员)),(量表变量二>=40),(测试评估名2!=匹配用结果项名1))',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用$0'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用==n,&,|,!
    def test_add_solution_group_specific_calculation_expression_have_simple_three(cls):
        params = {
            'expression': '==1((职业$0(休养或退休,专业技术人员))|(计算变量二<=30),(职业!$(休养或退休,专业技术人员))&(计算变量二<=30),(职业!$1(行政办公人员,专业技术人员)),(量表变量二>=40),!(测试评估名2!=匹配用结果项名1))',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用==n'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用计算变量适用条件中可以使用==n
    def test_add_solution_group_specific_calculation_expression_have_simple_scale(cls):
        params = {
            'expression': '==1(职业$0(休养或退休,专业技术人员)|(计算变量二<=30),(职业!$(休养或退休,专业技术人员))&(计算变量二<=30),(职业!$1(行政办公人员,专业技术人员)),(量表变量二>=40),!(测试评估名2!=匹配用结果项名1))',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试方案组专用计算变量适用条件中可以使用==n'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试变量值不在变量的取值范围中  pass
    def test_add_solution_group_specific_calculation_expression_value_not_in_value_range(cls):
        params = {
            'expression': '职业$1(停职)',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试变量值不在变量的取值范围中'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试后端对中文的校验
    def test_add_solution_group_specific_calculation_expression_confirm_chinese(cls):
        params = {
            'expression': '职业$1（休养或退休）',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试后端对中文的校验'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试$后面的阿拉伯数字大于括号中的个数  pass
    def test_add_solution_group_specific_calculation_expression_behind_math_bigger_than_value_(cls):
        params = {
            'expression': '职业$2(休养或退休)',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试$后面的阿拉伯数字大于括号中的个数'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试评估名的匹配结果项中存在没有的匹配结果项名
    def test_add_solution_group_specific_calculation_expression_evaluate_not_have_result_item_name(cls):
        params = {
            'expression': '测试评估项2!=匹配用结果项名3',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试评估名的匹配结果项中存在没有的匹配结果项名'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 变量和取值范围之间不能用$$ pass
    def test_add_solution_group_specific_calculation_expression_variable_not_have(cls):
        params = {
            'expression': '职业$$1(休养或退休)',
            'type': 'solution_calcu_condition'
        }
        case_name = '变量和取值范围之间不能用$$'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 评估项和匹配用结果项名不能用$$  pass
    def test_add_solution_group_specific_calculation_expression_evaluate_not_have(cls):
        params = {
            'expression': '测试评估项$$1(匹配用结果项名3)',
            'type': 'solution_calcu_condition'
        }
        case_name = '变量和取值范围之间不能用$$'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试表达式括号不对应  pass
    def test_add_solution_group_specific_calculation_expression_parentheses_not_match(cls):
        params = {
            'expression': '(职业$1(休养或退休)',
            'type': 'solution_calcu_condition'
        }
        case_name = '测试表达式括号不对应'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中可以使用方案组可用直接变量-题目
    def test_add_solution_group_specific_scaleVariable_expression_have_scheme_available_group_variable(cls):
        params = {
            'expression': '(职业$1(休养或退休))',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中可以使用方案组可用直接变量-题目'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中不可以使用常规直接变量-题目
    def test_add_solution_group_specific_scaleVariable_expression_have_conventional_variable(cls):
        params = {
            'expression': '(身高>90)',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中不可以使用常规直接变量-题目'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中可以使用方案组可用计算变量 pass
    def test_add_solution_group_specific_scaleVariable_expression_have_scheme_available_group_calculation(cls):
        params = {
            'expression': '(计算变量二>50)',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中可以使用方案组可用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中可以使用方案组专用计算变量  pass
    def test_add_solution_group_specific_scaleVariable_expression_have_solution_group_calculation(cls):
        params = {
            'expression': '(方案组专用计算变量>50)',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中可以使用方案组可用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示适用条件中不可以使用常规计算变量
    def test_add_solution_group_specific_scaleVariable_expression_have_conventional_calculation(cls):
        params = {
            'expression': '(计算变量一>70)',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示适用条件中不可以使用常规计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中可以使用方案组可用量表变量  pass
    def test_add_solution_group_specific_scaleVariable_expression_have_scheme_available_group_scaleVariable(cls):
        params = {
            'expression': '(量表变量二>60)',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中可以使用方案组可用量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中不可以使用常规量表变量
    def test_add_solution_group_specific_scaleVariable_expression_have_conventional_scaleVariable(cls):
        params = {
            'expression': '(量表变量一>60)',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中不可以使用常规量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中不可以使用常规评估项
    def test_add_solution_group_specific_scaleVariable_expression_have_conventional_evaluate(cls):
        params = {
            'expression': '(测试评估名1=匹配用结果项名1)',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中不可以使用常规评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中中可以使用方案组可用评估项   pass
    def test_add_solution_group_specific_scaleVariable_expression_have_scheme_available_group_evaluate(cls):
        params = {
            'expression': '(测试评估名2=匹配用结果项名1)',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中中可以使用方案组可用评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 测试方案组专用显示变量适用条件中中可以使用*  pass
    def test_add_solution_group_specific_scaleVariable_expression_have_star(cls):
        params = {
            'expression': '*',
            'type': 'solution_display_condition'
        }
        case_name = '测试方案组专用显示变量适用条件中中可以使用*'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中不能使用常规直接变量
    def test_add_solution_composition_not_direct_variable_conventional(cls):
        params = {
            'expression': '身高>70',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中不能使用常规直接变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中可以使用方案组可用直接变量 pass
    def test_add_solution_composition_have_direct_variable_scheme_available_group(cls):
        params = {
            'expression': '职业$1(休养或退休)',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中可以使用方案组可用直接变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中不能使用常规计算变量
    def test_add_solution_composition_not_calculation_variable_conventional(cls):
        params = {
            'expression': '计算变量一>70',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中不能使用常规计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中可以使用方案组可用计算变量 pass
    def test_add_solution_composition_calculation_variable_scheme_available_group(cls):
        params = {
            'expression': '计算变量二>70',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中可以使用方案组可用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中可以使用方案组专用计算变量
    def test_add_solution_composition_calculation_variable_scheme_available_group_calculation(cls):
        params = {
            'expression': '方案组专用计算变量>70',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中可以使用方案组可用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中不可以使用常规量表变量
    def test_add_solution_composition_scale_variable_conventional(cls):
        params = {
            'expression': '量表变量一>70',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中不可以使用常规量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中可以使用方案组可用量表变量 pass
    def test_add_solution_composition_scale_variable_scheme_available_group(cls):
        params = {
            'expression': '量表变量二>70',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中可以使用方案组可用量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中不可以使用常规评估项
    def test_add_solution_composition_evaluate_conventional(cls):
        params = {
            'expression': '测试评估名1=匹配用结果项名1',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中不可以使用常规评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中可以使用方案组可用评估项 pass
    def test_add_solution_composition_evaluate_scheme_available_group(cls):
        params = {
            'expression': '测试评估名2=匹配用结果项名1',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中可以使用方案组可用评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中不能使用this=
    def test_add_solution_composition_not_have_this(cls):
        params = {
            'expression': 'this=匹配用结果项名1',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中不能使用this='
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中不能使用食材属性营养表
    def test_add_solution_composition_have_food_nutrients(cls):
        params = {
            'expression': '(GI值=10)&(状态=固态)',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中不能使用食材属性营养表'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成显示条件中可以使用*
    def test_add_solution_composition_have_star(cls):
        params = {
            'expression': '*',
            'type': 'solution_composition_display_condition'
        }
        case_name = '方案组成显示条件中可以使用*'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中不能使用常规直接变量-题目
    def test_add_solution_composition_expression_not_have_direct_variable_conventional(cls):
        params = {
            'expression': '身高>70',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中不能使用常规直接变量-题目'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中可以使用方案组可用直接变量-题目
    def test_add_solution_composition_expression_have_direct_variable_scheme_available_group(cls):
        params = {
            'expression': '职业$1(休养或退休)',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中可以使用方案组可用直接变量-题目'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中不可以使用常规计算变量
    def test_add_solution_composition_expression_have_calculation_variable_conventional(cls):
        params = {
            'expression': '计算变量一>50',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中不可以使用常规计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中可以使用方案组可用计算变量
    def test_add_solution_composition_expression_have_calculation_variable_scheme_available_group(cls):
        params = {
            'expression': '计算变量二>50',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中可以使用方案组计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中可以使用方案组专用计算变量
    def test_add_solution_composition_expression_have_calculation_variable_specific_available_group(cls):
        params = {
            'expression': '方案组专用计算变量>50',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中可以使用方案组专用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中不可以使用1+1
    def test_add_solution_composition_expression_have_calculation_variable_specific_available_group11(cls):
        params = {
            'expression': '1+1',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中不可以使用1+1'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中不能使用常规量表变量
    def test_add_solution_composition_expression_not_have_scale_variable_conventional(cls):
        params = {
            'expression': '量表变量一>60',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中不能使用常规量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中能使用方案组量表变量
    def test_add_solution_composition_expression_have_scale_variable_scheme_available_group(cls):
        params = {
            'expression': '量表变量二>60',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中能使用方案组量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中能使用方案组评估项
    def test_add_solution_composition_expression_have_evaluate_scheme_available_group(cls):
        params = {
            'expression': '测试评估名2=匹配用结果项名1',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中能使用方案组评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中不能使用常规评估项
    def test_add_solution_composition_expression_not_have_evaluate_conventional(cls):
        params = {
            'expression': '测试评估名1=匹配用结果项名1',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中不能使用常规评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中不能使用this
    def test_add_solution_composition_expression_not_have_this(cls):
        params = {
            'expression': 'this=匹配用结果项名1',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中不能使用this'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中不能使用食材属性营养素
    def test_add_solution_composition_expression_not_have_food_nutrients(cls):
        params = {
            'expression': '(GI值=10)&(状态=固态)',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中不能使用食材属性营养素'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案组成方案结果适用条件中不能使用*
    def test_add_solution_composition_expression_not_have_star(cls):
        params = {
            'expression': '*',
            'type': 'solution_composition_result_condition'
        }
        case_name = '方案组成方案结果适用条件中不能使用*'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')
    '''
    # 方案评定显示条件中不能使用常规直接变量
    def test_add_scheme_evaluation_not_direct_variable_conventional(cls):
        params = {
            'expression': '身高>70',
            'type': ' solution_assess_condition'
        }
        case_name = '方案评定显示条件中不能使用常规直接变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')
    '''
    # 方案评定显示条件中可以使用方案组可用直接变量 pass
    def test_add_scheme_evaluation_have_direct_variable_scheme_available_group(cls):
        params = {
            'expression': '职业$1(休养或退休)',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中可以使用方案组可用直接变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中不能使用常规计算变量
    def test_add_scheme_evaluation_not_calculation_variable_conventional(cls):
        params = {
            'expression': '计算变量一>70',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中不能使用常规计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中可以使用方案组可用计算变量 pass
    def test_add_scheme_evaluation_calculation_variable_scheme_available_group(cls):
        params = {
            'expression': '计算变量二>70',
            'type': 'solution_assess_condition'
        }
        case_name = '方案组成显示条件中可以使用方案组可用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中可以使用方案组专用计算变量
    def test_add_scheme_evaluation_calculation_variable_scheme_available_group_calculation(cls):
        params = {
            'expression': '方案组专用计算变量>70',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中可以使用方案组专用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中不可以使用常规量表变量
    def test_add_scheme_evaluation_scale_variable_conventional(cls):
        params = {
            'expression': '量表变量一>70',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中不可以使用常规量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中可以使用方案组可用量表变量 pass
    def test_add_scheme_evaluation_scale_variable_scheme_available_group(cls):
        params = {
            'expression': '量表变量二>70',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中可以使用方案组可用量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中不可以使用常规评估项
    def test_add_scheme_evaluation_evaluate_conventional(cls):
        params = {
            'expression': '测试评估名1=匹配用结果项名1',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中不可以使用常规评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中可以使用方案组可用评估项 pass
    def test_add_scheme_evaluation_evaluate_scheme_available_group(cls):
        params = {
            'expression': '测试评估名2=匹配用结果项名1',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中可以使用方案组可用评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中不能使用this=
    def test_add_scheme_evaluation_not_have_this(cls):
        params = {
            'expression': 'this=匹配用结果项名1',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中不能使用this='
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中不能使用食材属性营养表
    def test_add_scheme_evaluation_have_food_nutrients(cls):
        params = {
            'expression': '(GI值=10)&(状态=固态)',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中不能使用食材属性营养表'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定显示条件中可以使用*
    def test_add_scheme_evaluation_have_star(cls):
        params = {
            'expression': '*',
            'type': 'solution_assess_condition'
        }
        case_name = '方案评定显示条件中可以使用*'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中不能使用常规直接变量-题目
    def test_add_scheme_evaluation_expression_not_have_direct_variable_conventional(cls):
        params = {
            'expression': '身高>70',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中不能使用常规直接变量-题目'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中可以使用方案组可用直接变量-题目
    def test_add_scheme_evaluation_expression_have_direct_variable_scheme_available_group(cls):
        params = {
            'expression': '职业$1(休养或退休)',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中可以使用方案组可用直接变量-题目'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中不可以使用常规计算变量
    def test_add_scheme_evaluation_expression_have_calculation_variable_conventional(cls):
        params = {
            'expression': '计算变量一>50',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中不可以使用常规计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中可以使用方案组可用计算变量
    def test_add_scheme_evaluation_expression_have_calculation_variable_scheme_available_group(cls):
        params = {
            'expression': '计算变量二>50',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中可以使用方案组可用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中可以使用方案组专用计算变量
    def test_add_scheme_evaluation_expression_have_calculation_variable_specific_available_group(cls):
        params = {
            'expression': '方案组专用计算变量>50',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中可以使用方案组专用计算变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中不能使用常规量表变量
    def test_add_scheme_evaluation_expression_not_have_scale_variable_conventional(cls):
        params = {
            'expression': '量表变量一>60',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中不能使用常规量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中能使用方案组量表变量
    def test_add_scheme_evaluation_expression_have_scale_variable_scheme_available_group(cls):
        params = {
            'expression': '量表变量二>60',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中能使用方案组量表变量'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中能使用方案组评估项
    def test_add_scheme_evaluation_expression_have_evaluate_scheme_available_group(cls):
        params = {
            'expression': '测试评估名2=匹配用结果项名1',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中能使用方案组评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中不能使用常规评估项
    def test_add_scheme_evaluation_expression_not_have_evaluate_conventional(cls):
        params = {
            'expression': '测试评估名1=匹配用结果项名1',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中不能使用常规评估项'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中不能使用this
    def test_add_scheme_evaluation_expression_not_have_this(cls):
        params = {
            'expression': 'this=匹配用结果项名1',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中不能使用this'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中不能使用食材属性营养素
    def test_add_scheme_evaluation_expression_not_have_food_nutrients(cls):
        params = {
            'expression': '(GI值=10)&(状态=固态)',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中不能使用食材属性营养素'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 方案评定方案结果适用条件中不能使用*
    def test_add_scheme_evaluation_expression_not_have_star(cls):
        params = {
            'expression': '*',
            'type': 'solution_assess_result_condition'
        }
        case_name = '方案评定方案结果适用条件中不能使用*'
        response = cls.session.get(url=cls.url, params=params)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()
