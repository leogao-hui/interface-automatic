#_author:leo gao
#encoding:utf-8

import requests
import json
import random

administrator_login_data = {
  "createtime": "",
  "deviceid": "",
  "devicename": "",
  "id": "",
  "ip": "",
  "lastloginerrortime": "",
  "lastlogintime": "",
  "logincode": "",
  "loginerrorcount": 0,
  "loginstatus": 0,
  "morendevice": "",
  "num": "string",
  "organizationname": "",
  "organizationnum": "",
  "page": 0,
  "password": "admin123",
  "realname": "",
  "rows": 0,
  "searchkey": "",
  "status": "",
  "translaterealname": "",
  "username": "admin",
  "userrole": "",
  "usestatus": ""
}

add_user_data_one = {
    "password": "admin123",
    "username": "admin",
}

url = 'http://10.66.9.15/sys/login'

header = {"Content-Type": "application/json", "charset": "UTF-8", "x-forward-for":
        str(random.randint(1, 255)) + str(random.randint(1, 255)) + str(random.randint(1, 255)) + str(random.randint(1, 255))}
response = requests.session().post(url=url, data=json.dumps(administrator_login_data), headers=header)
print(response)