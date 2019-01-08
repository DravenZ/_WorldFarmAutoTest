#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/20'
"""


from utils.Util import Request
from utils.Config import Config
import json


class SessionTool(object):
    dataSSO = Config('sso').data

    def get_user_session(self, mobile, password, login_type=1, mobile_region=86):
        if login_type == 1:
            data = self.dataSSO['http://dev.sso.worldfarm.com']['/mobile/sso/login']
            data["mobileRegion"] = mobile_region
            data["mobile"] = mobile
            data["password"] = password
            session = Request().post(url="http://dev.sso.worldfarm.com/mobile/sso/login", data=data)
            return session
        elif login_type == 2:
            data = self.dataSSO['http://dev.sso.worldfarm.com']['/web/sso/login']
            data["mobileRegion"] = mobile_region
            data["mobile"] = mobile
            data["password"] = password
            session = Request().post(url="http://dev.sso.worldfarm.com/web/sso/login", data=data)
            return session
        else:
            return "login_type参数错误;1:app,2:web"

    def get_employee_session(self, account, password):
        data = self.dataSSO['http://dev.sso.worldfarm.com']['/web/sso/service-emp-login']
        data['account'] = account
        data['password'] = password
        session = Request().post(url="http://dev.sso.worldfarm.com/web/sso/service-emp-login", data=data)
        return session


class UserSession(object):
    def __init__(self, mobile, password, login_type=1, mobile_region=86):
        session = SessionTool().get_user_session(mobile, password, login_type, mobile_region)
        session_json = json.loads(session)
        self.token = str(session_json["content"]["token"])
        self.deviceId = str(session_json["content"]["deviceId"])


class EmployeeSession(object):
    def __init__(self, account, password):
        session = SessionTool().get_employee_session(account, password)
        session_json = json.loads(session)
        self.token = str(session_json["content"]["token"])
        self.deviceId = str(session_json["content"]["deviceId"])


# if __name__ == '__main__':
    # user = UserSession('18602832572', '123456a')
    # emp = EmployeeSession('100031', '123456')
#     print(user.token, user.deviceId)
#     print(emp.token, emp.deviceId)
