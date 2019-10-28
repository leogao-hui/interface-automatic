# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import ci_url
from Common.config import println
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci


class TestAddDirectVariableProblem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        cls.url = '%s/api/rule/directVariable' % ci_url
        cls.session = requests.session()

    # nhy-2107 新增直接变量-题目，当题目类型为多选时，值结构为集合，取值范围类型为序列，值类型为文本型时，正常新增直接变量-题目。
    def test_normal_directVariableProblem_create01(cls):
        body = {
            "variableName": "性别",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": "男",
            "optionalValues[0][sort]": "1",
            "optionalValues[1][variableValue]": "女",
            "optionalValues[1][sort]": "2",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的性别是？",
            "surveyItem[rank]": "1",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "multiple_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "comment",
            "surveyItem[options][0][surveyItemValue]": "汉子",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "妹子",
            "surveyItem[options][1][sort]": "2",
        }
        case_name = 'nhy-2107 新增直接变量-题目，当题目类型为多选时，值结构为集合，取值范围类型为序列，值类型为文本型时，正常新增直接变量-题目'
        response = cls.session.post(cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            # println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

        # 缺少get接口校验

    # nhy-2108 新增直接变量-题目，当题目类型为填空时，值结构为单值，取值范围类型为数值区间，值类型为数值型，正常新增直接变量-题目。
    def test_normal_directVariableProblem_create02(cls):
        body = {
            "variableName": "测试直接变量(填空题)",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试拒绝题目",
            "surveyItem[rank]": "10",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = 'nhy-2108 新增直接变量-题目，当题目类型为填空时，值结构为单值，取值范围类型为数值区间，值类型为数值型，正常新增直接变量-题目'
        response = cls.session.post(cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # nhy-2109 新增直接变量-题目，当题目类型为单选时，值结构为单值，取值范围类型为序列，值类型为数值型或文本型时，正常新增直接变量-题目。
    def test_normal_directVariableProblem_create03(cls):
        body = {
            "variableName": "职业",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": "司机",
            "optionalValues[0][sort]": "1",
            "optionalValues[1][variableValue]": "厨师",
            "optionalValues[1][sort]": "2",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的职业是？",
            "surveyItem[rank]": "3",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "single_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[explanation]": '解释说明',
            "surveyItem[comment]": "comment",
            "surveyItem[options][0][surveyItemValue]": "司机",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "厨师",
            "surveyItem[options][1][sort]": "2",
        }
        case_name = 'nhy-2109 新增直接变量-题目，当题目类型为单选时，值结构为单值，取值范围类型为序列，值类型为数值型或文本型时，正常新增直接变量-题目'
        response = cls.session.post(cls.url, data=body)
        if response.status_code == 200:
            println(1, case_name)
            cls.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # nhy-2094 新增直接变量-题目，当变量名没有填写时，报错变量名必填。
    def test_abnormal_directVariableProblem_create01(cls):
        body = {
            "variableName": "",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是11？",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "11",
        }
        case_name = 'nhy-2094 新增直接变量-题目，当变量名没有填写时，报错变量名必填'
        response = cls.session.post(url=cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2095 新增直接变量-题目，当题目名没有填写时，报错题目名必填。
    def test_abnormal_directVariableProblem_create02(cls):
        body = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "20",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = 'nhy-2095 新增直接变量-题目，当题目名没有填写时，报错题目名必填'
        response = cls.session.post(cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2096 新增直接变量-题目，当场景分类没有选择时，报错场景分类必选。
    def test_abnormal_directVariableProblem_create03(cls):
        body = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是？",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = 'nhy-2096 新增直接变量-题目，当场景分类没有选择时，报错场景分类必选'
        response = cls.session.post(cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2097 新增直接变量-题目，当显示顺序没有填写时，报错显示顺序必选。
    def test_abnormal_directVariableProblem_create04(cls):
        body = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是？",
            "surveyItem[rank]": "",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = 'nhy-2097 新增直接变量-题目，当显示顺序没有填写时，报错显示顺序必选'
        response = cls.session.post(cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2098 新增直接变量-题目，当拒绝答题没有填时，报错拒绝问题必选。
    def test_abnormal_directVariableProblem_create05(cls):
        body = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "",
            "surveyItem[title]": "您的年龄是？",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = 'nhy-2098 新增直接变量-题目，当拒绝答题没有填时，报错拒绝问题必选'
        response = cls.session.post(cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2102 新增直接变量-题目，当选项中的值重复时，报错选项的值不能重复。
    def test_abnormal_directVariableProblem_create06(cls):
        body = {
            "variableName": "职业",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": "司机",
            "optionalValues[0][sort]": "1",
            "optionalValues[1][variableValue]": "厨师",
            "optionalValues[1][sort]": "2",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的职业是？",
            "surveyItem[rank]": "3",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "single_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[explanation]": '解释说明',
            "surveyItem[comment]": "comment",
            "surveyItem[options][0][surveyItemValue]": "司机",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "司机",
            "surveyItem[options][1][sort]": "2",
        }
        case_name = 'nhy-2102 新增直接变量-题目，当选项中的值重复时，报错选项的值不能重复'
        response = cls.session.post(cls.url, data=body)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            cls.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # nhy-2103 新增直接变量-题目，当变量名重复时，报错变量名不能重复。
    def test_abnormal_directVariableProblem_create10(cls):
        body1 = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是？",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        body2 = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是1？",
            "surveyItem[rank]": "40",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = 'nhy-2103 新增直接变量-题目，当变量名重复时，报错变量名不能重复'
        cls.session.post(cls.url, data=body1)
        response_two = cls.session.post(cls.url, data=body2)
        if response_two.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response_two.status_code)
        elif response_two.status_code != 422:
            println(2, case_name)
            println(2, response_two.json())
            cls.assertEqual(422, response_two.status_code)
        else:
            print('what fuck')

    # nhy-2104 新增直接变量-题目，当题目重复时，报错题目不能重复。
    def test_abnormal_directVariableProblem_create11(cls):
        body1 = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是？",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        body2 = {
            "variableName": "年龄1",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是？",
            "surveyItem[rank]": "40",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '新增直接变量-题目，当题目重复时，报错题目不能重复'
        cls.session.post(cls.url, data=body1)
        response_two = cls.session.post(cls.url, data=body2)
        if response_two.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response_two.status_code)
        elif response_two.status_code != 422:
            println(2, case_name)
            println(2, response_two.json())
            cls.assertEqual(422, response_two.status_code)
        else:
            print('what fuck')

    # nhy-2106 新增直接变量-题目，当显示顺序一致时，报错显示顺序不能重复。
    def test_abnormal_directVariableProblem_create12(cls):
        body1 = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是？",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        body2 = {
            "variableName": "年龄1",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是1？",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '新增直接变量-题目，当显示顺序一致时，报错显示顺序不能重复'
        response_one = cls.session.post(cls.url, data=body1)
        response_two = cls.session.post(cls.url, data=body2)
        if response_two.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response_two.status_code)
        elif response_two.status_code != 422:
            println(2, case_name)
            println(2, response_two.json())
            cls.assertEqual(422, response_two.status_code)
        else:
            print('what fuck')

    # nhy-2113 新增直接变量-题目，当显示条件重复时，报错显示条件不能重复。
    def test_abnormal_directVariableProblem_create16(cls):
        body1 = {
            "variableName": "年龄1",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是1？",
            "surveyItem[rank]": "30",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        body2 = {
            "variableName": "年龄",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "您的年龄是？",
            "surveyItem[rank]": "40",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[preConditionItems][0][matchExp]": '年龄>50',
            "surveyItem[preConditionItems][0][description]": 'aaa',
            "surveyItem[preConditionItems][1][matchExp]": '年龄>50',
            "surveyItem[preConditionItems][1][description]": 'aaa',
        }
        case_name = '新增直接变量-题目，当显示条件重复时，报错显示条件不能重复'
        cls.session.post(url=cls.url, data=body1)
        response_two = cls.session.post(url=cls.url, data=body2)
        if response_two.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response_two.status_code)
        elif response_two.status_code != 422:
            println(2, case_name)
            println(2, response_two.json())
            cls.assertEqual(422, response_two.status_code)
        else:
            print('what fuck')

    # 题目类型为单选题时，值类型可以为数值型
    def test_normal_directVariableProblem_SingleChoice_numerical(cls):
        body = {
            "variableName": "测试单选题数值型",
            "variableValueType": "numerical",
            "optionalValues[0][variableValue]": '10',
            "optionalValues[0][sort]": 1,
            "optionalValues[1][variableValue]": '20',
            "optionalValues[1][sort]": 2,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试单选题数值型？",
            "surveyItem[rank]": "1000",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "single_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[options][0][surveyItemValue]": "1",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "2",
            "surveyItem[options][1][sort]": "2",
        }
        case_name = '题目类型为单选题时，值类型可以为数值型'
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

    # 题目类型为单选题时，值类型可以为文本型
    def test_normal_directVariableProblem_SingleChoice_text(cls):
        body = {
            "variableName": "测试单选题文本型",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": '一',
            "optionalValues[0][sort]": 1,
            "optionalValues[1][variableValue]": '二',
            "optionalValues[1][sort]": 2,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试单选题文本型？",
            "surveyItem[rank]": "1100",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "single_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[options][0][surveyItemValue]": "司机",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "司机2",
            "surveyItem[options][1][sort]": "2",
        }
        case_name = '题目类型为单选题时，值类型可以文本型'
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

    # 题目类型为单选题时，值类型不可以为键值对
    def test_abnormal_directVariableProblem_SingleChoice_not_keyValue(cls):
        body = {
            "variableName": "测试单选题键值对型",
            "variableValueType": "key_value",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试单选题键值对型？",
            "surveyItem[rank]": "1100",
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "single_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '题目类型为单选题时，值类型不可以为键值对'
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

    # 题目类型为多选题时，值类型可以为文本型
    def test_normal_directVariableProblem_MultipleChoice_text(cls):
        body = {
            "variableName": "测试多选题文本型",
            "variableValueType": "text",
            "optionalValues[0][variableValue]": '一',
            "optionalValues[0][sort]": 1,
            "optionalValues[1][variableValue]": '二',
            "optionalValues[1][sort]": 2,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试多选题文本型？",
            "surveyItem[rank]": "1200",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "multiple_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[options][0][surveyItemValue]": "司机",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "司机2",
            "surveyItem[options][1][sort]": "2",
        }
        case_name = '题目类型为多选题时，值类型可以为文本型'
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

    # 题目类型为多选题时，值类型不可以为数值型
    def test_abnormal_directVariableProblem_MultipleChoice_not_numerical(cls):
        body = {
            "variableName": "测试多选题数值型",
            "variableValueType": "numerical",
            "optionalValues[0][variableValue]": '111',
            "optionalValues[0][sort]": 1,
            "optionalValues[1][variableValue]": '222',
            "optionalValues[1][sort]": 2,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试多选题数值型？",
            "surveyItem[rank]": "1300",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "multiple_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '题目类型为多选题时，值类型不可以为数值型'
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

    # 题目类型为多选题时，值类型不可以为键值对型
    def test_abnormal_directVariableProblem_MultipleChoice_not_keyValue(cls):
        body = {
            "variableName": "测试多选题键值对",
            "variableValueType": "key_value",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试多选题键值对型？",
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[rank]": "1400",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "multiple_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '题目类型为多选题时，值类型不可以为键值对型'
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

    # 题目类型为填空题时，值类型可以为数值型
    def test_normal_directVariableProblem_fillUp_numerical(cls):
        body = {
            "variableName": "测试填空题数值型",
            "variableValueType": "numerical",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试填空题数值型？",
            "surveyItem[rank]": "2000",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '题目类型为填空题时，值类型可以为数值型'
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

    # 题目类型为填空题时，值类型不可以为文本型
    def test_abnormal_directVariableProblem_fillUp_text(cls):
        body = {
            "variableName": "测试填空题文本型",
            "variableValueType": "text",
            "optionalValueMin": 10,
            "optionalValueMax": 100,
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试填空题文本型？",
            "surveyItem[rank]": "1500",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '题目类型为填空题时，值类型不可以为文本型'
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

    # 题目类型为填空题时，值类型不可以为键值对型
    def test_abnormal_directVariableProblem_fillUp_keyValue(cls):
        body = {
            "variableName": "测试填空题键值对型",
            "variableValueType": "key_value",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试填空题键值对型？",
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[rank]": "1500",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "fillup",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '题目类型为填空题时，值类型不可以为键值对型'
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

    # 题目类型为搜索选择题时，值类型可以为键值对型
    def test_normal_directVariableProblem_SearchChoice_keyValue(cls):
        body = {
            "variableName": "测试搜索选择题键值对",
            "variableValueType": "key_value",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试搜索选择题键值对型？",
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[rank]": "1600",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "search_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '题目类型为搜索选择题时，值类型可以为键值对型'
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
    '''
    # 题目类型为搜索选择题时，值类型可以为文本型
    def test_normal_directVariableProblem_SearchChoice_text(cls):
        body = {
            "variableName": "测试搜索选择题文本型",
            "variableValueType": "text",
            "isSolutionCanUse": "yes",
            "optionalValues[0][variableValue]": "男",
            "optionalValues[0][sort]": "1",
            "optionalValues[1][variableValue]": "女",
            "surveyItem[title]": "测试搜索选择题文本型？",
            "surveyItem[rank]": "1900",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "search_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[options][0][surveyItemValue]": "汉子",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "妹子",
            "surveyItem[options][1][sort]": "2",

        }
        case_name = '题目类型为搜索选择题时，值类型可以为文本型'
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
        '''
    # 题目类型为搜索选择题时，值类型不可以为数值型
    def test_normal_directVariableProblem_SearchChoice_numerical(cls):
        body = {
            "variableName": "测试搜索选择题数值型",
            "variableValueType": "numerical",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试搜索选择题数值型？",
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[rank]": "1700",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "search_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
        }
        case_name = '题目类型为搜索选择题时，值类型不可以为数值型'
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

    # defaultSequence和options不能同时出现
    def test_normal_directVariableProblem_defaultSequence_options_all(cls):
        body = {
            "variableName": "测试同时出现",
            "variableValueType": "numerical",
            "isSolutionCanUse": "yes",
            "surveyItem[title]": "测试同时出现？",
            "optionalValues[0][variableValue]": '111',
            "optionalValues[0][sort]": 1,
            "optionalValues[1][variableValue]": '222',
            "optionalValues[1][sort]": 2,
            "surveyItem[defaultSequence]": "food_measuring_library",
            "surveyItem[rank]": "1700",
            "surveyItem[topicId]": "1",
            "surveyItem[type]": "search_choice",
            "surveyItem[canRefuse]": "can_refuse",
            "surveyItem[device]": "device",
            "surveyItem[comment]": "",
            "surveyItem[options][0][surveyItemValue]": "1",
            "surveyItem[options][0][sort]": "1",
            "surveyItem[options][1][surveyItemValue]": "2",
            "surveyItem[options][1][sort]": "2",

        }
        case_name = 'defaultSequence和options不能同时出现'
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

