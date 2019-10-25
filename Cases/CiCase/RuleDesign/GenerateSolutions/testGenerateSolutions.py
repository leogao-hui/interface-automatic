# author:LEO GAO
# project Encoding:UTF-8

import unittest
import requests
from Common.addFunction import AddFunction
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.coreVersionData import CoreVersionData
from Common.config import ci_url


class TestGenerateSolutions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        cls.add_func = AddFunction()
        cls.session = requests.session()

        # 新增食材
        food_one = {
            'serialNumber': 1,
            'name': '芸豆',
            'status': 'solidState',
            'class': 'composite_staple_food',
            'nutrients[0][name]': 'protein',
            'nutrients[0][amount]': 14,
            'nutrients[0][unit]': 'g',
            'nutrients[0][class]': 'energy_calculation_related',
            'nutrients[1][name]': 'iron',
            'nutrients[1][amount]': 5,
            'nutrients[1][unit]': 'mg',
            'nutrients[1][class]': 'minerals',
            'nutrients[2][name]': 'vitamin_A',
            'nutrients[2][amount]': 300,
            'nutrients[2][unit]': 'μgRE',
            'nutrients[2][class]': 'vitamins',
            'cookedFoodRation': '11',
            'cookedFoodRationPicture': '22'
        }
        cls.food_one_id = cls.add_func.add_food_ci(food_one)

        food_two = {
            'serialNumber': 2,
            'name': '黑木耳',
            'status': 'solidState',
            'class': 'fungi',
            'nutrients[0][name]': 'polyunsaturated_fatty_acid',
            'nutrients[0][amount]': 10,
            'nutrients[0][unit]': 'g',
            'nutrients[0][class]': 'fatty_acids',
            'nutrients[1][name]': 'ascorbic',
            'nutrients[1][amount]': 40,
            'nutrients[1][unit]': 'mg',
            'nutrients[1][class]': 'vitamins',
            'nutrients[2][name]': 'thiamin',
            'nutrients[2][amount]': 0.5,
            'nutrients[2][unit]': 'mg',
            'nutrients[2][class]': 'vitamins',
            'cookedFoodRation': '11',
            'cookedFoodRationPicture': '22'
        }
        cls.food_two_id = cls.add_func.add_food_ci(food_two)

        food_three = {
            'serialNumber': 3,
            'name': '紫菜',
            'status': 'solidState',
            'class': 'algae',
            'nutrients[0][name]': 'polyunsaturated_fatty_acid',
            'nutrients[0][amount]': 10,
            'nutrients[0][unit]': 'g',
            'nutrients[0][class]': 'fatty_acids',
            'cookedFoodRation': '11',
            'cookedFoodRationPicture': '22'
        }
        cls.food_three_id = cls.add_func.add_food_ci(food_three)

        food_four = {
            'serialNumber': 4,
            'name': '鸭血',
            'status': 'liquidState',
            'class': 'poultry',
            'nutrients[1][name]': 'iron',
            'nutrients[1][amount]': 5,
            'nutrients[1][unit]': 'mg',
            'nutrients[1][class]': 'minerals',
            'cookedFoodRation': '11',
            'cookedFoodRationPicture': '22'
        }
        cls.food_four_id = cls.add_func.add_food_ci(food_four)

        # 新增食材标签
        food_label_library_one = {
            'name': '富含铁',
            'category': '微量元素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(铁>=4.5))|((状态=液体)&(铁>=2.25))',
            'presentation': '固体大于4.5，液体大于2.25',
            'exclusionGroup': '100',
            'comment': '',
        }
        cls.food_label_library_one_id = cls.add_func.add_food_label_library(food_label_library_one)

        food_label_library_two = {
            'name': '高蛋白质',
            'category': '产能营养素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(蛋白质>=12))|((状态=液体)&(蛋白质>=6))',
            'presentation': '固体食物蛋白质含量大于12克/100克或者液体食物大于6克/100毫升，即认为是高蛋白食物',
            'exclusionGroup': '90',
            'comment': '',
        }
        cls.food_label_library_two_id = cls.add_func.add_food_label_library(food_label_library_two)

        food_label_library_three = {
            'name': '富含多不饱和脂肪酸',
            'category': '产能营养素',
            'type': '定量',
            'rationStandard': '(多不饱和脂肪酸>=9.9)',
            'presentation': '多不饱和脂肪酸含量超过9.9%即认为是富含多不饱和脂肪酸',
            'exclusionGroup': '80',
            'comment': '',
        }
        cls.food_label_library_three_id = cls.add_func.add_food_label_library(food_label_library_three)

        food_label_library_four = {
            'name': '富含维生素A',
            'category': '脂溶性维生素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(总维生素>=240)|(状态=液体)&(总维生素>=120))',
            'presentation': '固体大于240，液体大于120',
            'exclusionGroup': '70',
            'comment': '',
        }
        cls.food_label_library_four_id = cls.add_func.add_food_label_library(food_label_library_four)

        food_label_library_five = {
            'name': '富含维生素E',
            'category': '脂溶性维生素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(维生素B1>=4.2))|((状态=液体)&(维生素B1>=2.1))',
            'presentation': '固体大于4.2；液体大于2.1',
            'exclusionGroup': '60',
            'comment': '',
        }
        cls.food_label_library_five_id = cls.add_func.add_food_label_library(food_label_library_five)

        food_label_library_six = {
            'name': '富含维生素C',
            'category': '脂溶性维生素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(维生素C>=30))|((状态=液体)&(维生素C>=15))',
            'presentation': '固体大于30，液体大于15',
            'exclusionGroup': '50',
            'comment': '',
        }
        cls.food_label_library_six_id = cls.add_func.add_food_label_library(food_label_library_six)

        food_label_library_seven = {
            'name': '富含维生素B1',
            'category': '水溶性维生素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(维生素B1>=0.42))|((状态=液体)&(维生素B1>=0.21))',
            'presentation': '固体大于0.42，液体大于0.21',
            'exclusionGroup': '40',
            'comment': '',
        }
        cls.food_label_library_seven_id = cls.add_func.add_food_label_library(food_label_library_seven)

        body_one = {
            'name': '性别'
        }
        body_two = {
            'name': '年龄'
        }
        # 获取系统变量
        system_variable_one = cls.add_func.get_system_variable_ci(data=body_one)
        system_variable_two = cls.add_func.get_system_variable_ci(data=body_two)

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
        cls.response_search_id = cls.add_func.add_direct_variable_with_problem_ci(search_data)

        # 查看直接变量对应的id
        search_height_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_height_id)
        response_height_id = cls.add_func.get_survey_item(url=search_height_url)
        search_job_url = '%s/api/rule/directVariable/%s' % (ci_url, cls.response_job_id)
        response_job_id = cls.add_func.get_survey_item(url=search_job_url)
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

        data_search = {
            'groups[0][displayTitle]': '',
            'groups[0][rawTitle]': '测试搜索选择题键值对型？',
            'groups[0][material][type]': '',
            'groups[0][material][url]': ''
        }
        search_url = '%s/api/rule/surveyItem/%s' % (ci_url, response_search_id)
        cls.add_func.modify_survey_item(url=search_url, data=data_search)

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
        cls.response_calculation_one_id = cls.add_func.add_calculation_variable_ci(calculation_variable_one_data)

        # 新增量表变量
        scale_variable_one_data = {
            'name': '量表变量',
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
        cls.response_scale_one_id = cls.add_func.add_scale_variable_ci(scale_variable_one_data)

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
        cls.evaluateItemId_one_id = cls.add_func.add_evaluate_ci(evaluate_one_data)
        cls.evaluateItemId_two_id = cls.add_func.add_evaluate_ci(evaluate_two_data)

        cls.food_material_apply_scene_one_data = {
            'name': '测试场景库1',
            'categoryId': 3,
            'conditionExpression': '身高>60',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型1","conditionExpression":"测试评估名2=匹配用结果项名1","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"多维生素E","influence":"low","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"多维生素C","influence":"low","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"多维生素B1","influence":"high","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含铁","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"high","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向二情况说明","influence":"low","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"high","comment":""}]}}]',
        }

        cls.food_material_apply_scene_two_data = {
            'name': '测试场景库2',
            'categoryId': 3,
            'conditionExpression': '身高>60',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型3","conditionExpression":"测试评估名2=匹配用结果项名1","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"多维生素E","influence":"low","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"多维生素C","influence":"low","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"多维生素B1","influence":"high","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型4","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含铁","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"high","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向二情况说明二","influence":"high","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"high","comment":""}]}}]',
        }

        # 新增食材应用场景库
        cls.foodMaterialApplyScenarioId_one_id = cls.add_func.add_food_application_scene_library(cls.food_material_apply_scene_one_data)
        cls.foodMaterialApplyScenarioId_two_id = cls.add_func.add_food_application_scene_library(cls.food_material_apply_scene_two_data)

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
            'items[4][itemId]': cls.response_scale_one_id,
            'items[4][itemType]': 'scale_variable',
            'items[5][itemId]': cls.evaluateItemId_one_id,
            'items[5][itemType]': 'evaluate_item',
            'items[6][itemId]': cls.evaluateItemId_two_id,
            'items[6][itemType]': 'evaluate_item',
        }

        cls.evVersionId_one = cls.add_func.add_evaluate_version_ci(evaluate_version_one_data)

        # 新增套餐
        # 获取评估版本中实体项
        get_url = '%s/api/rule/evlVersions/%s' % (ci_url, cls.evVersionId_one)
        response_evaluate_version_real_item_one = cls.session.get(url=get_url)
        evaluate_item_data = []
        direct_variable_data = []
        calculation_variable_data = []
        scale_variable_data = []
        for key in (response_evaluate_version_real_item_one.json()['items']):
            if key['itemType'] == 'evaluate_item':
                evaluate_item_data.append(key['itemId'])
            elif key['itemType'] == 'direct_variable':
                direct_variable_data.append(key['itemId'])
            elif key['itemType'] == 'scale_variable':
                scale_variable_data.append(key['itemId'])
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
        cls.realItem_six = scale_variable_data[0]

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
            'items[3][itemType]': 'scale_variable',
            'items[4][itemId]': cls.realItem_four,
            'items[4][itemType]': 'evaluate_item',
            'items[5][itemId]': cls.realItem_five,
            'items[5][itemType]': 'evaluate_item',
            'items[6][itemId]': cls.realItem_seven,
            'items[6][itemType]': 'direct_variable',

        }
        cls.comboId_one = cls.add_func.add_combo_ci(combo_one)

        # 新增团队
        team_data_one = {
            'name': '测试团队'
        }

        cls.teamId_one = cls.add_func.add_team_ci(team_data_one)

        # 新增成员
        team_member_data_one = {
            'phone': '123456',
            'password': '123456',
            'name': '123456',
            'belongTeamId': cls.teamId_one,
            'identity': 'manager'
        }

        cls.clerkId_one = cls.add_func.add_team_number_ci(team_member_data_one)

        # 新增建档
        filling_data_one = {
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

        cls.patientSurveyResultId_one = cls.add_func.add_filing_ci(filling_data_one)

        # 答题
        # 获取第一题
        receive_next_question_url_ci = '%s/api/collection/patientSurveyResult/%s/nextSurveyItem' % (ci_url, cls.patientSurveyResultId_one)
        question_one = cls.session.get(url=receive_next_question_url_ci)
        print(question_one.status_code, question_one.json())
        survey_item_id_one = question_one.json()['surveyItemId']

        # 答第一题
        submit_question_data_one = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_one,
            'blankContent': 110,
        }
        cls.patientSurveyResultItemId_one = cls.add_func.submit_question(submit_question_data_one)

        # 获取第二题
        receive_question_data_two = {
            'surveyItemId': survey_item_id_one
        }
        question_two = cls.session.get(url=receive_next_question_url_ci, params=receive_question_data_two)
        survey_item_id_two = question_two.json()['surveyItemId']
        print(question_two.status_code, question_two.json())

        # 答第二题
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
        question_three = cls.session.get(url=receive_next_question_url_ci, params=receive_question_data_three)
        survey_item_id_three = question_three.json()['surveyItemId']
        print(question_three.status_code, question_three.json())

        # 答第三题
        submit_question_data_three = {
            'patientSurveyResultId': cls.patientSurveyResultId_one,
            'surveyItemId': survey_item_id_three,
            'selectOptions[0][content]': '{"食物":"20"}',
        }
        cls.patientSurveyResultItemId_three = cls.add_func.submit_question(submit_question_data_three)

        # 提交问卷
        submit_questionnaire_url_ci = '%s/api/collection/patientSurveyResult/%s/complete' % (ci_url, cls.patientSurveyResultId_one)
        cls.session.put(url=submit_questionnaire_url_ci)

        # 场景表详情
        cls.scene_table_details_url_ci = '%s/api/production/patientSolution/%s/applyScenario' % (ci_url, cls.patientSurveyResultId_one)

        # 标签表详情
        cls.label_table_details_url_ci = '%s/api/production/patientSolution/%s/relateFoodMaterialTags' % (ci_url, cls.patientSurveyResultId_one)

        # 方案食材表
        cls.food_table_details_url_ci = '%s/api/production/patientSolution/%s/relateFoodMaterials' % (ci_url, cls.patientSurveyResultId_one)

    # 生成方案 查看输出值与预期值是否一致
    def test_generate_solution_compare_want_with_print(cls):
        # 更新定量标签
        update_quantitative_tag_url = '%s/api/rule/foodMaterials/updateFoodMaterialTags' % ci_url
        cls.session.put(url=update_quantitative_tag_url)

        par = {
            'patientSurveyResultId': cls.patientSurveyResultId_one
        }
        cls.add_func.generate_solution(par)

        # 获取场景表详情
        scene_data = cls.session.get(url=cls.scene_table_details_url_ci)
        print(scene_data.json())
        scene_data_name_out = []
        for key in scene_data.json()['applyScenarios']:
            scene_data_name_out.append(key['name'])
            if scene_data.json()['applyScenarios'][0]['name'] == cls.food_material_apply_scene_one_data['name']:
                cls.assertEqual('呼吸系统', key['category'])
            if scene_data.json()['applyScenarios'][1]['name'] == cls.food_material_apply_scene_two_data['name']:
                cls.assertEqual('呼吸系统', key['category'])
        scene_data_name_in = []
        for key_two in scene_data.json()['applyScenarios']:
            for key_three in key_two['illnesses']:
                scene_data_name_in.append(key_three['name'])
            for key_three in key_two['remedies']:
                scene_data_name_in.append(key_three['name'])
        cls.assertEqual('测试类型1', scene_data_name_in[0])
        cls.assertEqual('测试类型2', scene_data_name_in[1])
        cls.assertEqual('测试类型3', scene_data_name_in[2])
        cls.assertEqual('测试类型4', scene_data_name_in[3])

        # 获取标签表详情
        tag_data = cls.session.get(url=cls.label_table_details_url_ci)
        print(tag_data.json())
        '''
        for key_four in tag_data.json()['tags']:
            if key_four['name'] == '富含铁':
                #cls.assertIn('recommend', key_four['suitability'])
                cls.assertEqual('微量元素', key_four['category'])
                situation_one_data = []
                for key_data_one in key_four['presentation']:
                    situation_one_data.append(key_data_one)
                cls.assertIn('需要铁', situation_one_data)
                cls.assertIn('正向一情况说明', situation_one_data)
                food_one_data = []
                for key_food in key_four['relateFoodMaterials']:
                    food_one_data.append(key_food['name'])
                cls.assertIn('鸭血', food_one_data)
                cls.assertIn('芸豆', food_one_data)
            elif key_four['name'] == '高蛋白质':
                #cls.assertIn('recommend', key_four['suitability'])
                cls.assertEqual('产能营养素', key_four['category'])
                situation_two_data = []
                for key_data_one in key_four['presentation']:
                    situation_two_data.append(key_data_one)
                cls.assertEqual('需要蛋白质', situation_two_data[0])
                food_two_data = []
                for key_food in key_four['relateFoodMaterials']:
                    food_two_data.append(key_food['name'])
                cls.assertIn('芸豆', food_two_data)
            elif key_four['name'] == '富含多不饱和脂肪酸':
                #cls.assertIn('prohibited', key_four['suitability'])
                cls.assertEqual('产能营养素', key_four['category'])
                situation_three_data = []
                for key_data_one in key_four['presentation']:
                    situation_three_data.append(key_data_one)
                #cls.assertIn('负向二情况说明二', situation_three_data)
                cls.assertIn('负向二情况说明', situation_three_data)
                food_three_data = []
                for key_food in key_four['relateFoodMaterials']:
                    food_three_data.append(key_food['name'])
                cls.assertIn('黑木耳', food_three_data)
                cls.assertIn('紫菜', food_three_data)
            elif key_four['name'] == '富含维生素A':
                #cls.assertIn('prohibited', key_four['suitability'])
                cls.assertEqual('脂溶性维生素', key_four['category'])
                situation_four_data = []
                for key_data_one in key_four['presentation']:
                    situation_four_data.append(key_data_one)
                cls.assertIn('负向三情况说明', situation_four_data)
                food_four_data = []
                for key_food in key_four['relateFoodMaterials']:
                    food_four_data.append(key_food['name'])
                cls.assertIn('芸豆', food_four_data)
            elif key_four['name'] == '富含维生素E':
                #cls.assertIn('notRecommended', key_four['suitability'])
                cls.assertEqual('脂溶性维生素', key_four['category'])
                situation_five_data = []
                for key_data_one in key_four['presentation']:
                    situation_five_data.append(key_data_one)
                cls.assertIn('多维生素E', situation_five_data)
                food_five_data = []
                for key_food in key_four['relateFoodMaterials']:
                    food_five_data.append(key_food['name'])
                cls.assertEqual(0, len(food_five_data))
            elif key_four['name'] == '富含维生素C':
                #cls.assertIn('notRecommended', key_four['suitability'])
                cls.assertEqual('脂溶性维生素', key_four['category'])
                situation_six_data = []
                for key_data_one in key_four['presentation']:
                    situation_six_data.append(key_data_one)
                cls.assertIn('多维生素C', situation_six_data)
                food_six_data = []
                for key_food in key_four['relateFoodMaterials']:
                    food_six_data.append(key_food['name'])
                cls.assertIn('黑木耳', food_six_data)
            elif key_four['name'] == '富含维生素B1':
                #cls.assertIn('prohibited', key_four['suitability'])
                cls.assertEqual('水溶性维生素', key_four['category'])
                situation_seven_data = []
                for key_data_one in key_four['presentation']:
                    situation_seven_data.append(key_data_one)
                cls.assertIn('负向一情况说明', situation_seven_data)
                food_seven_data = []
                for key_food in key_four['relateFoodMaterials']:
                    food_seven_data.append(key_food['name'])
                cls.assertIn('黑木耳', food_seven_data)
            else:
                print('---数据有问题---')
        '''

        # 获取方案食材表详情
        food_data = cls.session.get(url=cls.food_table_details_url_ci)
        print(food_data.json())
        '''
        for key_food_material in food_data.json()['foodMaterials']:
            if key_food_material['name'] == '鸭血':
                cls.assertEqual('recommend', key_food_material['suitability'])
                for description_key in key_food_material['presentation']:
                    cls.assertIn('需要铁', description_key)
                    cls.assertIn('正向一情况说明')
                for tag_key in key_food_material['relateTags']:
                    cls.assertEqual('富含铁', tag_key['name'])
        '''

    @classmethod
    def tearDownClass(cls):
        pass
        #delete_database_data_test_ci()
