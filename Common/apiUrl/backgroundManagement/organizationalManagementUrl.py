# author:LEO GAO
# project Encoding:UTF-8

from Common.config import ci_url


class OrganizationalManagementUrl:

    # 组织架构信息-新增
    organizational_information_add_url = '%s/organization/add' % ci_url

    # 组织架构信息-删除
    organizational_information_delete_url = '%s/organization/delete' % ci_url

    # 组织架构信息-拖拽变更
    organizational_information_drag_drop_change_url = '%s/organization/drag' % ci_url

    # 获取组织树
    receive_organizational_tree_url = '%s/organization/tree' % ci_url

    # 组织架构信息-修改
    organizational_information_update_url = '%s/organization/update' % ci_url

