# author:LEO GAO
# project Encoding:UTF-8

from Common.config import ci_url


class SystemConfigurationUrl:

    # 获取验证码
    receive_verification_code_url = '%s/sys/getVerify' % ci_url

    # 登录
    login_url = '%s/sys/login' % ci_url

    # 退出
    exit_url = '%s/sys/logout' % ci_url

    # 业务重启
    business_restart_url = '%s/sys/restartSys' % ci_url
