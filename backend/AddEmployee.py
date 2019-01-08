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
from backend.Session import EmployeeSession


class AddEmployee(object):
    def __init__(self, real_name, mobile, email, region, *roles):
        self.log = Log('User')
        self.log.logger.debug(type(roles))
        self.tool = Tool()
        self.request = Request()
        self.mobile = mobile
        self.user_info = self.tool.query_user_info_by_mobile(self.mobile)
        self.role_list = self.tool.get_role_code(*roles)
        self.real_name = real_name
        self.email = email
        self.region = region
        data_uc = Config('uc').data
        employee_data = data_uc['http://dev.uc.worldfarm.com']['/admin/emp/add']
        employee_data["mobile"] = self.mobile
        employee_data["realName"] = self.real_name
        employee_data["email"] = self.email
        employee_data["mobileRegion"] = self.region
        employee_data["roles"] = self.role_list
        admin = EmployeeSession('007', '123456')
        employee_data["_tk_"] = admin.token
        employee_data["_deviceId_"] = admin.deviceId
        add_employee = self.request.post(url="http://dev.uc.worldfarm.com/admin/emp/add",
                                         data=employee_data)
        self.log.logger.debug(add_employee)


# if __name__ == '__main__':
#     AddEmployee('运营露瑶', '18382373126', 'luyao.yang@worldfarm.com', '86', '运营')
