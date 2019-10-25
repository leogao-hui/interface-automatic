# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.addFunction import AddFunction
from Common.operateDatabaseData import delete_database_data_test_ci, add_database_data_ci
from Common.coreVersionData import CoreVersionData
from Common.config import add_food_application_scene_library_url_ci, println


class TestAddFoodApplicationSceneLibrary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_ci()
        add_func = AddFunction()
        cls.session = requests.session()

        # 新增食材
        food_one = {
            'serialNumber': 1,
            'name': '芸豆',
            'status': 'solidState',
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
        cls.food_one_id = add_func.add_food_ci(food_one)

        food_two = {
            'serialNumber': 2,
            'name': '黑木耳',
            'status': 'solidState',
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
        cls.food_two_id = add_func.add_food_ci(food_two)

        food_three = {
            'serialNumber': 3,
            'name': '紫菜',
            'status': 'solidState',
            'nutrients[0][name]': 'polyunsaturated_fatty_acid',
            'nutrients[0][amount]': 10,
            'nutrients[0][unit]': 'g',
            'nutrients[0][class]': 'fatty_acids',
            'cookedFoodRation': '11',
            'cookedFoodRationPicture': '22'
        }
        cls.food_three_id = add_func.add_food_ci(food_three)

        food_four = {
            'serialNumber': 4,
            'name': '鸭血',
            'status': 'liquidState',
            'nutrients[1][name]': 'iron',
            'nutrients[1][amount]': 5,
            'nutrients[1][unit]': 'mg',
            'nutrients[1][class]': 'minerals',
            'cookedFoodRation': '11',
            'cookedFoodRationPicture': '22'
        }
        cls.food_four_id = add_func.add_food_ci(food_four)

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
        cls.food_label_library_one_id = add_func.add_food_label_library(food_label_library_one)

        food_label_library_two = {
            'name': '高蛋白质',
            'category': '产能营养素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(蛋白质>=12))|((状态=液体)&(蛋白质>=6))',
            'presentation': '固体食物蛋白质含量大于12克/100克或者液体食物大于6克/100毫升，即认为是高蛋白食物',
            'exclusionGroup': '90',
            'comment': '',
        }
        cls.food_label_library_two_id = add_func.add_food_label_library(food_label_library_two)

        food_label_library_three = {
            'name': '富含多不饱和脂肪酸',
            'category': '产能营养素',
            'type': '定量',
            'rationStandard': '(多不饱和脂肪酸>=9.9)',
            'presentation': '多不饱和脂肪酸含量超过9.9%即认为是富含多不饱和脂肪酸',
            'exclusionGroup': '80',
            'comment': '',
        }
        cls.food_label_library_three_id = add_func.add_food_label_library(food_label_library_three)

        food_label_library_four = {
            'name': '富含维生素A',
            'category': '脂溶性维生素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(总维生素>=240)|(状态=液体)&(总维生素>=120))',
            'presentation': '固体大于240，液体大于120',
            'exclusionGroup': '70',
            'comment': '',
        }
        cls.food_label_library_four_id = add_func.add_food_label_library(food_label_library_four)

        food_label_library_five = {
            'name': '富含维生素E',
            'category': '脂溶性维生素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(维生素B1>=4.2))|((状态=液体)&(维生素B1>=2.1))',
            'presentation': '固体大于4.2；液体大于2.1',
            'exclusionGroup': '60',
            'comment': '',
        }
        cls.food_label_library_five_id = add_func.add_food_label_library(food_label_library_five)

        food_label_library_six = {
            'name': '富含维生素C',
            'category': '脂溶性维生素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(维生素C>=30))|((状态=液体)&(维生素C>=15))',
            'presentation': '固体大于30，液体大于15',
            'exclusionGroup': '50',
            'comment': '',
        }
        cls.food_label_library_six_id = add_func.add_food_label_library(food_label_library_six)

        food_label_library_seven = {
            'name': '富含维生素B1',
            'category': '水溶性维生素',
            'type': '定量',
            'rationStandard': '((状态=固体)&(维生素B1>=0.42))|((状态=液体)&(维生素B1>=0.21))',
            'presentation': '固体大于0.42，液体大于0.21',
            'exclusionGroup': '40',
            'comment': '',
        }
        cls.food_label_library_seven_id = add_func.add_food_label_library(food_label_library_seven)

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

    # 食材应用场景名为空 报错必填
    def test_food_application_scene_library_name_null(self):
        data = {
            'name': '',
            'categoryId': 3,
            'conditionExpression': '身高>60',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]'
                        'i}}]',
        }
        case_name = '食材应用场景名为空 报错必填'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 食材应用场景分类ID为空 报错必填
    def test_food_application_scene_library_ID_null(self):
        data = {
            'name': '测试名',
            'categoryId': '',
            'conditionExpression': '身高>60',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[]}}]',
        }
        case_name = '食材应用场景分类ID为空 报错必填'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 食材应用场景适用条件为空 报错必填
    def test_food_application_scene_library_condition_null(self):
        data = {
            'name': '测试名1',
            'categoryId': 3,
            'conditionExpression': '',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[]}}]',
        }
        case_name = '食材应用场景适用条件为空 报错必填'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 食材应用场景说明情况为空 报错必填
    def test_food_application_scene_library_suitable_condition_null(self):
        data = {
            'name': '测试名1',
            'categoryId': 3,
            'conditionExpression': '身高>60',
            'description': '',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[]}}]',
        }
        case_name = '食材应用场景说明情况为空 报错必填'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 食材应用场景病情为空 报错必填
    def test_food_application_scene_library_illness_null(self):
        data = {
            'name': '测试名1',
            'categoryId': 3,
            'conditionExpression': '身高>60',
            'description': '情况说明',
            'illnesses': '',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含铁","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"高蛋白质","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[]}}]',
        }
        case_name = '食材应用场景病情为空 报错必填'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 食材应用场景治疗为空 报错必填
    def test_food_application_scene_library_remedies_null(self):
        data = {
            'name': '测试名1',
            'categoryId': 3,
            'conditionExpression': '身高>70',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': ''
        }
        case_name = '食材应用场景治疗为空 报错必填'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 同一个病情中的分期表达式重复 报错
    def test_food_application_scene_library_installment_suitable_condition_not_repeat_one_illness(self):
        data = {
            'name': '测试名1',
            'categoryId': 3,
            'conditionExpression': '身高>70',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}},{"name":"测试类型2","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸,"conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]}}]',
        }
        case_name = '同一个病情中的分期表达式重复 报错'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 同一个治疗中的分期表达式重复 报错
    def test_food_application_scene_library_installment_suitable_condition_not_repeat_one_remedies(self):
        data = {
            'name': '测试名1',
            'categoryId': 3,
            'conditionExpression': '身高>70',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]}},{"name":"测试类型3","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含铁","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"高蛋白质","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]}}]',
        }
        case_name = '同一个治疗中的分期表达式重复 报错'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 同一个病情中的分期类型重复 报错
    def test_food_application_scene_library_suitable_installment_type_not_repeat_one_remedies(self):
        data = {
            'name': '测试名1',
            'categoryId': 3,
            'conditionExpression': '身高>70',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>80","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeCrisisTags":[],{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"多血清","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"高葡萄糖","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"高脂肪","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[{"name":"高碳水","conditionExpression":"*","presentation":"碳水超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]}}]',
        }
        case_name = '同一个病情中的分期类型重复 报错'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 同一个治疗中的分期类型重复 报错
    def test_food_application_scene_library_installment_type_not_repeat_one_remedies(self):
        data = {
            'name': '测试名1',
            'categoryId': 3,
            'conditionExpression': '身高>70',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]}},{"name":"测试类型2","conditionExpression":"身高>100","positive":{"enhanceTreatmentTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含铁","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]}}]',
        }
        case_name = '同一个治疗中的分期表达式重复 报错'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')
    '''
    # 病情和治疗的分期表达式重复 报错
    def test_food_application_scene_library_suitable_condition_repeat_between_illnesses_and_remedies(self):
        data = {
            'name': '测试名',
            'categoryId': 3,
            'conditionExpression': '身高>60',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>60","positive":{"enhanceTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]}}]',
        }
        case_name = '病情和治疗的分期表达式重复 报错'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')
        '''

    # 在正向（负向）的同一个标题下标签重复 报错
    def test_food_application_scene_library_tag_repeat_in_title(self):
        data = {
            'name': '测试场景库1',
            'categoryId': 3,
            'conditionExpression': '身高>60',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"高蛋白质","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"高影响","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"高影响","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响高","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响高","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响高","comment":""}]}}]',
        }
        case_name = '在正向（负向）的同一个标题下标签重复 报错'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code, response.json())
        elif response.status_code != 422:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 新增食材场景应用库 正常保存
    def test_food_application_scene_library_create(self):
        data = {
            'name': '测试场景库1',
            'categoryId': 3,
            'conditionExpression': '身高>60',
            'description': '情况说明',
            'illnesses': '[{"name":"测试类型","conditionExpression":"身高>60","positive":{"controlEnemyTags":[{"name":"富含铁","conditionExpression":"*","presentation":"需要铁","comment":"111"},{"name":"高蛋白质","conditionExpression":"*","presentation":"需要蛋白质","comment":"222"}],"supplyTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"不饱和脂肪酸多","comment":"111"}],"easeSymptomTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"多维生素A","comment":""}]},"negative":{"helpEnemyTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"血清超标","influence":"高影响","comment":"1111"}],"negativeSupplyTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"葡萄糖超标","influence":"影响high","comment":""}],"causeAdverseReactionTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"脂肪超标","influence":"影响hign","comment":""}],"causeCrisisTags":[]}}]',
            'remedies': '[{"name":"测试类型2","conditionExpression":"身高>70","positive":{"enhanceTreatmentTags":[{"name":"富含维生素E","conditionExpression":"*","presentation":"正向一情况说明","comment":"11"}],"easeSymptomTags":[{"name":"富含维生素C","conditionExpression":"*","presentation":"正向二情况说明","comment":""}]},"negative":{"interfereTreatmentTags":[{"name":"富含维生素B1","conditionExpression":"*","presentation":"负向一情况说明","influence":"影响hign","comment":""}],"causeAdverseReactionTags":[{"name":"富含多不饱和脂肪酸","conditionExpression":"*","presentation":"负向二情况说明","influence":"影响hign","comment":""}],"causeCrisisTags":[{"name":"富含维生素A","conditionExpression":"*","presentation":"负向三情况说明","influence":"影响hign","comment":""}]}}]',
        }
        case_name = '新增食材场景应用库 正常保存'
        response = self.session.post(url=add_food_application_scene_library_url_ci, data=data)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code, response.json())
        elif response.status_code != 200:
            println(2, case_name)
            print(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()








