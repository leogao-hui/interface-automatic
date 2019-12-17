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
    receive_video_meeting_group_list, video_meeting_open_meeting
from Common.apiFunction.backgroundManagement.deviceManagementFun import add_device_information


class TestOpenVideoConference(unittest.TestCase):

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

    # 正常新增开启视频会议
    def test_normal_add_video_conference(cls):

        # 主席登录
        auth = login(get_header(''), json_dump(basic_data.login_user_data_one)).json()['d']['authorization']
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
        add_video_response = add_video_conference_group(get_header(auth), json_dump(add_video_conference_data))
        cls.assertEqual('新增成功', add_video_response.json()['m'])
        cls.assertEqual(True, add_video_response.json()['s'])
        cls.assertEqual(200, add_video_response.status_code)
        if add_video_response.json()['m'] == '新增成功':
            log().info('新增视频会议组成功')
        else:
            log().error('新增视频会议组失败')

        # 获取视频会议组ID
        meeting_conference_id = receive_video_meeting_group_list(get_header(auth), '').json()['d']['list'][0]['id']

        # 启动视频会议组
        open_meeting_data = {
            'chairMan': cls.user_id_one,
            'id': meeting_conference_id
        }
        open_meeting_response = video_meeting_open_meeting(get_header(auth), json_dump(open_meeting_data))
        cls.assertEqual(True, open_meeting_response.json()['s'])
        cls.assertEqual('启动成功', open_meeting_response.json()['m'])
        cls.assertEqual(200, open_meeting_response.status_code)
        if open_meeting_response.json()['m'] == '启动成功':
            log().info('启动视频会议组成功')
        else:
            log().error('启动视频会议组失败')
        cls.assertIn('开启了视频会议会议组', receive_data(cls.ws_two, 2)[0])
        cls.assertIn('开启了视频会议会议组', receive_data(cls.ws_three, 2)[0])
        log().info('socket信息发送成功')

    @classmethod
    def tearDownClass(cls):
        delete_database_data_test_ci()

