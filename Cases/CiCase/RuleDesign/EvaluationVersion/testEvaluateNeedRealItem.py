# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData
from Common.config import ci_url
from Common.operateDatabaseData import delete_database_data_test_ci
from Common.operateDatabaseData import add_database_data_ci
from Common.config import println


class TestAddEvaluationVersion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        add_func = AddFunction()
        cls.session = requests.session()
        # 获取评估项所需的实体项
        cls.url = '%s/api/rule/evlItems/RelateItems' % ci_url

        # 新增直接变量
        cls.response_height_id = add_func.add_direct_variable_with_problem_ci(CoreVersionData.height_data)
        cls.response_job_id = add_func.add_direct_variable_with_problem_ci(CoreVersionData.job_data)
        cls.response_tumor_id = add_func.add_direct_variable_with_problem_ci(CoreVersionData.tumor_data)
        cls.response_treatment_id = add_func.add_direct_variable_with_problem_ci(CoreVersionData.treatment_stage_data)
        cls.response_hobby_id = add_func.add_direct_variable_with_problem_ci(CoreVersionData.hobby_data)

        # 查看直接变量对应的id
        search_height_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_height_id)
        response_height_id = add_func.get_survey_item(url=search_height_url)
        search_job_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_job_id)
        response_job_id = add_func.get_survey_item(url=search_job_url)
        search_tumor_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_tumor_id)
        response_tumor_id = add_func.get_survey_item(url=search_tumor_url)
        search_treatment_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_treatment_id)
        response_treatment_id = add_func.get_survey_item(url=search_treatment_url)
        search_hobby_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_hobby_id)
        response_hobby_id = add_func.get_survey_item(url=search_hobby_url)

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

        data_tumor = {
            'groups[0][displayTitle]': '您得过什么瘤种？',
            'groups[0][rawTitle]': '',
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
        add_func.modify_survey_item(url=tumor_url, data=data_tumor)

        data_treatment = {
            'groups[0][displayTitle]': '您所处什么治疗阶段？',
            'groups[0][rawTitle]': '',
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
        add_func.modify_survey_item(url=treatment_url, data=data_treatment)

        data_hobby = {
            'groups[0][displayTitle]': '您的兴趣爱好是什么？',
            'groups[0][rawTitle]': '',
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
        add_func.modify_survey_item(url=hobby_url, data=data_hobby)

        # 新增计算变量
        add_func.add_calculation_variable_ci(CoreVersionData.calculation_variable_one_data)
        add_func.add_calculation_variable_ci(CoreVersionData.calculation_variable_two_data)
        add_func.add_calculation_variable_ci(CoreVersionData.calculation_variable_three_data)

        # 新增量表变量
        add_func.add_scale_variable_ci(CoreVersionData.scale_variable_one_data)

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

        # 2328
        evaluate_two_data = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '标签二',
            'rank': 2,
            'name': '测试评估名2',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(计算变量一>50)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }

        # nhy2329
        evaluate_three_data = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '标签二',
            'rank': 3,
            'name': '测试评估名3',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(量表变量=1)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }

        # nhy2330
        evaluate_four_data = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '标签二',
            'rank': 4,
            'name': '测试评估名4',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(计算变量二>50)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }

        # 2327
        evaluate_five_data = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '标签二',
            'rank': 5,
            'name': '测试评估名5',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(测试评估名2=匹配用结果项名1)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }

        evaluate_six_data = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '标签二',
            'rank': 6,
            'name': '测试评估名6',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(测试评估名5=匹配用结果项名1)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }

        # 新增评估项
        cls.evaluateItemId_one = add_func.add_evaluate_ci(evaluate_one_data)
        cls.evaluateItemId_two = add_func.add_evaluate_ci(evaluate_two_data)
        cls.evaluateItemId_three = add_func.add_evaluate_ci(evaluate_three_data)
        cls.evaluateItemId_four = add_func.add_evaluate_ci(evaluate_four_data)
        cls.evaluateItemId_five = add_func.add_evaluate_ci(evaluate_five_data)
        cls.evaluateItemId_six = add_func.add_evaluate_ci(evaluate_six_data)

    # nhy-2328 新增评估版本，评估项中用到计算变量，解析出计算变量所用到的直接变量
    def test_01(cls):
        params = {
            'evlItems[0][id]': cls.evaluateItemId_two,
        }
        case_name = ' 新增评估版本，评估项中用到计算变量，解析出计算变量所用到的直接变量'
        response = cls.session.get(url=cls.url, params=params)
        assert_value = []
        for i in response.json()['evlItems']:
            assert_value.append(i['itemName'])
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
            cls.assertIn('身高', assert_value)
            cls.assertIn('职业', assert_value)
            cls.assertIn('计算变量一', assert_value)
        elif response.status_code != 200:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # nhy-2329 新增评估版本，评估项中用到量表变量，解析出量表变量所用到的直接变量
    def test_02(cls):
        params = {
            'evlItems[0][id]': cls.evaluateItemId_three,
        }
        case_name = '新增评估版本，评估项中用到量表变量，解析出量表变量所用到的直接变量'
        response = cls.session.get(url=cls.url, params=params)
        assert_value = []
        for i in response.json()['evlItems']:
            assert_value.append(i['itemName'])
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
            cls.assertIn('身高', assert_value)
            cls.assertIn('量表变量', assert_value)
        elif response.status_code != 200:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # nhy-2330 新增评估版本，评估项中用到嵌套计算变量的计算变量，解析出两个计算变量所用到的直接变量。
    def test_03(cls):
        params = {
            'evlItems[0][id]': cls.evaluateItemId_four,
        }
        case_name = '新增评估版本，评估项中用到嵌套计算变量的计算变量，解析出两个计算变量所用到的直接变量'
        response = cls.session.get(url=cls.url, params=params)
        assert_value = []
        for i in response.json()['evlItems']:
            assert_value.append(i['itemName'])
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
            cls.assertIn('身高', assert_value)
            cls.assertIn('职业', assert_value)
            cls.assertIn('计算变量一', assert_value)
            cls.assertIn('计算变量二', assert_value)
        elif response.status_code != 200:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # bhy-2331 新增评估版本，评估项中用到计算变量嵌套量表变量，计算变量中的直接变量有显示条件，显示条件中的直接变量有显示条件，解析出所有用到的没有用到显示条件的直接变量。
    def test_04(cls):
        params = {
            'evlItems[0][id]': cls.evaluateItemId_one,
        }
        case_name = '新增评估版本，评估项中用到计算变量嵌套量表变量，计算变量中的直接变量有显示条件，显示条件中的直接变量有显示条件，解析出所有用到的没有用到显示条件的直接变量'
        response = cls.session.get(url=cls.url, params=params)
        assert_value = []
        for i in response.json()['evlItems']:
            assert_value.append(i['itemName'])
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
            cls.assertIn('身高', assert_value)
            cls.assertIn('职业', assert_value)
            cls.assertIn('计算变量一', assert_value)
            cls.assertIn('计算变量二', assert_value)
            cls.assertIn('治疗阶段', assert_value)
            cls.assertIn('瘤种', assert_value)
        elif response.status_code != 200:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # nhy-2327 新增评估版本，当选择的评估项包含另一个评估项时，包含的评估项所涉及到的变量也需要展示。
    def test_05(cls):
        params = {
            'evlItems[0][id]': cls.evaluateItemId_five
        }
        case_name = '新增评估版本，当选择的评估项包含另一个评估项时，包含的评估项所涉及到的变量也需要展示'
        response = cls.session.get(url=cls.url, params=params)
        assert_value = []
        for i in response.json()['evlItems']:
            assert_value.append(i['itemName'])
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
            cls.assertIn('身高', assert_value)
            cls.assertIn('职业', assert_value)
            cls.assertIn('计算变量一', assert_value)
            cls.assertIn('测试评估名2', assert_value)
        elif response.status_code != 200:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # nhy-2327 新增评估版本，当选择的评估项包含另一个评估项,这个评估项又包含另一个评估项时，包含的评估项所涉及到的变量也需要展示。
    def test_06(cls):
        params = {
            'evlItems[0][id]': cls.evaluateItemId_six
        }
        case_name = '新增评估版本，当选择的评估项包含另一个评估项,这个评估项又包含另一个评估项时，包含的评估项所涉及到的变量也需要展示'
        response = cls.session.get(url=cls.url, params=params)
        assert_value = []
        for i in response.json()['evlItems']:
            assert_value.append(i['itemName'])
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code, response.json())
            cls.assertIn('身高', assert_value)
            cls.assertIn('职业', assert_value)
            cls.assertIn('计算变量一', assert_value)
            cls.assertIn('测试评估名2', assert_value)
            cls.assertIn('测试评估名5', assert_value)
        elif response.status_code != 200:
            println(2, case_name)
            print(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()








