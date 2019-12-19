#_author:leo gao
#encoding:utf-8


import unittest
import warnings
from Common.Data.videoConferenceData import basic_data
from Common.config import json_dump, get_header
from Common.Log.log import log
from Common.operateDatabaseData import add_database_data_test_ci, delete_database_data_test_ci, get_data_from_database
from Common.apiFunction.System.systemConfigurationFun import login, connect_socket, receive_data, exit_login
from Common.apiFunction.backgroundManagement.userManagementFun import add_user_information, user_bind_device
from Common.apiFunction.BusinessControlOver.videoConferenceFun import add_video_conference_group, \
    receive_video_meeting_group_list, video_meeting_open_meeting, add_video_conference_group_member, video_meeting_end,\
    receive_video_member_group_details
from Common.apiFunction.backgroundManagement.deviceManagementFun import add_device_information


class TestAddMember(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)  # 去除requests中多余的warning
        delete_database_data_test_ci()  # 清空数据库
        add_database_data_test_ci()  # 新增配置数据
        # 登录管理员账号
        response = login(get_header(''), json_dump(basic_data.administrator_login_data))
        # exit_login(get_header(response.json()['d']['authorization']), '')

        # 新增人员
        add_user_information(get_header(response.json()['d']['authorization']),
                                   json_dump(basic_data.add_user_data_one))
        add_user_information(get_header(response.json()['d']['authorization']),
                             json_dump(basic_data.add_user_data_two))
        add_user_information(get_header(response.json()['d']['authorization']),
                             json_dump(basic_data.add_user_data_three))
        add_user_information(get_header(response.json()['d']['authorization']),
                             json_dump(basic_data.add_user_data_four))

        # 新增设备
        add_device_information(get_header(response.json()['d']['authorization']), json_dump(basic_data.device_data))

        # 登录
        cls.user_id_one = login(get_header(''), json_dump(basic_data.login_user_data_one)).json()['d']['user']['id']
        login(get_header(''), json_dump(basic_data.login_user_data_two))
        cls.user_id_two = login(get_header(''), json_dump(basic_data.login_user_data_two)).json()['d']['user']['id']
        cls.user_id_three = login(get_header(''), json_dump(basic_data.login_user_data_three)).json()['d']['user']['id']
        cls.user_id_four = login(get_header(''), json_dump(basic_data.login_user_data_four)).json()['d']['user']['id']

        # 获取设备id
        device_id = get_data_from_database('select id from spzh_device where name = "设备一"')[0][0]
        user_bind_device_data = {
            "id": cls.user_id_one,
            "ids": device_id,
            "morendevice": device_id,

        }
        user_bind_device(get_header(response.json()['d']['authorization']), json_dump(user_bind_device_data))

        # 视频会议人员连接socket
        cls.ws_one = connect_socket(cls.user_id_one)
        cls.ws_two = connect_socket(cls.user_id_two)
        cls.ws_three = connect_socket(cls.user_id_three)
        cls.ws_four = connect_socket(cls.user_id_four)

        # 主席身份登录
        cls.auth = login(get_header(''), json_dump(basic_data.login_user_data_one)).json()['d']['authorization']
        add_video_conference_data = {
            'name': '视频会议',
            'chairMan': cls.user_id_one,
            'spokesMan': cls.user_id_one,
            'member': [
                {'id': cls.user_id_one,
                 'type': 2
                 },
                {
                    'id': cls.user_id_two,
                    'type': 2
                },
                {
                    'id': cls.user_id_three,
                    'type': 2
                }
            ],
        }

        # 新增视频会议组
        add_video_conference_group(get_header(cls.auth), json_dump(add_video_conference_data))

        # 获取视频会议组
        cls.meeting_conference_id = receive_video_meeting_group_list(get_header(cls.auth), '').json()['d']['list'][0]['id']

        # 启动视频会议组
        open_meeting_data = {
            'chairMan': cls.user_id_one,
            'id': cls.meeting_conference_id
        }
        video_meeting_open_meeting(get_header(cls.auth), json_dump(open_meeting_data))

    # 正常添加添加成员
    def test_normal_add_member_in_video_conference(cls):
        print(cls.meeting_conference_id)
        add_member_in_video_conference_data = {
            'id': cls.meeting_conference_id,
            'member': [
                {
                    'id': cls.user_id_one,
                    'temporary': 0,
                    'type': 2,
                },
                {
                    'id': cls.user_id_two,
                    'temporary': 0,
                    'type': 2,
                },
                {
                    'id': cls.user_id_three,
                    'temporary': 0,
                    'type': 2,
                },
                {
                    'id': cls.user_id_four,
                    'temporary': 1,
                    'type': 2,
                },
            ]
        }
        response = add_video_conference_group_member(get_header(cls.auth),
                                                     json_dump(add_member_in_video_conference_data))
        cls.assertEqual(200, response.status_code)
        cls.assertEqual(True, response.json()['s'])
        cls.assertEqual('添加成员成功', response.json()['m'])
        data = receive_data(cls.ws_four, 2)

    # 添加人员表没有中的人员
    # def test_no_person_in_member_list(cls):
    #     add_member_in_video_conference_data = {
    #         'id': cls.meeting_conference_id,
    #         'member': [
    #             {
    #                 'id': cls.user_id_four + 'a',
    #                 'temporary': 0,
    #                 'type': 2,
    #             }
    #         ]
    #     }
    #     response = add_video_conference_group_member(get_header(cls.auth),
    #                                                  json_dump(add_member_in_video_conference_data))
    #     print(response.json())

    # 会议结束后，添加成员不保存之会议组中
    def test_video_conference_end_temporary_member_not_in_conference(cls):
        add_member_in_video_conference_data = {
            'id': cls.meeting_conference_id,
            'member': [
                {
                    'id': cls.user_id_four,
                    'temporary': 0,
                    'type': 2,
                }
            ]
        }
        # 新增成员
        add_video_conference_group_member(get_header(cls.auth), json_dump(add_member_in_video_conference_data))

        # 会议结束
        video_meeting_end_data = {
            'id': cls.meeting_conference_id,
            'relationid': cls.user_id_one,
        }
        end_video_meeting_response = video_meeting_end(get_header(cls.auth), json_dump(video_meeting_end_data))
        cls.assertEqual(True, end_video_meeting_response.json()['s'])
        cls.assertEqual('结束成功', end_video_meeting_response.json()['m'])

        receive_video_member_group_details_data = {
            'id': cls.meeting_conference_id,
        }

        receive_video_meeting_group_list_response = receive_video_member_group_details(get_header(cls.auth),
                                                      json_dump(receive_video_member_group_details_data))
        cls.assertEqual(True, receive_video_meeting_group_list_response.json()['s'])
        cls.assertEqual('获取数据成功', receive_video_meeting_group_list_response.json()['m'])
        for i in receive_video_meeting_group_list_response.json()['d']['list']['member']:
            cls.assertNotIn(i['name'], '测试人员四')








