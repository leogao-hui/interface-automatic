# author:LEO GAO
# project Encoding:UTF-8

from Common.config import ci_url


class ExternalInterfaceManagementUrl:

    # 接口信息-新增
    interface_information_add_url = '%s/service/add' % ci_url

    # 接口信息-列表
    interface_information_list_url = '%s/service/getpage' % ci_url

    # 获取新媒体地址
    receive_new_media_address_url = '%s/service/getwebsocketUrl' % ci_url

    # 接口信息-修改
    interface_information_update_url = '%s/service/update' % ci_url

