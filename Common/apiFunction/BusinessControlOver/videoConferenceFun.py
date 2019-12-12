# author:LEO GAO
# project Encoding:UTF-8


import requests
from Common.apiUrl.BusinessControlOver.videoConferenceUrl import VideoConferenceUrl
from Common.config import header


def add_video_conference_group(header_name, data):
    '''
    视频会议组-新增
    :param data: 视频会议组-新增数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header_name, url=VideoConferenceUrl.video_conference_group_add_url, data=data)
    return response


def add_video_conference_group_member(data):
    '''
    视频会议组 - 添加成员
    :param data: 视频会议组 - 添加成员数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header,url=VideoConferenceUrl.video_conference_group_add_member_url, data=data)
    return response


def video_meeting_apply_to_speak(data):
    '''
    视频会议-发言申请
    :param data: 视频会议-发言申请数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_apply_to_speak_url, data=data)
    return response


def video_meeting_group_designated_by_chairman(data):
    '''
    视频会议组-主席指定发言
    :param data: 视频会议组-主席指定发言数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_group_designated_by_chairman_url,
                            data=data)
    return response


def video_meeting_group_call(data):
    '''
    视频会议组-呼叫
    :param data: 视频会议组-呼叫数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_group_call_url, data=data)
    return response


def video_meeting_cancel_apply_to_speak(data):
    '''
    视频会议-取消发言申请
    :param data: 视频会议-取消发言申请数据
    :return:
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_cancel_apply_to_speak_url, data=data)
    return response


def video_meeting_cancel_strong_back(data):
    '''
    视频会议-取消强退
    :param data: 视频会议-取消强退数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_cancel_strong_back_url, data=data)
    return response


def video_meeting_group_designated_by_chairman_cancel(data):
    '''
    视频会议组-主席取消指定发言
    :param data: 视频会议组-主席取消指定发言数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header,
                            url=VideoConferenceUrl.video_meeting_group_designated_by_chairman_cancel_url, data=data)
    return response


def video_meeting_confirm_member_change(data):
    '''
    视频会议确实讨论成员变更
    :param data: 视频会议确实讨论成员变更数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_confirm_member_change_url, data=data)
    return response


def video_meeting_confirm_apply_to_speak(data):
    '''
    视频会议-确认发言申请
    :param data: 视频会议-确认发言申请数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_confirm_apply_to_speak_url, data=data)
    return response


def video_meeting_group_delete(data):
    '''
    视频会议组-删除
    :param data: 视频会议组-删除数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_group_delete_url, data=data)
    return response


def video_meeting_group_exit_meeting(data):
    '''
    视频会议组-退出会议
    :param data: 视频会议组-退出会议数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_group_exit_meeting_url, data=data)
    return response


def video_meeting_receive_discussion_members_list(data):
    '''
    视频会议获取讨论成员列表
    :param data: 视频会议获取讨论成员列表数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_receive_discussion_members_list_url,
                            data=data)
    return response


def video_member_group_receive_member(data):
    '''
    视频会议组-获取成员
    :param data: 视频会议组-获取成员数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_member_group_receive_member_url, data=data)
    return response


def video_member_group_receive_member_start_group(data):
    '''
    视频会议组-获取该成员启动的组
    :param data: 视频会议组-获取该成员启动的组数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_member_group_receive_member_start_group_url,
                            data=data)
    return response


def receive_video_meeting_opening_group_information(data):
    '''
    获取视频会议开启组信息
    :param data: 获取视频会议开启组信息数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.receive_video_meeting_opening_group_information_url,
                            data=data)
    return response


def video_meeting_resume_suspension(data):
    '''
    视频会议-恢复暂停
    :param data: 视频会议-恢复暂停数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_resume_suspension_url, data=data)
    return response


def video_meeting_refuse_apply(data):
    '''
    视频会议-拒绝申请
    :param data: 视频会议-拒绝申请数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_refuse_apply_url, data=data)
    return response


def video_meeting_withdraw_members(data):
    '''
    视频会议-强退成员
    :param data: 视频会议-强退成员数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_withdraw_members_url, data=data)
    return response


def video_meeting_enter(data):
    '''
    视频会议-进入
    :param data: 视频会议-进入数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_enter_url, data=data)
    return response


def receive_video_member_group_details(data):
    '''
    获取视频会议组详细信息
    :param data: 获取视频会议组详细信息数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.receive_video_member_group_details_url, data=data)
    return response


def video_meeting_open_meeting(header_name, data):
    '''
    视频会议-开启会议
    :param data: 视频会议-开启会议数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header_name, url=VideoConferenceUrl.video_meeting_open_meeting_url, data=data)
    return response


def video_meeting_open_discussion(data):
    '''
    视频会议-开启讨论
    :param data: 视频会议-开启讨论数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_open_discussion_url, data=data)
    return response


def video_meeting_end(data):
    '''
    视频会议-结束
    :param data: 视频会议-结束数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_end_url, data=data)
    return response


def video_meeting_end_discussion(data):
    '''
    视频会议-结束讨论
    :param data: 视频会议-结束讨论数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_end_discussion_url, data=data)
    return response


def video_meeting_group_end_meeting(data):
    '''
    视频会议组-结束讨论
    :param data:
    :return:
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_group_end_meeting_url, data=data)
    return response


def video_meeting_pause(data):
    '''
    视频会议-暂停
    :param data: 视频会议-暂停数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_pause_url, data=data)
    return response


def video_meeting_group_update(data):
    '''
    视频会议组-修改
    :param data: 视频会议组-修改数据
    :return: response
    '''
    request = requests.session()
    response = request.post(headers=header, url=VideoConferenceUrl.video_meeting_group_update_url, data=data)
    return response


def receive_video_meeting_group_list(header_name, data):
    '''
    获取视频会议组
    :param data: 获取视频会议组数据
    :return: response
    '''
    request = requests.session()
    response = request.get(headers=header_name, url=VideoConferenceUrl.receive_video_meeting_group_list_url, data=data)
    return response

