# author:LEO GAO
# project Encoding:UTF-8


import unittest
import requests
from Common.config import generate_evaluation_data_url_ci

'''
class TestBuildData(unittest.TestCase):

    def setUp(self):

        self.url = generate_evaluation_data_url_ci
        self.session = requests.session()

    def test_generate_evaluation_data(self):

        database_data = {
            'fromDatabase[address]': 'rm-2ze99312f0be55dyc2o.mysql.rds.aliyuncs.com',
            'fromDatabase[port]': '3306',
            'fromDatabase[name]': 'api_huiyu_services',
            'fromDatabase[userName]': 'huiyu_read',
            'fromDatabase[password]': 'Wskj1111',
            'toDatabase[address]': '192.168.1.195',
            'toDatabase[port]': '3306',
            'toDatabase[name]': 'test_api_huiyu_services_test',
            'toDatabase[userName]': 'root',
            'toDatabase[password]': 'wskj1111',
            'type': 'library',
            'items[0][itemId]': 422,
            'items[1][itemId]': 423,
            'items[2][itemId]': 424,
            'items[3][itemId]': 425,
            'items[4][itemId]': 426,
            'items[5][itemId]': 427,
            'items[6][itemId]': 428,
            'items[7][itemId]': 429,
            'items[8][itemId]': 430,
        }

        response = self.session.post(url=self.url, data=database_data)
        print(response.elapsed.total_seconds())
'''