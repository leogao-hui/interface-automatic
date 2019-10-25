# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import ci_url, println
from Common.operateDatabaseData import delete_database_data_test_ci


class TestAddFood(unittest.TestCase):

    def setUp(self):
        delete_database_data_test_ci()
        self.url = '%s/api/rule/foodMaterial' % ci_url
        self.session = requests.session()

    # 正常新增食物
    def test_normal_food(self):
        food_data = {
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
        case_name = '正常新增食物'
        response = self.session.post(url=self.url, data=food_data)
        if response.status_code == 200:
            println(1, case_name)
            self.assertEqual(200, response.status_code)
        elif response.status_code != 200:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(200, response.status_code)
        else:
            print('what fuck')

    # 测试类型id为空 报错
    def test_abnormal_food_serialNumber_null(self):
        food_data = {
            'serialNumber': '',
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
        case_name = '测试类型id为空 报错'
        response = self.session.post(url=self.url, data=food_data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    # 测试类型食物名为空 报错
    def test_abnormal_food_name_null(self):
        food_data = {
            'serialNumber': 1,
            'name': '',
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
        case_name = '测试类型食物名为空 报错'
        response = self.session.post(url=self.url, data=food_data)
        if response.status_code == 422:
            println(1, case_name)
            self.assertEqual(422, response.status_code)
        elif response.status_code != 422:
            println(2, case_name)
            println(2, response.json())
            self.assertEqual(422, response.status_code)
        else:
            print('what fuck')

    def tearDown(self):
        delete_database_data_test_ci()
