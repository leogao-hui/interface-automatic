#_author:leo gao
#encoding:utf-8

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