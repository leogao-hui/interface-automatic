# author:LEO GAO
# project Encoding:UTF-8

from Common.config import ci_url


class DeviceManagementUrl:

    # 设备信息-新增
    add_device_url = '%s/device/add' % ci_url

    # 设备信息-删除
    delete_device_url = '%s/device/delete' % ci_url

    # 设备信息查询
    device_information_query_url = '%s/device/detect' % ci_url

    # 设备未绑定用户列表获取
    device_not_tied_to_user_list_url = '%s/device/get/wbd/page' % ci_url

    # 设备列表获取
    device_receive__list_url = '%s/device/getpage' % ci_url

    # 设备信息-修改
    device_update_url = '%s/device/update' % ci_url

    # 设备信息-同步统一设备信息
    synchronize_unified_device_information_url = '%s/device/update/sync' % ci_url
