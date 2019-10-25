# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.addFunction import AddFunction
from Common.coreVersionData import CoreVersionData
from Common.config import ci_url, println


class TestAddPlanToRelease(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        cls.add_func = AddFunction()
        cls.session = requests.session()
        cls.url = '%s/api/rule/solutionVersion' % ci_url

        # 新增直接变量
        solution_group_available_direct_variable_data_one = {
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
        cls.direct_one = cls.add_func.add_direct_variable_with_problem_ci(
            solution_group_available_direct_variable_data_one)

        solution_group_available_direct_variable_data_two = {
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
        cls.direct_two = cls.add_func.add_direct_variable_with_problem_ci(
            solution_group_available_direct_variable_data_two)

        solution_group_available_direct_variable_data_three = {
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
        cls.direct_three = cls.add_func.add_direct_variable_with_problem_ci(
            solution_group_available_direct_variable_data_three)

        search_height_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.direct_one)
        response_height_id = cls.add_func.get_survey_item(url=search_height_url)
        search_job_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.direct_two)
        response_job_id = cls.add_func.get_survey_item(url=search_job_url)
        search_hobby_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.direct_three)
        response_hobby_id = cls.add_func.get_survey_item(url=search_hobby_url)

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
        cls.add_func.modify_survey_item(url=hobby_url, data=data_hobby)

        # 新增计算变量方案组可用
        solution_group_available_calculation_variable_data_one = {
            'name': '计算变量一',
            'optionalValues[0][matchExpression]': '职业$1(休养或退休)',
            'optionalValues[0][content]': '身高+20',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'no'
        }
        cls.calculation_one = cls.add_func.add_calculation_variable_ci(
            solution_group_available_calculation_variable_data_one)

        solution_group_available_calculation_variable_data_two = {
            'name': '计算变量二',
            'optionalValues[0][matchExpression]': '计算变量一=1',
            'optionalValues[0][content]': '2',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.calculation_two = cls.add_func.add_calculation_variable_ci(
            solution_group_available_calculation_variable_data_two)

        solution_group_available_calculation_variable_data_three = {
            'name': '计算变量三',
            'optionalValues[0][matchExpression]': '计算变量二>40',
            'optionalValues[0][content]': '2',
            'optionalValues[0][priority]': 1,
            'optionalValues[0][comment]': 'aaa',
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.calculation_three = cls.add_func.add_calculation_variable_ci(
            solution_group_available_calculation_variable_data_three)

        # 新增量表变量方案组可用
        solution_group_available_scale_variable_data_one = {
            'name': '量表变量一',
            'optionalValues[0][matchExpression]': '计算变量三>60',
            'optionalValues[0][calcuRule]': 'sum',
            'optionalValues[0][rDirectVars][0][variableName]': '身高',
            'optionalValues[0][rDirectVars][0][valueCalcuRule]': 'max',
            'optionalValues[0][rDirectVars][0][comment]': 'aaaa',
            'optionalValues[0][rDirectVars][0][scoreItems][0][matchExp]': '*',
            'optionalValues[0][rDirectVars][0][scoreItems][0][score]': 20,
            'comment': 'aaa',
            'isSolutionCanUse': 'no'
        }
        cls.scale_one = cls.add_func.add_scale_variable_ci(solution_group_available_scale_variable_data_one)

        solution_group_available_scale_variable_data_two = {
            'name': '量表变量二',
            'optionalValues[0][matchExpression]': '量表变量一=20',
            'optionalValues[0][calcuRule]': 'sum',
            'optionalValues[0][rDirectVars][0][variableName]': '身高',
            'optionalValues[0][rDirectVars][0][valueCalcuRule]': 'max',
            'optionalValues[0][rDirectVars][0][comment]': 'aaaa',
            'optionalValues[0][rDirectVars][0][scoreItems][0][matchExp]': '*',
            'optionalValues[0][rDirectVars][0][scoreItems][0][score]': 20,
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.scale_two = cls.add_func.add_scale_variable_ci(solution_group_available_scale_variable_data_two)

        solution_group_available_scale_variable_data_three = {
            'name': '量表变量三',
            'optionalValues[0][matchExpression]': '量表变量二=20',
            'optionalValues[0][calcuRule]': 'sum',
            'optionalValues[0][rDirectVars][0][variableName]': '身高',
            'optionalValues[0][rDirectVars][0][valueCalcuRule]': 'max',
            'optionalValues[0][rDirectVars][0][comment]': 'aaaa',
            'optionalValues[0][rDirectVars][0][scoreItems][0][matchExp]': '*',
            'optionalValues[0][rDirectVars][0][scoreItems][0][score]': 20,
            'comment': 'aaa',
            'isSolutionCanUse': 'yes'
        }
        cls.scale_three = cls.add_func.add_scale_variable_ci(solution_group_available_scale_variable_data_three)

        # 新增显示变量
        solution_group_available_display_variable_data_one = {
            'name': '显示变量一',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '量表变量三=20',
            'optionalValues[0][content]': '显示内容',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': 'comment',
            'isSolutionCanUse': 'no',
            'comment': '111'
        }
        cls.display_one = cls.add_func.add_display_variable_ci(solution_group_available_display_variable_data_one)

        solution_group_available_display_variable_data_two = {
            'name': '显示变量二',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '量表变量三=20',
            'optionalValues[0][content]': '显示内容',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': 'comment',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }
        cls.display_two = cls.add_func.add_display_variable_ci(solution_group_available_display_variable_data_two)

        solution_group_available_display_variable_data_three = {
            'name': '显示变量三',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '量表变量三=20',
            'optionalValues[0][content]': '显示内容',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': 'comment',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }
        cls.display_three = cls.add_func.add_display_variable_ci(solution_group_available_display_variable_data_three)

        # 新增信息结构
        cls.add_func.add_information_structure_ci(CoreVersionData.information_structure_one_data)
        cls.add_func.add_information_structure_ci(CoreVersionData.information_structure_two_data)

        # 新增根模板
        cls.rootTplId = cls.add_func.add_root_template_ci(CoreVersionData.root_template_data)

        # 新增评估项
        solution_group_available_evaluate_data_one = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '随访关注',
            'rank': 1,
            'name': '测试评估名1',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(身高>50)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }
        cls.evaluate_one = cls.add_func.add_evaluate_ci(solution_group_available_evaluate_data_one)

        solution_group_available_evaluate_data_two = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '随访关注',
            'rank': 1,
            'name': '测试评估名2',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(身高>50)&(职业$1(休养或退休))&(计算变量二=20)&(量表变量二=30)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'no',
            'comment': '111'
        }
        cls.evaluate_two = cls.add_func.add_evaluate_ci(solution_group_available_evaluate_data_two)

        solution_group_available_evaluate_data_three = {
            'templateId': cls.rootTplId,
            'tags[0][name]': '标签一',
            'tags[1][name]': '随访关注',
            'rank': 1,
            'name': '测试评估名3',
            'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"*","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                       '"content":[{"表达式":"(身高>50)&(职业$1(专业技术人员))&(计算变量二=20)&(量表变量二=30)&(测试评估名1=匹配用结果项名1)","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
            'isSolutionCanUse': 'yes',
            'comment': '111'
        }
        cls.evaluate_three = cls.add_func.add_evaluate_ci(solution_group_available_evaluate_data_three)

        # 新增计算变量方案组专用
        project_group_specific_calculation_variable_one_data = {
            'name': '方案组专用计算变量一',
            'optionalValues[0][matchExpression]': '(计算变量二=40)&(量表变量二=40)&(测试评估名3=匹配用结果项名1)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.solutionCalcuVariableId_one = cls.add_func.add_solution_group_solution_calculationVariable(
            project_group_specific_calculation_variable_one_data)

        project_group_specific_calculation_variable_two_data = {
            'name': '方案组专用计算变量二',
            'optionalValues[0][matchExpression]': '(方案组专用计算变量一=40)&(量表变量二=40)&(测试评估名3=匹配用结果项名1)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.solutionCalcuVariableId_two = cls.add_func.add_solution_group_solution_calculationVariable(
            project_group_specific_calculation_variable_two_data)

        project_group_specific_calculation_variable_three_data = {
            'name': '方案组专用计算变量三',
            'optionalValues[0][matchExpression]': '(方案组专用计算变量二=40)&(量表变量二=40)&(测试评估名1=匹配用结果项名1)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.solutionCalcuVariableId_three = cls.add_func.add_solution_group_solution_calculationVariable(
            project_group_specific_calculation_variable_three_data)

        project_group_specific_calculation_variable_four_data = {
            'name': '方案组专用计算变量四',
            'optionalValues[0][matchExpression]': '(方案组专用计算变量三=40)&(量表变量二=40)&(测试评估名1=匹配用结果项名1)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.solutionCalcuVariableId_four = cls.add_func.add_solution_group_solution_calculationVariable(
            project_group_specific_calculation_variable_four_data)

        project_group_specific_display_variable_one_data = {
            'name': '方案组专用显示变量一',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '(方案组专用计算变量二=40)&(量表变量二=40)&(测试评估名3=匹配用结果项名1)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.solutionDisplayVariableId_one = cls.add_func.add_solution_group_solution_displayVariable(
            project_group_specific_display_variable_one_data)

        project_group_specific_display_variable_two_data = {
            'name': '方案组专用显示变量二',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '(方案组专用计算变量二=40)&(量表变量二=40)&(测试评估名3=匹配用结果项名1)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.solutionDisplayVariableId_two = cls.add_func.add_solution_group_solution_displayVariable(
            project_group_specific_display_variable_two_data)

        project_group_specific_display_variable_three_data = {
            'name': '方案组专用显示变量三',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '(方案组专用计算变量二=40)&(量表变量二=40)&(测试评估名3=匹配用结果项名1)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.solutionDisplayVariableId_three = cls.add_func.add_solution_group_solution_displayVariable(
            project_group_specific_display_variable_three_data)

        project_group_specific_display_variable_four_data = {
            'name': '方案组专用显示变量四',
            'joinMark': ',',
            'optionalValues[0][matchExpression]': '(方案组专用计算变量二=40)&(量表变量二=40)&(测试评估名3=匹配用结果项名1)',
            'optionalValues[0][content]': '1',
            'optionalValues[0][priority]': '1',
            'optionalValues[0][comment]': '111',
            'module': 'mentality_module',
            'comment': ''
        }
        cls.solutionDisplayVariableId_four = cls.add_func.add_solution_group_solution_displayVariable(
            project_group_specific_display_variable_four_data)

        # 新增评估版本
        evaluate_version_one_data = {
            'name': '测试版本',
            'items[0][itemId]': cls.direct_one,
            'items[0][itemType]': 'direct_variable',
            'items[1][itemId]': cls.evaluate_one,
            'items[1][itemType]': 'evaluate_item',
        }
        cls.evVersionId_one = cls.add_func.add_evaluate_version_ci(evaluate_version_one_data)

        # 新增方案项
        project_item_one_data = {
            'name': '方案项一',
            'module': 'movement_module'
        }
        cls.solutionItemId_one = cls.add_func.add_project_item(project_item_one_data)

        project_item_two_data = {
            'name': '方案项二',
            'module': 'movement_module'
        }
        cls.solutionItemId_two = cls.add_func.add_project_item(project_item_two_data)

        # 新增方案组成
        solution_composition_data_one = {
            'name': '方案组成一',
            'solutionItemId': cls.solutionItemId_one,
            'conditionExpression': '*',
            'displayOrder': 1,
            'content': '[{"name":"方案组成结果1","displayContent":"具体显示内容","group":"1","comment":"备注","conditions":[{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"}]},{"name":"方案组成结果2","displayContent":"具体显示内容1","group":"2","comment":"备注","conditions":[{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"}]}]',
            'comment': ''
        }
        cls.solutionCompositionId_one = cls.add_func.add_solution_composition(solution_composition_data_one)

        # 新增方案评定
        scheme_evaluation_one_data = {
            'name': '方案评定一',
            'solutionItemId': cls.solutionItemId_two,
            'conditionExpression': '*',
            'displayOrder': 1,
            'content': '[{"name":"方案评定结果","grade":"normal","displayContent":"具体显示内容","group":"1","comment":"备注","conditions":[{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]},{"name":"方案评定结果2","grade":"anomaly","displayContent":"具体显示内容2","group":"2","comment":"备注","conditions":[{"expression":"(职业$1(休养或退休))","presentation":"情况说明","comment":"备注"},{"expression":"(职业$1(专业技术人员))","presentation":"情况说明","comment":"备注"}]}]',
            'comment': ''
        }
        cls.solutionAssessmentId_one = cls.add_func.add_scheme_evaluation(scheme_evaluation_one_data)

    def test_01(cls):
        data = {
            'name': '方案版本1',
            'evVersionId': cls.evVersionId_one,
            'solutionItems[0][itemId]': cls.solutionCompositionId_one,
            'solutionItems[0][itemType]': 'solution_composition',
        }
        case_name = '测试'
        response = cls.session.post(url=cls.url, data=data)
        if response.status_code == 422:
            println(1, case_name)
            cls.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            cls.assertEqual(422, response.status_code)
        else:
            println('what fuck')

    def test_02(cls):
        # 新增方案评定
        data = {
            'name': '方案版本1',
            'evVersionId': cls.evVersionId_one,
            'solutionItems[0][itemId]': cls.solutionAssessmentId_one,
            'solutionItems[0][itemType]': 'solution_assessment',
        }
        case_name = '测试'
        response = cls.session.post(url=cls.url, data=data)
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
