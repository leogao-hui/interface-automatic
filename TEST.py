#_author:leo gao
#encoding:utf-8

import requests
import json

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
    "password": "admin@123",
    "username": "wt",
}

url = 'http://10.66.9.15/sys/login'


header = {"Content-Type": "application/json", "charset": "UTF-8"}
response = requests.session().post(url=url, data=json.dumps(add_user_data_one), headers=header)
print(response)