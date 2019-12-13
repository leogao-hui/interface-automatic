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

add_user_data_one = {
    "organizationnum": "1",
    "password": "admin123",
    "username": "admingao",
    "userrole": "参谋",
}

add_user_data_two = {
    "organizationnum": "1",
    "password": "admin123",
    "username": "admintest",
    "userrole": "参谋",
}

add_user_data_three = {
    "organizationnum": "1",
    "password": "admin123",
    "username": "admintest1",
    "userrole": "参谋",
}

add_user_data_four = {
    "organizationnum": "1",
    "password": "admin123",
    "username": "admintest2",
    "userrole": "参谋",
}

login_user_data_one = {
    "username": add_user_data_one.get('username'),
    "password": add_user_data_one.get('password')
}

login_user_data_two = {
    "username": add_user_data_two.get('username'),
    "password": add_user_data_two.get('password')
}

login_user_data_three = {
    "username": add_user_data_three.get('username'),
    "password": add_user_data_three.get('password')
}

login_user_data_four = {
    "username": add_user_data_four.get('username'),
    "password": add_user_data_four.get('password')
}

device_data = {
                "company": "测试公司",
                "ip": "192.168.1.1",
                "name": "设备一",
                "organizationnum": "1",
                "type": "编码器",
                }