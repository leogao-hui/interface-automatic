#_author:leo gao
#encoding:utf-8

import unittest
import requests
from Common.config import ci_url, println
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData


class TestAddFoodLabelLibrary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        add_func = AddFunction()
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
        cls.url = '%s/api/rule/foodMaterialTag' % ci_url
        cls.session = requests.session()

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
        cls.response_calculation_three_id = add_func.add_solution_group_solution_calculationVariable(calculation_variable_three_data)

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

    # 新增食材标签,标签名未填,报错标签必填
    def test_add_food_label_library_not_tags(cls):
        body = {
            'name': '',
            'category': '品质',
            'type': '定性',
            'presentation': '说明情况',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '新增食材标签,标签名未填,报错标签必填'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 新增食材标签,分类名未填,报错分类名必填
    def test_add_food_label_library_not_category(cls):
        body = {
            'name': '分类1',
            'category': '',
            'type': '定性',
            'presentation': '说明情况',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '新增食材标签,分类名未填,报错分类名必填'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 分类为空
    def test_add_food_label_library_not_type(cls):
        body = {
            'name': '分类2',
            'category': '品质',
            'type': '',
            'presentation': '说明情况',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '新增食材标签,标签类型未填,报错标签类型必填'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 情况为空
    def test_add_food_label_library_not_presentation(cls):
        body = {
            'name': '分类3',
            'category': '品质',
            'type': '定性',
            'presentation': '',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '新增食材标签,标签类型未填,报错标签类型必填'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 互斥组为空
    def test_add_food_label_library_not_exclusionGroup(cls):
        body = {
            'name': '分类4',
            'category': '品质',
            'type': '定性',
            'presentation': '情况说明',
            'exclusionGroup': '',
            'comment': '',
        }
        case_name = '新增食材标签,互斥组未填,报错标签类型必填'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 添加标签名重复
    def test_add_food_label_library_tag_repeat(cls):
        body_one = {
            'name': '分类5',
            'category': '品质',
            'type': '定性',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }

        body_two = {
            'name': '分类6',
            'category': '品质',
            'type': '定性',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '新增食材标签,添加标签名重复'
        cls.session.post(url=cls.url, data=body_one)
        response_two = cls.session.post(url=cls.url, data=body_two)
        if response_two.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response_two.status_code, response_two.json())
        elif response_two.status_code != 422:
            println(2, case_name)
            println(2, response_two.json())
            cls.assertEqual(422, response_two.status_code)
        else:
            println('what fuck')

    # 当标签类型为定量时, 定量标准字段为必填
    def test_add_food_label_library_tag_is_quantitative_rationStandard_is_must(cls):
        body = {
            'name': '标签7',
            'category': '品质',
            'type': '定量',
            'rationStandard': '',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '新增食材标签,当标签类型为定量时, 定量标准字段为必填'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 当标签类型为定性时，定量标准不传
    def test_add_food_label_library_tag_is_qualitative_rationStandard_is_not(cls):
        body = {
            'name': '标签8',
            'category': '品质',
            'type': '定性',
            'rationStandard': '',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '新增食材标签,当标签类型为定性时，定量标准不传'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中输入GI值>10
    def test_add_food_label_library_GI_big_in_rationStandard(cls):
        body = {
            'name': '标签9',
            'category': '品质',
            'type': '定量',
            'rationStandard': 'GI值>10',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '新增食材标签,当定量标准中输入GI值>10'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中输入GI值<10
    def test_add_food_label_library_GI_less_in_rationStandard(cls):
        body = {
            'name': '标签10',
            'category': '品质',
            'type': '定量',
            'rationStandard': 'GI值>10',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中输入GI值<10'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中输入GI值=10
    def test_add_food_label_library_GI_equal_in_rationStandard(cls):
        body = {
            'name': '标签11',
            'category': '品质',
            'type': 'quantitative',
            'rationStandard': 'GI值=10',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中输入GI值=10'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中输入GI值>=10
    def test_add_food_label_library_GI_bigEqual_in_rationStandard(cls):
        body = {
            'name': '标签12',
            'category': '品质',
            'type': 'quantitative',
            'rationStandard': 'GI值>=10',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中输入GI值>=10'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中输入GI值<=10
    def test_add_food_label_library_GI_lessEqual_in_rationStandard(cls):
        body = {
            'name': '标签13',
            'category': '品质',
            'type': 'quantitative',
            'rationStandard': 'GI值<=10',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中输入GI值<=10'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中输入GI值!=10
    def test_add_food_label_library_GI_notEqual_in_rationStandard(cls):
        body = {
            'name': '标签14',
            'category': '品质',
            'type': '定量',
            'rationStandard': 'GI值!=10',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中输入GI值!=10'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中输入GI值=10|状态=固态
    def test_add_food_label_library_or_in_rationStandard(cls):
        body = {
            'name': '标签15',
            'category': '品质',
            'type': '定量',
            'rationStandard': 'GI值=10|状态=固态',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中输入GI值=10|状态=固态'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中输入GI值=10&状态=固态
    def test_add_food_label_library_and_in_rationStandard(cls):
        body = {
            'name': '标签16',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(GI值=10)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中输入GI值=10&状态=固态'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # 当定量标准中输入((GI值>=10)&(状态=固态)|((可食部系数>10)|(颜色$1(白色))))
    def test_add_food_label_library_complex_expression_in_rationStandard(cls):
        body = {
            'name': '标签17',
            'category': '品质',
            'type': '定量',
            'rationStandard': '((GI值>=10)&(状态=固态)|((可食部系数>10)|(颜色$1(白色))))',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中输入((GI值>=10)&(状态=固态)|((可食部系数>10)|(颜色$1(白色))))'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中左边是不存在的【食材基础属性】【食材营养素】，报错变量不存在
    def test_add_food_label_library_basic_properties_of_ingredients_or_food_nutrient_not_exist_in_left(cls):
        body = {
            'name': '标签18',
            'category': '品质',
            'type': '定量',
            'rationStandard': '((GI值1>=10)&(状态=固态)|((可食部系数>10)|(颜色$1(白色)))',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中左边是不存在的【食材基础属性】【食材营养素】，报错变量不存在'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # 当定量标准中右边的值不在【食材基础属性】【食材营养素】的取值范围中，报错变量不在取值范围中
    def test_add_food_label_library_right_value_not_in_basic_properties_of_ingredients_or_food_nutrient_(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '((GI值1>=10)&(状态=固态)|((可食部系数>10)|(颜色$1(白色)))',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '当定量标准中右边的值不在【食材基础属性】【食材营养素】的取值范围中，报错变量不在取值范围中'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用直接变量（常规）
    def test_add_food_label_library_expression_not_in_direct_variable_conventional(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(身高>60)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用直接变量（常规）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用直接变量（方案组可用）
    def test_add_food_label_library_expression_not_in_direct_variable_solution_group_available(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(职业$1(休养或退休))&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用直接变量（方案组可用）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用计算变量（常规）
    def test_add_food_label_library_expression_not_in_calculation_variable_conventional(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(计算变量一>50)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用计算变量（常规）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用计算变量（方案组可用）
    def test_add_food_label_library_expression_not_in_calculation_variable_solution_group_available(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(计算变量二>50)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用计算变量（方案组可用）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用计算变量（方案组专用）
    def test_add_food_label_library_expression_not_in_calculation_variable_solution_group_specific(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(方案组专用计算变量>50)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用计算变量（方案组专用）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用量表变量（常规）
    def test_add_food_label_library_expression_not_in_scale_variable_conventional(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(量表变量一>50)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用量表变量（常规）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用量表变量（方案组可用）
    def test_add_food_label_library_expression_not_in_scale_variable_solution_group_available(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(量表变量二>50)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用量表变量（方案组可用）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用评估项（常规）
    def test_add_food_label_library_expression_not_in_evaluate_conventional(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(测试评估名1=匹配用结果项名1)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用评估项（常规）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用评估项（方案组可用）
    def test_add_food_label_library_expression_not_in_evaluate_solution_group_available(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(测试评估名2=匹配用结果项名1)&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用评估项（方案组可用）'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用this
    def test_add_food_label_library_expression_not_in_this(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '(this$1(匹配用结果项名1))&(状态=固态)',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用this'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 在食材标签的定量标准中不能使用*
    def test_add_food_label_library_expression_not_in_star(cls):
        body = {
            'name': '标签19',
            'category': '品质',
            'type': '定量',
            'rationStandard': '*',
            'presentation': '情况说明',
            'exclusionGroup': '1',
            'comment': '',
        }
        case_name = '在食材标签的定量标准中不能使用*'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()


