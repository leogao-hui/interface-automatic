# author:LEO GAO
# project Encoding:UTF-8

import unittest
import requests
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData
from Common.config import ci_url, add_combo_url_ci
from Common.operateDatabaseData import delete_database_data_test_ci
from Common.operateDatabaseData import add_database_data_ci
from Common.config import println


class TestAddCombo(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        add_func = AddFunction()
        cls.session = requests.session()

        # 新增直接变量
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

        # 新增计算变量
        calculation_variable_one_data = {
            'name': '计算变量二',
            'optionalValues[0][matchExpression]': '职业$1(休养或退休)',
            'optionalValues[0][content]': '身高+20',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.response_calculation_one_id = add_func.add_calculation_variable_ci(calculation_variable_one_data)

        # 新增信息结构
        add_func.add_information_structure_ci(CoreVersionData.information_structure_one_data)
        add_func.add_information_structure_ci(CoreVersionData.information_structure_two_data)

        cls.session = requests.session()

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
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }

        # 新增评估项
        cls.evaluateItemId_one = add_func.add_evaluate_ci(evaluate_one_data)

        evaluate_version_one_data = {
            'name': '测试版本',
            'items[0][itemId]': cls.response_height_id,
            'items[0][itemType]': 'direct_variable',
            'items[1][itemId]': cls.response_job_id,
            'items[1][itemType]': 'direct_variable',
            'items[2][itemId]': cls.response_calculation_one_id,
            'items[2][itemType]': 'calcu_variable',
            'items[3][itemId]': cls.evaluateItemId_one,
            'items[3][itemType]': 'evaluate_item',
        }

        # 新增评估版本
        cls.evVersionId_one = add_func.add_evaluate_version_ci(evaluate_version_one_data)

        # 获取评估版本中实体项
        get_url = '%s/api/rule/evlVersions/%s' % (ci_url, cls.evVersionId_one)
        response_evaluate_version_real_item_one = cls.session.get(url=get_url)
        evaluate_item_data = []
        direct_variable_data = []
        calculation_variable_data = []
        for key in (response_evaluate_version_real_item_one.json()['items']):
            if key['itemType'] == 'evaluate_item':
                evaluate_item_data.append(key['itemId'])
            elif key['itemType'] == 'direct_variable':
                direct_variable_data.append(key['itemId'])
            elif key['itemType'] == 'calcu_variable':
                calculation_variable_data.append(key['itemId'])

        cls.realItem_one = direct_variable_data[0]
        cls.realItem_two = direct_variable_data[1]
        cls.realItem_three = calculation_variable_data[0]
        cls.realItem_four = evaluate_item_data[0]

    # nhy-2127 新增一条套餐，正常保存，调获取套餐接口，对比数据。
    def test_normal_combo_create01(cls):
        body = {
            'name': '测试答题套餐名',
            'evId': cls.evVersionId_one,
            'items[0][itemId]': cls.realItem_one,
            'items[0][itemType]': 'direct_variable',
            'items[1][itemId]': cls.realItem_two,
            'items[1][itemType]': 'direct_variable',
            'items[2][itemId]': cls.realItem_three,
            'items[2][itemType]': 'calcu_variable',
            'items[3][itemId]': cls.realItem_four,
            'items[3][itemType]': 'evaluate_item',
        }
        case_name = '新增一条套餐，正常保存，调获取套餐接口，对比数据'
        print(body)
        response = cls.session.post(url=add_combo_url_ci, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            println('what fuck')

    # nhy-2121 新增套餐，当套餐名没有填时，报错套餐名应必填。
    def test_abnormal_combo_create01(cls):
        body = {
            'name': '',
            'evId': cls.evVersionId_one,
            'items[0][itemId]': cls.realItem_one,
            'items[0][itemType]': 'direct_variable'
        }
        case_name = '新增套餐，当套餐名没有填时，报错套餐名应必填'
        response = cls.session.post(url=add_combo_url_ci, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    # nhy-2122 新增套餐，当评估版本id没有填时，报错评估版本id应必填。
    def test_abnormal_combo_create02(cls):
        body = {
            'name': '测试套餐名2',
            'evId': '',
            'items[0][itemId]': cls.realItem_one,
            'items[0][itemType]': 'evaluate_item'
        }
        case_name = '新增套餐，当评估版本id没有填时，报错评估版本id应必填'
        response = cls.session.post(url=add_combo_url_ci, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2400 新增套餐，当ItemId（变量id）不存在于所属的evId时，应报错变量不存在。
    def test_abnormal_combo_create03(cls):
        body = {
            'name': '测试套餐名4',
            'evId': cls.evVersionId_one,
            'items[0][itemId]': int(cls.realItem_one) - 2,
            'items[0][itemType]': 'direct_variable'
        }
        case_name = '新增套餐，当ItemId（变量id）不存在于所属的evId时，应报错变量不存在'
        response = cls.session.post(url=add_combo_url_ci, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2401 新增套餐，当ItemId（评估项id）不存在于所属的evId时，应报错变量不存在。
    def test_abnormal_combo_create04(cls):
        body = {
            'name': '测试套餐名4',
            'evId': cls.evVersionId_one,
            'items[0][itemId]': int(cls.realItem_four) - 1,
            'items[0][itemType]': 'evaluate_item'
        }
        case_name = '新增套餐，当ItemId（评估项id）不存在于所属的evId时，应报错变量不存在'
        response = cls.session.post(url=add_combo_url_ci, data=body)
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
