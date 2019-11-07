#_author:LEO GAO
#_project Encoding: UTF-8


from Common.config import ci_url


# 是否有账户
account_check_url = '%s/account/check' % ci_url

# 是否需要信息验证码
is_account_register_need_captcha_url = '%s/account/register-need-captcha' % ci_url

# 用户注册
account_register_url = '%s/account/register' % ci_url

# 验证码登录
login_with_smscode_url = '%s/login_with_smscode_url' % ci_url

# 密码登录
login_with_pw_url = '%s/account/login-with-password' % ci_url



