# author:LEO GAO
# project Encoding:UTF-8

import requests
from Common.apiUrl.BusinessControlOver.videoCommandUrl import VideoCommandUrl
from Common.config import header


def add_video_command_group(data):
    '''
    新增视频指挥组
    :param data: 新增视频指挥组数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.add_video_command_group_url, data=data)
    return response


def add_member_video_command_group(data):
    '''
    视频指挥组添加成员
    :param data: 视频指挥组添加成员数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.add_member_video_command_group_url, data=data)
    return response


def call(data):
    '''
    呼叫
    :param data: 呼叫数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.call_url, data=data)
    return response


def video_command_cancel_strong_back(data):
    '''
    视频指挥-取消强退
    :param data: 视频指挥-取消强退数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.video_command_cancel_strong_back_url, data=data)
    return response


def cancel_coordinated_command(data):
    '''
    取消协同指挥
    :param data: 取消协同指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.cancel_coordinated_command_url, data=data)
    return response


def confirm_coordinated_command(data):
    '''
    确认协同指挥
    :param data: 确认协同指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.confirm_coordinated_command_url, data=data)
    return response


def delete_command_group(data):
    '''
    删除指挥分组
    :param data: 删除指挥分组
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.delete_command_group_url, data=data)
    return response


def on_the_silent(data):
    '''
    对上静默
    :param data: 对上静默数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.on_the_silent_url, data=data)
    return response


def down_the_silent(data):
    '''
    对下静默
    :param data: 对下静默数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.down_the_silent_url, data=data)
    return response


def receive_video_commands_operator_list(data):
    '''
    获取视频指挥可操作人员列表
    :param data: 获取视频指挥可操作人员列表数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.receive_video_commands_operator_list_url, data=data)
    return response


def end_of_command(data):
    '''
    结束指挥
    :param data: 结束指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.end_of_command_url, data=data)
    return response


def replace_of_command(data):
    '''
    接替指挥
    :param data: 接替指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.replace_of_command_url, data=data)
    return response


def video_command_group_member_started(data):
    '''
    视频指挥组-获取该成员启动的组
    :param data: 视频指挥组-获取该成员启动的组数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.video_command_group_member_started_url, data=data)
    return response


def receive_video_command_group_member_started_list(data):
    '''
    获取视频指挥开启组信息列表
    :param data: 获取视频指挥开启组信息列表数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.receive_video_command_group_member_started_list_url,
                            data=data)
    return response


def video_command_group_retreats_members(data):
    '''
    视频指挥组强退成员
    :param data: 视频指挥组强退成员数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.video_command_group_retreats_members_url, data=data)
    return response


def cancel_on_the_silent(data):
    '''
    取消对上静默
    :param data: 取消对上静默数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.cancel_on_the_silent_url, data=data)
    return response


def cancel_down_the_silent(data):
    '''
    取消对下静默
    :param data: 取消对下静默数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.cancel_down_the_silent_url, data=data)
    return response


def cancel_replace_of_command(data):
    '''
    取消接替指挥
    :param data: 取消接替指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.cancel_replace_of_command_url, data=data)
    return response


def cancel_authorization_of_command(data):
    '''
    取消授权指挥
    :param data: 取消授权指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.cancel_authorization_of_command_url, data=data)
    return response


def cancel_great_of_command(data):
    '''
    取消越级指挥
    :param data: 取消越级指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.cancel_great_of_command_url, data=data)
    return response


def cancel_perform_command(data):
    '''
    取消专项指挥
    :param data: 取消专项指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.cancel_perform_command_url, data=data)
    return response


def video_command_resume_suspended(data):
    '''
    视频指挥-恢复暂停
    :param data: 视频指挥-恢复暂停数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.video_command_resume_suspended_url, data=data)
    return response


def refuse_coordinated_command(data):
    '''
    拒绝协同指挥
    :param data: 拒绝协同指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.refuse_coordinated_command_url, data=data)
    return response


def video_command_enter_command(data):
    '''
    视频指挥-进入指挥
    :param data: 视频指挥-进入指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.video_command_enter_command_url, data=data)
    return response


def receive_video_command_group_details(data):
    '''
    获取视频指挥组详细信息
    :param data: 获取视频指挥组详细信息数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.video_command_enter_command_url, data=data)
    return response


def command_group_personnel_tree(data):
    '''
    指挥组人员树
    :param data: 指挥组人员树数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.command_group_personnel_tree_url, data=data)
    return response


def apply_coordinated_command(data):
    '''
    申请协同指挥
    :param data: 申请协同指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.apply_coordinated_command_url, data=data)
    return response


def authorization_of_command(data):
    '''
    授权指挥
    :param data: 授权指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.authorization_of_command_url, data=data)
    return response


def video_command_group_open_command(data):
    '''
    视频指挥组开启指挥
    :param data: 视频指挥组开启指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.video_command_group_open_command_url, data=data)
    return response


def exit_the_command(data):
    '''
    退出指挥
    :param data: 退出指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.exit_the_command_url, data=data)
    return response


def editor_command_group(data):
    '''
    编辑指挥分组
    :param data: 编辑指挥分组数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.editor_command_group_url, data=data)
    return response


def receive_current_user_command_group(data):
    '''
    获取当前用户指挥分组
    :param data: 获取当前用户指挥分组数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.receive_current_user_command_group_url, data=data)
    return response


def great_command(data):
    '''
    越级指挥
    :param data: 越级指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.great_command_url, data=data)
    return response


def pause_command(data):
    '''
    暂停指挥
    :param data: 暂停指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.pause_command_url, data=data)
    return response


def perform_command(data):
    '''
    专向指挥
    :param data: 专向指挥数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoCommandUrl.perform_command_url, data=data)
    return response

