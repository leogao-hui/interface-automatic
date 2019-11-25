# author:LEO GAO
# project Encoding:UTF-8

from Common.config import ci_url


class UserManagementUrl:

    # 用户信息-新增
    user_add_url = '%s/spzh/user/add' % ci_url

    # 用户绑定设备
    user_bind_device_url = '%s/user/bddevice' % ci_url

    # 用户删除
    user_delete_url = '%s/user/delete' % ci_url

    # 获取解码器
    receive_decoder_url = '%s/user/getdecoder' % ci_url

    # 获取编译和启动时间
    receive_compile_and_start_time_url = '%s/user/getEdition' % ci_url

    # 用户获取列表
    user_receive_list_url = '%s/user/getpage' % ci_url

    # 获取系统时间
    receive_system_time_url = '%s/user/getSysDate' % ci_url

    # 根据用户id判断用户是否在线
    user_isOnline_url = '%s/user/getuserstatus' % ci_url

    # 重置用户密码
    reset_user_password_url = '%s/user/reset/password' % ci_url

    # 用户信息修改
    user_update_url = '%s/user/update' % ci_url

    # 修改用户初始化密码
    update_user_initialize_password_url = '%s/user/update/initpassword' % ci_url

    # 修改用户密码
    update_user_password_url = '%s/user/update/password' % ci_url

    # 根据用户名修改用户信息
    according_user_update_user_url = '%s/user/update/username' % ci_url
