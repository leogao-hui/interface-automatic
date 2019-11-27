#_author:leo gao
#encoding:utf-8

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


add_user_data = {
    "organizationnum": "1",
    "password": "admin123",
    "username": "admintest",
    "userrole": "参谋",
}

user_wrong_password_login_data = {
    "username": add_user_data.get('username'),
    "password": add_user_data.get('password') + 'a'
}

