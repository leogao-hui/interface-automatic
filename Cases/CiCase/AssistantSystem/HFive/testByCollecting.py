# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import ci_url, println
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData


class TestByCollecting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        add_func = AddFunction()
        cls.url = '%s/api/collection/patient' % ci_url
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

        search_data = {
            "variableName": "测试搜索选择题键值对",
            "variableValueType": "key_value",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试搜索选择题键值对型？",
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[rank]": "80",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "search_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        cls.response_search_id = add_func.add_direct_variable_with_problem_ci(search_data)

        # 查看直接变量对应的id
        search_height_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_height_id)
        response_height_id = add_func.get_survey_item(url=search_height_url)
        search_job_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_job_id)
        response_job_id = add_func.get_survey_item(url=search_job_url)
        search_search_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_search_id)
        response_search_id = add_func.get_survey_item(url=search_search_url)

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

        data_search = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '测试搜索选择题键值对型？',
            'groups[0][material][type]': '',
            'groups[0][material][url]': ''
        }
        search_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_search_id)
        add_func.modify_survey_item(url=search_url, data=data_search)

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

        # 新增显示变量
        display_variable_one_data = {
            'name': '测试显示变量',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '身高>70',
            'optionalValues[0][content]': 'hhh',
            'optionalValues[0][priority]': '10',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.response_display_one_id = add_func.add_display_variable_ci(display_variable_one_data)

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
            'isSolutionCanUse': 'yes',
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
        cls.evaluateItemId_one_id = add_func.add_evaluate_ci(evaluate_one_data)
        cls.evaluateItemId_two_id = add_func.add_evaluate_ci(evaluate_two_data)

        # 新增评估版本
        evaluate_version_one_data = {
            'name': '测试版本',
            'items[0][itemId]': cls.response_height_id,
            'items[0][itemType]': 'direct_variable',
            'items[1][itemId]': cls.response_job_id,
            'items[1][itemType]': 'direct_variable',
            'items[2][itemId]': cls.response_search_id,
            'items[2][itemType]': 'direct_variable',
            'items[3][itemId]': cls.response_calculation_one_id,
            'items[3][itemType]': 'calcu_variable',
            'items[4][itemId]': cls.response_display_one_id,
            'items[4][itemType]': 'display_variable',
            'items[5][itemId]': cls.evaluateItemId_one_id,
            'items[5][itemType]': 'evaluate_item',
            'items[6][itemId]': cls.evaluateItemId_two_id,
            'items[6][itemType]': 'evaluate_item',
        }

        cls.evVersionId_one = add_func.add_evaluate_version_ci(evaluate_version_one_data)

        # 新增套餐
        # 获取评估版本中实体项
        get_url = '%s/api/rule/evlVersions/%s' % (ci_url, cls.evVersionId_one)
        response_evaluate_version_real_item_one = cls.session.get(url=get_url)
        evaluate_item_data = []
        direct_variable_data = []
        calculation_variable_data = []
        display_variable_data = []
        for key in (response_evaluate_version_real_item_one.json()['items']):
            if key['itemType'] == 'evaluate_item':
                evaluate_item_data.append(key['itemId'])
            elif key['itemType'] == 'direct_variable':
                direct_variable_data.append(key['itemId'])
            elif key['itemType'] == 'display_variable':
                display_variable_data.append(key['itemId'])
            elif key['itemType'] == 'calcu_variable':
                calculation_variable_data.append(key['itemId'])
            else:
                print('有问题')
        cls.realItem_one = direct_variable_data[0]
        cls.realItem_two = direct_variable_data[1]
        cls.realItem_seven = direct_variable_data[4]
        cls.realItem_three = calculation_variable_data[0]
        cls.realItem_four = evaluate_item_data[0]
        cls.realItem_five = evaluate_item_data[1]
        cls.realItem_six = display_variable_data[0]

        combo_one = {
            'name': '测试答题套餐名',
            'evId': cls.evVersionId_one,
            'items[0][itemId]': cls.realItem_one,
            'items[0][itemType]': 'direct_variable',
            'items[1][itemId]': cls.realItem_two,
            'items[1][itemType]': 'direct_variable',
            'items[2][itemId]': cls.realItem_three,
            'items[2][itemType]': 'calcu_variable',
            'items[3][itemId]': cls.realItem_six,
            'items[3][itemType]': 'display_variable',
            'items[4][itemId]': cls.realItem_four,
            'items[4][itemType]': 'evaluate_item',
            'items[5][itemId]': cls.realItem_five,
            'items[5][itemType]': 'evaluate_item',
            'items[6][itemId]': cls.realItem_seven,
            'items[6][itemType]': 'direct_variable',

        }
        cls.comboId_one = add_func.add_combo_ci(combo_one)

        # 新增团队
        team_data_one = {
            'name': '测试团队'
        }

        cls.teamId_one = add_func.add_team_ci(team_data_one)

        # 新增成员
        team_member_data_one = {
            'phone': '123456',
            'password': '123456',
            'name': '123456',
            'belongTeamId': cls.teamId_one,
            'identity': 'manager'
        }

        cls.clerkId_one = add_func.add_team_number_ci(team_member_data_one)

    # nhy-2227 新增一条正常数据，查看返回字段是否正确。
    def test_normal_collection_create01(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
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
        case_name = 'nhy-2227 新增一条正常数据，查看返回字段是否正确。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # nhy-2213 患者建档时，店员名id没填，查看是否报错。
    def test_abnormal_collection_create01(cls):
        body = {
            'clerkId': '',
            'comboId': cls.comboId_one,
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
        case_name = 'nhy-2213 患者建档时，店员名id没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2214 套餐id没填，查看是否报错。
    def test_abnormal_collection_create02(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': '',
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
        case_name = 'nhy-2214 套餐id没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2215 患者建档时，name（患者姓名）没填，查看是否报错。
    def test_abnormal_collection_create03(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': '',
            'phone': '13342423242',
            'sex': '男',
            'birthAt': '456',
            'representor': 'adadd',
            'nation': 'qdw',
            'address': 'dwdq',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        case_name = 'nhy-2215 患者建档时，name（患者姓名）没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2216 患者建档时，phone（患者手机号）没填，查看是否报错。
    def test_abnormal_collection_create04(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': 'aaa',
            'phone': '',
            'sex': '男',
            'birthAt': '456',
            'representor': 'adadd',
            'nation': 'qdw',
            'address': 'dwdq',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        case_name = 'nhy-2216 患者建档时，phone（患者手机号）没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2217 患者建档时，sex（性别）没填，查看是否报错。
    def test_abnormal_collection_create05(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': 'aaa',
            'phone': '',
            'sex': '',
            'birthAt': '456',
            'representor': 'adadd',
            'nation': 'qdw',
            'address': 'dwdq',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        case_name = 'nhy-2217 患者建档时，sex（性别）没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2218 患者建档时，birthAt（出生年月）没填，查看是否报错。
    def test_abnormal_collection_create06(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': 'aaa',
            'phone': '14323424324',
            'sex': '男',
            'birthAt': '',
            'representor': 'adadd',
            'nation': 'qdw',
            'address': 'dwdq',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        case_name = 'nhy-2218 患者建档时，birthAt（出生年月）没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2219 患者建档时，representor（陈述人）没填，查看是否报错。
    def test_abnormal_collection_create07(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': 'aaa',
            'phone': '14323424324',
            'sex': '男',
            'birthAt': '345',
            'representor': '',
            'nation': 'qdw',
            'address': 'dwdq',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        case_name = 'nhy-2219 患者建档时，representor（陈述人）没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2220 患者建档时，nation（民族）没填，查看是否报错。
    def test_abnormal_collection_create08(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': 'aaa',
            'phone': '14323424324',
            'sex': '男',
            'birthAt': '345',
            'representor': 'ddqd',
            'nation': '',
            'address': 'dwdq',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        case_name = 'nhy-2220 患者建档时，nation（民族）没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2221 患者建档时，address（常住地址）没填，查看是否报错。
    def test_abnormal_collection_create09(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': 'aaa',
            'phone': '14323424324',
            'sex': '男',
            'birthAt': '345',
            'representor': 'ddqd',
            'nation': 'eqw',
            'address': '',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        case_name = 'nhy-2221 患者建档时，address（常住地址）没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2222 患者建档时，caregiver（护理人）没填，查看是否报错。
    def test_abnormal_collection_create10(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': 'aaa',
            'phone': '14323424324',
            'sex': '男',
            'birthAt': '345',
            'representor': 'ddqd',
            'nation': 'eqw',
            'address': 'addw',
            'caregiver': '',
            'caregiverPhone': 'dwdqdwd'
        }
        case_name = 'nhy-2222 患者建档时，caregiver（护理人）没填，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2224 患者建档时，传入的clerkId不存在，查看是否报错。
    def test_abnormal_collection_create12(cls):
        body = {
            'clerkId': int(cls.clerkId_one) - 1,
            'comboId': cls.comboId_one,
            'name': 'aaa',
            'phone': '14323424324',
            'sex': '男',
            'birthAt': '345',
            'representor': 'ddqd',
            'nation': 'eqw',
            'address': 'addw',
            'caregiver': 'qewqe',
            'caregiverPhone': 'dadda'
        }
        case_name = 'nhy-2224 患者建档时，传入的clerkId不存在，查看是否报错。'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2225 患者建档时，comboId不存在，查看是否报错。
    def test_abnormal_collection_create13(cls):
        body = {
            'clerkId': cls.clerkId_one,
            'comboId': int(cls.comboId_one) - 1,
            'name': 'aaa',
            'phone': '14323424324',
            'sex': '男',
            'birthAt': '345',
            'representor': 'ddqd',
            'nation': 'eqw',
            'address': 'addw',
            'caregiver': 'qewqe',
            'caregiverPhone': 'asdad'
        }
        case_name = 'nhy-2225 患者建档时，comboId不存在，查看是否报错'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()




