#_author:leo gao
#encoding:utf-8

import json
import requests
url = 'http://10.66.8.200:8088/spzh/sys/login'
header = {
"Content-Type": "application/json"
}
data = {
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

response = requests.session().post(url=url, data=json.dumps(data), headers=header)
print(response.status_code)