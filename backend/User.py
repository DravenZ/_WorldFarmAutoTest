#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/9/6'
"""


from utils.Config import Config
from utils.Util import Request
from utils.Log import Log
from backend.Tool import Tool
from backend.Session import UserSession
import json


class User(object):

    def __init__(self, mobile, password, register=False, login_type=1, mobile_region=86):
        self.log = Log('User')
        self.tool = Tool()
        self.request = Request()
        self.user_info = self.tool.query_user_info_by_mobile(mobile)
        if self.user_info != ():
            self.user_info = self.user_info[0]
        if register:
            if self.user_info:
                self.tool.delete_user_by_mobile(mobile)
            else:
                pass
            self.dataSSO = Config('sso').data
            validate_code_data = \
                self.dataSSO['http://dev.sso.worldfarm.com']['/mobile/sso/register/validate-verify-code']
            validate_code_data["mobileRegion"] = mobile_region
            validate_code_data["mobile"] = mobile
            validate_code = self.request.post(
                url="http://dev.sso.worldfarm.com/mobile/sso/register/validate-verify-code",
                data=validate_code_data)
            business_token = json.loads(validate_code)["content"]
            register_data = self.dataSSO['http://dev.sso.worldfarm.com']['/mobile/sso/register']
            register_data["mobileRegion"] = mobile_region
            register_data["mobile"] = mobile
            register_data["newPassword"] = password
            register_data["businessToken"] = business_token
            self.request.post(url="http://dev.sso.worldfarm.com/mobile/sso/register",
                              data=register_data)
            user_info = self.tool.query_user_info_by_mobile(mobile)[0]
            self.user_id = user_info["id"]
            self.real_name = user_info["real_name"]
            self.user_name = user_info["username"]
            self.sex = user_info["sex"]
            self.mobile_region = user_info["mobile_region"]
            self.mobile = user_info["mobile"]
            self.email = user_info["email"]
            self.email_state = user_info["email_state"]
            self.account_status = user_info["account_status"]
            self.account_type = user_info["account_type"]
            self.head_img = user_info["head_img"]
            self.company_name = user_info["company_name"]
            self.register_time = user_info["register_time"]
            self.nation_id = user_info["nation_id"]
            self.province_id = user_info["province_id"]
            self.city_id = user_info["city_id"]
            self.address = user_info["address"]
            self.birthday = user_info["birthday"]
            self.edit_time = user_info["edit_time"]
            self.log.logger.debug("手机号为 %s 的用户注册成功, id为%s" % (str(self.mobile), str(self.user_id)))
            us = UserSession(mobile, password, login_type)
            self.password = password
            self.token, self.device_id = us.token, us.deviceId
            self.language = 'zh'
        else:
            if self.user_info:
                self.user_id = self.user_info["id"]
                self.real_name = self.user_info["real_name"]
                self.user_name = self.user_info["username"]
                self.sex = self.user_info["sex"]
                self.mobile_region = self.user_info["mobile_region"]
                self.mobile = self.user_info["mobile"]
                self.email = self.user_info["email"]
                self.email_state = self.user_info["email_state"]
                self.account_status = self.user_info["account_status"]
                self.account_type = self.user_info["account_type"]
                self.head_img = self.user_info["head_img"]
                self.company_name = self.user_info["company_name"]
                self.register_time = self.user_info["register_time"]
                self.nation_id = self.user_info["nation_id"]
                self.province_id = self.user_info["province_id"]
                self.city_id = self.user_info["city_id"]
                self.address = self.user_info["address"]
                self.birthday = self.user_info["birthday"]
                self.edit_time = self.user_info["edit_time"]
                us = UserSession(mobile, password, login_type)
                self.password = password
                self.token, self.device_id = us.token, us.deviceId
                self.language = 'zh'
            else:
                raise Exception('手机号 %s 无对应用户: 1. 若需老账号请修改手机号; 2. 若需新注册添加, register=True'
                                % str(mobile))




# if __name__ == '__main__':
#     user = User("13658082213", "123456a", register=False)
#     user.update_user("星买家", "男", "成都大农科技有限公司", "前端工程师",
#                      "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012058085.png")
#     user.approve_seller_agent("鑫中介", "大农科技鑫中介公司")
