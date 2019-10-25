# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData
from Common.config import ci_url, println
from Common.operateDatabaseData import add_database_data_ci, delete_database_data_test_ci, delete_answer_question


class TestImportantCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        cls.add_func = AddFunction()
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
        cls.response_height_id = cls.add_func.add_direct_variable_with_problem_ci(height_data)

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
        cls.response_job_id = cls.add_func.add_direct_variable_with_problem_ci(job_data)

        tumor_data = {
            "variableName": "瘤种",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": "肺癌",
            "optionalValues[0][sort]": "1",
            "optionalValues[1][variableValue]": "大肠癌",
            "optionalValues[1][sort]": "2",
            "optionalValues[2][variableValue]": "乳腺癌",
            "optionalValues[2][sort]": "3",
            "optionalValues[3][variableValue]": "前列腺癌",
            "optionalValues[3][sort]": "4",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您得过什么瘤种？",
            "surveyItem[rank]": "80",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "multiple_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "comment",
            "surveyItem[options][0][surveyItemValue]": "肺癌",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "大肠癌",
            "surveyItem[options][1][sort]": "2",
            "surveyItem[options][2][surveyItemValue]": "乳腺癌",
            "surveyItem[options][2][sort]": "3",
            "surveyItem[options][3][surveyItemValue]": "前列腺癌",
            "surveyItem[options][3][sort]": "4",
            "surveyItem[preConditionItems][0][matchExp]": "(职业$1(休养或退休))",
            "surveyItem[preConditionItems][0][description]": "显示条件",
            "surveyItem[preConditionItems][0][comment]": "1111"
        }
        cls.response_tumor_id = cls.add_func.add_direct_variable_with_problem_ci(tumor_data)

        treatment_stage_data = {
            "variableName": "治疗阶段",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": "姑息治疗期间",
            "optionalValues[0][sort]": "1",
            "optionalValues[1][variableValue]": "围手术期术后",
            "optionalValues[1][sort]": "2",
            "optionalValues[2][variableValue]": "化疗期间",
            "optionalValues[2][sort]": "3",
            "optionalValues[3][variableValue]": "放疗期间",
            "optionalValues[3][sort]": "4",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您所处什么治疗阶段？",
            "surveyItem[rank]": "70",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "multiple_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "comment",
            "surveyItem[options][0][surveyItemValue]": "姑息治疗期间",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "围手术期术后",
            "surveyItem[options][1][sort]": "2",
            "surveyItem[options][2][surveyItemValue]": "乳腺癌",
            "surveyItem[options][2][sort]": "3",
            "surveyItem[options][3][surveyItemValue]": "前列腺癌",
            "surveyItem[options][3][sort]": "4",
            "surveyItem[preConditionItems][0][matchExp]": "(职业$1(专业技术人员))|(瘤种$1(肺癌,大肠癌))",
            "surveyItem[preConditionItems][0][description]": "显示条件",
            "surveyItem[preConditionItems][0][comment]": "1111",
        }
        cls.response_treatment_id = cls.add_func.add_direct_variable_with_problem_ci(treatment_stage_data)

        hobby_data = {
            "variableName": "兴趣爱好",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": 1,
            "optionalValues[0][sort]": "1",
            "optionalValues[1][variableValue]": 2,
            "optionalValues[1][sort]": "2",
            "optionalValues[2][variableValue]": 3,
            "optionalValues[2][sort]": "3",
            "optionalValues[3][variableValue]": 4,
            "optionalValues[3][sort]": "4",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的兴趣爱好是什么？",
            "surveyItem[rank]": "60",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "single_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "comment",
            "surveyItem[options][0][surveyItemValue]": "没有减少",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "略微减少参与次数",
            "surveyItem[options][1][sort]": "2",
            "surveyItem[options][2][surveyItemValue]": "明显减少",
            "surveyItem[options][2][sort]": "3",
            "surveyItem[options][3][surveyItemValue]": "基本不参与",
            "surveyItem[options][3][sort]": "4",
        }
        cls.response_hobby_id = cls.add_func.add_direct_variable_with_problem_ci(hobby_data)

        search_data = {
            "variableName": "测试搜索选择题键值对",
            "variableValueType": "key_value",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试搜索选择题键值对型？",
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[rank]": "50",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "search_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        cls.response_search_id = cls.add_func.add_direct_variable_with_problem_ci(search_data)

        latest_data = {
            "variableName": "最后一题",
            "variableValueType": "numerical",
            "optionalValueMin": 20,
            "optionalValueMax": 250,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "最后一题",
            "surveyItem[rank]": "40",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        cls.response_end_id = cls.add_func.add_direct_variable_with_problem_ci(latest_data)

        # 新增计算变量
        calculation_variable_one_data = {
            'name': '计算变量一',
            'optionalValues[0][matchExpression]': '职业$1(休养或退休)',
            'optionalValues[0][content]': '身高+20',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.response_calculation_one_id = cls.add_func.add_calculation_variable_ci(calculation_variable_one_data)

        calculation_variable_two_data = {
            'name': '计算变量二',
            'optionalValues[0][matchExpression]': '$$1((治疗阶段$1(姑息治疗期间,化疗期间)),瘤种$1(肺癌,大肠癌),(计算变量一>100))',
            'optionalValues[0][content]': '0',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': '111',
            'comment': '111',
            'isSolutionCanUse': 'yes'
        }
        cls.response_calculation_two_id = cls.add_func.add_calculation_variable_ci(calculation_variable_two_data)
        '''
        # 新增量表变量
        response_scale = cls.add_func.add_scale_variable(CoreData.scale_variable_one_data)
        self.response_scale_id = response_scale.json['scaleVariableId']
        '''
        # 新增信息结构
        cls.add_func.add_information_structure_ci(CoreVersionData.information_structure_one_data)
        cls.add_func.add_information_structure_ci(CoreVersionData.information_structure_two_data)

        # 新增根模板
        cls.rootTplId = cls.add_func.add_root_template_ci(CoreVersionData.root_template_data)

        evaluate_one_data = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '标签二',
            'rank': 1,
            'name': '测试评估名1',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"计算变量一>100","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(职业$1(休养或退休))","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }

        # 新增评估项
        cls.evaluateItemId_one_id = cls.add_func.add_evaluate_ci(evaluate_one_data)

        # 查看直接变量对应的id
        search_height_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_height_id)
        response_height_id = cls.add_func.get_survey_item(url=search_height_url)
        search_job_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_job_id)
        response_job_id = cls.add_func.get_survey_item(url=search_job_url)
        search_tumor_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_tumor_id)
        response_tumor_id = cls.add_func.get_survey_item(url=search_tumor_url)
        search_treatment_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_treatment_id)
        response_treatment_id = cls.add_func.get_survey_item(url=search_treatment_url)
        search_hobby_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_hobby_id)
        response_hobby_id = cls.add_func.get_survey_item(url=search_hobby_url)
        search_search_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_search_id)
        response_search_id = cls.add_func.get_survey_item(url=search_search_url)

        # 修改题目状态
        data_height = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '您的身高是多少',
            'groups[0][material][type]': '',
            'groups[0][material][url]': ''
        }
        height_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_height_id)
        cls.add_func.modify_survey_item(url=height_url, data=data_height)

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
        cls.add_func.modify_survey_item(url=job_url, data=data_job)

        data_tumor = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '您得过什么瘤种？',
            'groups[0][material][type]': '',
            'groups[0][material][url]': '',
            'groups[0][options][0][id]': '0',
            'groups[0][options][0][content]': '肺癌',
            'groups[0][options][0][sort]': '0',
            'groups[0][options][0][displayContent]': '',
            'groups[0][options][0][canSelectedComment]': 'yes',
            'groups[0][options][0][orderInGroup]': '1',
            'groups[0][options][1][id]': '1',
            'groups[0][options][1][content]': '大肠癌',
            'groups[0][options][1][sort]': '1',
            'groups[0][options][1][displayContent]': '',
            'groups[0][options][1][canSelectedComment]': 'yes',
            'groups[0][options][1][orderInGroup]': '1',
            'groups[0][options][2][id]': '1',
            'groups[0][options][2][content]': '乳腺癌',
            'groups[0][options][2][sort]': '2',
            'groups[0][options][2][displayContent]': '',
            'groups[0][options][2][canSelectedComment]': 'yes',
            'groups[0][options][2][orderInGroup]': '1',
            'groups[0][options][3][id]': '1',
            'groups[0][options][3][content]': '前列腺癌',
            'groups[0][options][3][sort]': '3',
            'groups[0][options][3][displayContent]': '',
            'groups[0][options][3][canSelectedComment]': 'yes',
            'groups[0][options][3][orderInGroup]': '1',
        }
        tumor_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_tumor_id)
        cls.add_func.modify_survey_item(url=tumor_url, data=data_tumor)

        data_treatment = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '您所处什么治疗阶段？',
            'groups[0][material][type]': '',
            'groups[0][material][url]': '',
            'groups[0][options][0][id]': '0',
            'groups[0][options][0][content]': '姑息治疗期间',
            'groups[0][options][0][sort]': '0',
            'groups[0][options][0][displayContent]': '',
            'groups[0][options][0][canSelectedComment]': 'yes',
            'groups[0][options][0][orderInGroup]': '1',
            'groups[0][options][1][id]': '1',
            'groups[0][options][1][content]': '围手术期',
            'groups[0][options][1][sort]': '1',
            'groups[0][options][1][displayContent]': '',
            'groups[0][options][1][canSelectedComment]': 'yes',
            'groups[0][options][1][orderInGroup]': '1',
            'groups[0][options][2][id]': '1',
            'groups[0][options][2][content]': '乳腺癌',
            'groups[0][options][2][sort]': '2',
            'groups[0][options][2][displayContent]': '',
            'groups[0][options][2][canSelectedComment]': 'yes',
            'groups[0][options][2][orderInGroup]': '1',
            'groups[0][options][3][id]': '1',
            'groups[0][options][3][content]': '前列腺癌',
            'groups[0][options][3][sort]': '3',
            'groups[0][options][3][displayContent]': '',
            'groups[0][options][3][canSelectedComment]': 'yes',
            'groups[0][options][3][orderInGroup]': '1',
        }
        treatment_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_treatment_id)
        cls.add_func.modify_survey_item(url=treatment_url, data=data_treatment)

        data_hobby = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '您的兴趣爱好是什么？',
            'groups[0][material][type]': '',
            'groups[0][material][url]': '',
            'groups[0][options][0][id]': '0',
            'groups[0][options][0][content]': '姑息治疗期间',
            'groups[0][options][0][sort]': '0',
            'groups[0][options][0][displayContent]': '',
            'groups[0][options][0][canSelectedComment]': 'yes',
            'groups[0][options][0][orderInGroup]': '1',
            'groups[0][options][1][id]': '1',
            'groups[0][options][1][content]': '围手术期',
            'groups[0][options][1][sort]': '1',
            'groups[0][options][1][displayContent]': '',
            'groups[0][options][1][canSelectedComment]': 'yes',
            'groups[0][options][1][orderInGroup]': '1',
            'groups[0][options][2][id]': '1',
            'groups[0][options][2][content]': '乳腺癌',
            'groups[0][options][2][sort]': '2',
            'groups[0][options][2][displayContent]': '',
            'groups[0][options][2][canSelectedComment]': 'yes',
            'groups[0][options][2][orderInGroup]': '1',
            'groups[0][options][3][id]': '1',
            'groups[0][options][3][content]': '前列腺癌',
            'groups[0][options][3][sort]': '3',
            'groups[0][options][3][displayContent]': '',
            'groups[0][options][3][canSelectedComment]': 'yes',
            'groups[0][options][3][orderInGroup]': '1',
        }
        hobby_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_hobby_id)
        cls.add_func.modify_survey_item(url=hobby_url, data=data_hobby)

        data_search = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '测试搜索选择题键值对型？',
            'groups[0][material][type]': '',
            'groups[0][material][url]': ''
        }
        search_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_search_id)
        cls.add_func.modify_survey_item(url=search_url, data=data_search)

        # 新增评估版本
        evaluate_version_one_data = {
            'name': '测试答题评估版本',
            'items[0][itemId]': cls.response_height_id,
            'items[0][itemType]': 'direct_variable',
            'items[1][itemId]': cls.response_job_id,
            'items[1][itemType]': 'direct_variable',
            'items[2][itemId]': cls.response_tumor_id,
            'items[2][itemType]': 'direct_variable',
            'items[3][itemId]': cls.response_treatment_id,
            'items[3][itemType]': 'direct_variable',
            'items[4][itemId]': cls.response_hobby_id,
            'items[4][itemType]': 'direct_variable',
            'items[5][itemId]': cls.response_calculation_one_id,
            'items[5][itemType]': 'calcu_variable',
            'items[6][itemId]': cls.response_calculation_two_id,
            'items[6][itemType]': 'calcu_variable',
            'items[7][itemId]': cls.evaluateItemId_one_id,
            'items[7][itemType]': 'evaluate_item',
            'items[8][itemId]': cls.response_search_id,
            'items[8][itemType]': 'direct_variable',
        }
        cls.evVersionId_one = cls.add_func.add_evaluate_version_ci(evaluate_version_one_data)

        # 新增套餐
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
            else:
                print('有问题')
        cls.realItem_one = direct_variable_data[0]
        cls.realItem_two = direct_variable_data[1]
        cls.realItem_three = direct_variable_data[2]
        cls.realItem_four = direct_variable_data[3]
        cls.realItem_five = direct_variable_data[4]
        cls.realItem_six = calculation_variable_data[0]
        cls.realItem_seven = calculation_variable_data[1]
        cls.realItem_eight = evaluate_item_data[0]
        cls.realItem_nine = direct_variable_data[5]

        combo_data = {
            'name': '测试答题套餐名',
            'evId': cls.evVersionId_one,
            'items[0][itemId]': cls.realItem_one,
            'items[0][itemType]': 'direct_variable',
            'items[1][itemId]': cls.realItem_two,
            'items[1][itemType]': 'direct_variable',
            'items[2][itemId]': cls.realItem_three,
            'items[2][itemType]': 'direct_variable',
            'items[3][itemId]': cls.realItem_four,
            'items[3][itemType]': 'direct_variable',
            'items[4][itemId]': cls.realItem_five,
            'items[4][itemType]': 'direct_variable',
            'items[5][itemId]': cls.realItem_six,
            'items[5][itemType]': 'calcu_variable',
            'items[6][itemId]': cls.realItem_seven,
            'items[6][itemType]': 'calcu_variable',
            'items[7][itemId]': cls.realItem_eight,
            'items[7][itemType]': 'evaluate_item',
            'items[8][itemId]': cls.realItem_nine,
            'items[8][itemType]': 'direct_variable',
        }

        cls.comboId_one = cls.add_func.add_combo_ci(combo_data)

        # 新增团队
        team_data = {
            'name': '测试团队'
        }
        cls.teamId_one = cls.add_func.add_team_ci(team_data)

        # 新增团队人员
        team_member_one_data = {
            'phone': '123456',
            'password': '123456',
            'name': '123456',
            'belongTeamId': cls.teamId_one,
            'identity': 'manager'
        }
        cls.clerkId_one = cls.add_func.add_team_number_ci(team_member_one_data)

    def setUp(cls):
        # 新增建档
        filling_data = {
            'clerkId': cls.clerkId_one,
            'comboId': cls.comboId_one,
            'name': '测试人',
            'phone': '123456',
            'sex': 'male',
            'birthAt': '456',
            'representor': 'adadd',
            'nation': 'qdw',
            'address': 'dwdq',
            'caregiver': 'dwq',
            'caregiverPhone': 'dwdqdwd'
        }
        cls.patientSurveyResultId_one = cls.add_func.add_filing_ci(filling_data)
        cls.url_get_prev = '%s/api/collection/patientSurveyResult/%s/prevSurveyItem' % (ci_url, cls.patientSurveyResultId_one)

        # 获取第一题
        cls.receive_next_question_url_ci = '%s/api/collection/patientSurveyResult/%s/nextSurveyItem' % (ci_url, cls.patientSurveyResultId_one)
        question_one = cls.session.get(url=cls.receive_next_question_url_ci)
        cls.survey_item_id_one = question_one.json()['surveyItemId']
        print(question_one.status_code, question_one.json())

    # nhy-2335 测试连续两次上一题
    def test_twice_on_a_topic_answer01(cls):

        # 答第一题
        submit_question_data_one = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': cls.survey_item_id_one,
            'blankContent': 110,
        }
        cls.patientSurveyResultItemId_one = cls.add_func.submit_question(submit_question_data_one)

        # 获取第二题
        receive_question_data_two = {
            'surveyItemId': cls.survey_item_id_one
        }
        question_two = cls.session.get(url=cls.receive_next_question_url_ci, params=receive_question_data_two)
        survey_item_id_two = question_two.json()['surveyItemId']
        print(question_two.status_code, question_two.json())
        cls.assertEqual('您的职业是？', question_two.json()['title'])

        # 提交第二题
        submit_question_data_two = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_two,
            'selectOptions[0][content]': '休养或退休',
        }
        cls.patientSurveyResultItemId_two = cls.add_func.submit_question(submit_question_data_two)

        # 获取第三题
        receive_question_data_three = {
            'surveyItemId': survey_item_id_two
        }
        question_three = cls.session.get(url=cls.receive_next_question_url_ci, params=receive_question_data_three)
        survey_item_id_three = question_three.json()['surveyItemId']
        print(question_three.status_code, question_three.json())

        # 返回上一题
        par_get_prev_one = {
            'surveyItemId': survey_item_id_three
        }
        response4 = cls.session.get(url=cls.url_get_prev, params=par_get_prev_one)
        cls.assertEqual('您的职业是？', response4.json()['title'])
        cls.assertEqual(200, response4.status_code)

        # 返回上上一题
        par_get_prev_two = {
            'surveyItemId': survey_item_id_two
        }
        response5 = cls.session.get(url=cls.url_get_prev, params=par_get_prev_two)
        case_name = '测试连续两次上一题'
        print(response5.json())
        if not cls.assertEqual('您的身高是多少', response5.json()['title']):
            println(1, case_name)
            cls.assertEqual(200, response5.status_code, response5.json())
        else:
            println(2, case_name)

    # nhy-2336 正常答题选择refuse
    def test_refuse_answer02(cls):
        url_refuse = '%s/api/collection/patientSurveyResultItem/refuse' % ci_url
        body = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': cls.survey_item_id_one
        }
        cls.session.post(url=url_refuse, data=body)

        # 获取第二题
        receive_question_data_two = {
            'surveyItemId': cls.survey_item_id_one
        }
        question_two = cls.session.get(url=cls.receive_next_question_url_ci, params=receive_question_data_two)
        survey_item_id_two = question_two.json()['surveyItemId']
        print(question_two.status_code, question_two.json())

        # 返回上一题
        par_get_prev_one = {
            'surveyItemId': survey_item_id_two
        }
        response = cls.session.get(url=cls.url_get_prev, params=par_get_prev_one)
        cls.assertEqual(200, response.status_code)
        cls.assertEqual('您的身高是多少', response.json()['title'])
        case_name = '正常答题选择refuse'
        if not cls.assertEqual('can_refuse', response.json()['canRefuse']):
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
        else:
            println(2, case_name)

    # nhy-2337 正常答题时，当第二题输入的值没有符合第三题的显示条件，跳至第四题
    def test_not_match_answer03(cls):

        # 提交第一题
        url_post = '%s/api/collection/patientSurveyResultItem' % ci_url
        body_one = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': cls.survey_item_id_one,
            'blankContent': 110,
        }
        response = cls.session.post(url=url_post, data=body_one)
        cls.assertEqual(200, response.status_code)

        # 获取第二题
        par_get_next = {
            'surveyItemId': cls.survey_item_id_one
        }
        question_two = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next)
        survey_item_id_two = question_two.json()['surveyItemId']
        cls.assertEqual(200, question_two.status_code)

        # 提交第二题
        body_two = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_two,
            'selectOptions[0][content]': '专业技术人员',
        }
        response2 = cls.session.post(url=url_post, data=body_two)
        cls.assertEqual(200, response2.status_code)

        # 获取第三题
        par_get_next_three = {
            'surveyItemId': survey_item_id_two
        }
        response3 = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next_three)
        cls.assertEqual(200, response3.status_code)
        case_name = '正常答题时，当第二题输入的值没有符合第三题的显示条件，跳至第四题'
        if not cls.assertEqual('您所处什么治疗阶段？', response3.json()['title']):
            println(1, case_name)
        else:
            println(2, case_name)

    # nhy-2338 正常答题时，当第一题输入的值没有符合第二题的显示条件，第三题的显示条件依赖于第二题，跳至第四题。
    def test_not_match_two_answer04(cls):
        # 提交第一题
        url_post = '%s/api/collection/patientSurveyResultItem' % ci_url
        body_one = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': cls.survey_item_id_one,
            'blankContent': 90,
        }
        response1 = cls.session.post(url=url_post, data=body_one)
        cls.assertEqual(200, response1.status_code)

        # 获取第二题
        par_get_next = {
            'surveyItemId': cls.survey_item_id_one
        }
        response2 = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next)
        cls.assertEqual(200, response2.status_code)
        case_name = '正常答题时，当第一题输入的值没有符合第二题的显示条件，第三题的显示条件依赖于第二题，跳至第四题。'
        if not cls.assertEqual('您的兴趣爱好是什么？', response2.json()['title']):
            println(1, case_name)
        else:
            println(2, case_name)

    # nhy-2339 正常答题时，当第一题输入的值没有符合第二题和第三题的显示条件，跳至第四题。
    def test_not_match_all_answer05(cls):
        # 提交第一题
        url_post = '%s/api/collection/patientSurveyResultItem' % ci_url
        body_one = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': cls.survey_item_id_one,
            'blankContent': 110,
        }
        response1 = cls.session.post(url=url_post, data=body_one)
        cls.assertEqual(200, response1.status_code)

        # 获取第二题
        par_get_next = {
            'surveyItemId': cls.survey_item_id_one
        }
        question_two = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next)
        survey_item_id_two = question_two.json()['surveyItemId']
        cls.assertEqual(200, question_two.status_code)

        # 提交第二题
        body_two = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_two,
            'selectOptions[0][content]': '服务业人员',
        }
        response3 = cls.session.post(url=url_post, data=body_two)
        cls.assertEqual(200, response3.status_code)

        # 获取第三题
        par_get_next_three = {
            'surveyItemId': survey_item_id_two
        }
        response4 = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next_three)
        case_name = '正常答题时，当第一题输入的值没有符合第二题和第三题的显示条件，跳至第四题。'
        if not cls.assertEqual('您的兴趣爱好是什么？', response4.json()['title']):
            println(1, case_name)
        else:
            println(2, case_name)

    # nhy-2343 正常答题时，当第一题的值符合第二题的显示条件，返回上一题，把第一题的值修改也符合第二题的显示条件，跳至第二题。
    def test_two_options_match_answer06(cls):
        # 提交第一题
        url_post = '%s/api/collection/patientSurveyResultItem' % ci_url
        body_one = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': cls.survey_item_id_one,
            'blankContent': 110,
        }
        response1 = cls.session.post(url=url_post, data=body_one)
        cls.assertEqual(200, response1.status_code)
        # 获取第二题
        par_get_next = {
            'surveyItemId': cls.survey_item_id_one
        }
        question_two = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next)
        survey_item_id_two = question_two.json()['surveyItemId']
        cls.assertEqual(200, question_two.status_code)

        # 提交第二题
        body_two = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_two,
            'selectOptions[0][content]': '休养或退休',
        }
        response3 = cls.session.post(url=url_post, data=body_two)
        cls.assertEqual(200, response3.status_code)

        # 获取第三题
        par_get_next_three = {
            'surveyItemId': survey_item_id_two
        }
        question_three = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next_three)
        survey_item_id_three = question_three.json()['surveyItemId']
        cls.assertEqual(200, question_three.status_code)

        # 提交第三题
        body_three = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_three,
            'selectOptions[0][content]': '肺癌',
        }
        response6 = cls.session.post(url=url_post, data=body_three)
        cls.assertEqual(200, response6.status_code)

        # 获取第四题
        par_get_next_four = {
            'surveyItemId': survey_item_id_three
        }
        question_four = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next_four)
        survey_item_id_four = question_four.json()['surveyItemId']
        cls.assertEqual('您所处什么治疗阶段？', question_four.json()['title'])

        # 返回第三题
        par_get_prev_one = {
            'surveyItemId': survey_item_id_four
        }
        response8 = cls.session.get(url=cls.url_get_prev, params=par_get_prev_one)
        cls.assertEqual(200, response8.status_code)

        # 提交第三题
        body_three = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_three,
            'selectOptions[0][content]': '大肠癌',
        }
        response9 = cls.session.put(url=url_post, data=body_three)
        cls.assertEqual(204, response9.status_code)

        # 获取第四题
        par_get_next_four = {
            'surveyItemId': survey_item_id_three
        }
        response10 = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next_four)
        case_name = '正常答题时，当第一题的值符合第二题的显示条件，返回上一题，把第一题的值修改也符合第二题的显示条件，跳至第二题。'
        if not cls.assertEqual('您所处什么治疗阶段？', response10.json()['title']):
            println(1, case_name)
        else:
            println(2, case_name)
    '''
    # 修改搜索选择题
    def test_search_choose_question_modify(cls):
        url_post = '%s/api/collection/patientSurveyResultItem' % ci_url
        # 答第一题
        submit_question_data_one = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': cls.survey_item_id_one,
            'blankContent': 90,
        }
        cls.patientSurveyResultItemId_one = cls.add_func.submit_question(submit_question_data_one)

        # 获取第二题
        par_get_next = {
            'surveyItemId': cls.survey_item_id_one
        }
        question_two = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next)
        survey_item_id_two = question_two.json()['surveyItemId']
        cls.assertEqual(200, question_two.status_code)

        # 提交第二题
        body_two = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_two,
            'selectOptions[0][content]': '基本不参与',
        }
        response3 = cls.session.post(url=url_post, data=body_two)
        cls.assertEqual(200, response3.status_code)

        # 获取第三题
        par_get_next_three = {
            'surveyItemId': survey_item_id_two
        }
        survey_item_id_three = cls.session.get(url=cls.receive_next_question_url_ci, params=par_get_next_three)
        cls.assertEqual(200, response3.status_code)


        # 提交第三题
        body_three = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_three,
            'selectOptions[0][content]': '{"食物":"20"}',
        }
        response9 = cls.session.post(url=url_post, data=body_three)
        cls.assertEqual(200, response9.status_code)

        # 获取第四题
        '''

    def tearDown(self):
        delete_answer_question()

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()














