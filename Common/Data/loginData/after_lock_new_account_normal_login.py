#_author:leo gao
#encoding:utf-8

add_user_data = {
    "organizationnum": "1",
    "password": "admin123",
    "username": "admintest2",
    "userrole": "参谋",
}

user_five_time_wrong_password_lock_account_login_data = {
    "username": add_user_data.get('username'),
    "password": add_user_data.get('password') + 'a'
}

new_account_data = {
    "username": 'admin',
    "password": 'admin123'
}