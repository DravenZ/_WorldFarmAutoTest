#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/9/10'
"""


from utils.Util import Request
from utils.Log import Log
from backend.Tool import Tool
from backend.Session import EmployeeSession


class Employee(object):

    def __init__(self, account, password):
        gender = {'1': '男', '2': '女'}
        self.log = Log('Employee')
        self.tool = Tool()
        employee_info = self.tool.query_employee_info_by_account(account)[0]
        self.real_name = employee_info['real_name']
        self.log.logger.debug("工号 %s 的 姓名 为 %s" % (str(account), self.real_name))
        self.mobile = employee_info['mobile']
        self.log.logger.debug("工号 %s 的 手机号 为 %s" % (str(account), self.mobile))
        self.mobile_region = employee_info['mobile_region']
        self.log.logger.debug("工号 %s 的 手机国际区号 为 %s" % (str(account), self.mobile_region))
        self.account_status = employee_info['account_status']
        self.log.logger.debug("工号 %s 的 账户状态 为 %s" % (str(account), self.account_status))
        self.account_type = employee_info['account_type']
        self.log.logger.debug("工号 %s 的 账户类型 为 %s" % (str(account), self.account_type))
        self.email = employee_info['email']
        self.log.logger.debug("工号 %s 的 邮箱 为 %s" % (str(account), self.email))
        self.email_state = employee_info['email_state']
        self.log.logger.debug("工号 %s 的 邮箱状态 为 %s" % (str(account), self.email_state))
        self.user_id = employee_info['id']
        self.log.logger.debug("工号 %s 的 用户id 为 %s" % (str(account), self.user_id))
        self.register_time = employee_info['register_time']
        self.log.logger.debug("工号 %s 的 注册时间 为 %s" % (str(account), self.register_time))
        self.account = str(account)
        self.log.logger.debug("工号 %s 的 工号 为 %s" % (str(account), str(account)))
        self.birthday = employee_info['birthday']
        self.log.logger.debug("工号 %s 的 生日 为 %s" % (str(account), self.birthday))
        self.head_img = employee_info['head_img']
        self.log.logger.debug("工号 %s 的 头像 为 %s" % (str(account), self.head_img))
        # self.sex = employee_info['sex']
        # self.log.logger.debug("工号 %s 的 性别 为 %s" % (str(account), gender[str(self.sex)]))
        self.request = Request()
        session = EmployeeSession(account, password)
        self.token = session.token
        self.log.logger.debug("工号 %s 的 token 为 %s" % (str(account), session.token))
        self.device_id = session.deviceId
        self.log.logger.debug("工号 %s 的 deviceId 为 %s" % (str(account), session.deviceId))


# if __name__ == '__main__':
#     Employee('100031', '123456')

