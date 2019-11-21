# author:LEO GAO
# project Encoding:UTF-8

from Common.config import ci_url


class VideoCommandUrl:

    # 新增视频指挥组
    add_video_command_group_url = '%s/spzh/group/add' % ci_url

    # 视频指挥组添加成员
    add_member_video_command_group_url = '%s/spzh/group/addmember' % ci_url

    # 呼叫
    call_url = '%s/spzh/group/calleixt' % ci_url

    # 视频指挥-取消强退
    video_command_cancel_strong_back_url = '%s/spzh/group/cancelretreat' % ci_url

    # 取消协同指挥
    cancel_coordinated_command_url = '%s/spzh/group/cancelxtzh' % ci_url

    # 确认协同指挥
    confirm_coordinated_command_url = '%s/spzh/group/confirmxtzh' % ci_url

    # 删除指挥分组
    delete_command_group_url = '%s/spzh/group/delete' % ci_url

    # 对上静默
    on_the_silent_url = '%s/spzh/group/dsjm' % ci_url

    # 对下静默
    down_the_silent_url = '%s/spzh/group/dxjm' % ci_url

    # 获取视频指挥可操作人员列表
    receive_video_commands_operator_list_url = '%s/spzh/group/getCanOperateMember' % ci_url

    # 结束指挥
    end_of_command_url = '%s/spzh/group/jszh' % ci_url

    # 接替指挥
    replace_of_command_url = '%s/spzh/group/jtzh' % ci_url

    # 视频指挥组-获取该成员启动的组
    video_command_group_member_started_url = '%s/spzh/group/memberGroup' % ci_url

    # 获取视频指挥开启组信息列表
    receive_video_command_group_member_started_list_url = '%s/spzh/group/online' % ci_url

    # 视频指挥组强退成员
    video_command_group_retreats_members_url = '%s/spzh/group/qtcy' % ci_url

    # 取消对上静默
    cancel_on_the_silent_url = '%s/spzh/group/qxdsjm' % ci_url

    # 取消对下静默
    cancel_down_the_silent_url = '%s/spzh/group/qxdxjm' % ci_url

    # 取消接替指挥
    cancel_replace_of_command_url = '%s/spzh/group/qxjtzh' % ci_url

    # 取消授权指挥
    cancel_authorization_of_command_url = '%s/spzh/group/qxsqzh' % ci_url

    # 取消越级指挥
    cancel_great_of_command_url = '%s/spzh/group/qxyjzh' % ci_url

    # 取消专向指挥
    cancel_perform_command_url = '%s/spzh/group/qxzxzh' % ci_url

    # 视频指挥-恢复暂停
    video_command_resume_suspended_url = '%s/spzh/group/recovery' % ci_url

    # 拒绝协同指挥
    refuse_coordinated_command_url = '%s/spzh/group/refusxtzh' % ci_url

    # 视频指挥-进入指挥
    video_command_enter_command_url = '%s/spzh/group/ry/enter' % ci_url

    # 获取视频指挥组详细信息
    receive_video_command_group_details_url = '%s/spzh/group/ry/list' % ci_url

    # 指挥组人员树
    command_group_personnel_tree_url = '%s/spzh/group/ry/tree' % ci_url

    # 申请协同指挥
    apply_coordinated_command_url = '%s/spzh/group/sqxtzh' % ci_url

    # 授权指挥
    authorization_of_command_url = '%s/spzh/group/sqzh' % ci_url

    # 视频指挥组开启指挥
    video_command_group_open_command_url = '%s/spzh/group/start' % ci_url

    # 退出指挥
    exit_the_command_url = '%s/spzh/group/tczh' % ci_url

    # 编辑指挥分组
    editor_command_group_url = '%s/spzh/group/update' % ci_url

    # 获取当前用户指挥分组
    receive_current_user_command_group_url = '%s/spzh/group/user/list' % ci_url

    # 越级指挥
    great_command_url = '%s/spzh/group/yjzh' % ci_url

    # 暂停指挥
    pause_command_url = '%s/spzh/group/ztzh' % ci_url

    # 专向指挥
    perform_command_url = '%s/spzh/group/zxzh' % ci_url

