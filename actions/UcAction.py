# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json

class UcAction(object):

    def __init__(self, Uc):
        self.log = Log('Uc')
        self.request = Request()
        self.Uc = Uc

    def _admin_emp_add(self, realName, mobileRegion, mobile, email, roles):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/emp/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['realName'] = realName
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['email'] = email
        data['roles'] = roles
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/emp/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_emp_frozen(self, accountId, reason):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/emp/frozen')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['accountId'] = accountId
        data['reason'] = reason
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/emp/frozen', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_emp_list(self, accountType, status, realName, account, mobile, email, pn, ps):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/emp/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['accountType'] = accountType
        data['status'] = status
        data['realName'] = realName
        data['account'] = account
        data['mobile'] = mobile
        data['email'] = email
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/emp/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_emp_reset_pwd(self, accountId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/emp/reset-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['accountId'] = accountId
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/emp/reset-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_emp_unfrozen(self, accountId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/emp/unfrozen')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['accountId'] = accountId
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/emp/unfrozen', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_role_get_ids(self):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/role/get-ids')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/role/get-ids', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_role_list(self):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/role/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/role/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_role_list_by_user(self):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/role/list-by-user')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/role/list-by-user', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_frozen(self, userId, reason):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/user/frozen')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['reason'] = reason
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/user/frozen', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_list(self, accountType, status, realName, mobile, email, pn, ps):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/user/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['accountType'] = accountType
        data['status'] = status
        data['realName'] = realName
        data['mobile'] = mobile
        data['email'] = email
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/user/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_unfrozen(self, userId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/admin/user/unfrozen')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.uc.worldfarm.com/admin/user/unfrozen', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_role_check_role(self, userId, roleId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/role/check-role')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['roleId'] = roleId
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/role/check-role', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_role_role_by_id(self, userId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/role/role-by-id')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/role/role-by-id', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_role_service_list(self):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/role/service-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/role/service-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_role_user_by_role(self, roleId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/role/user-by-role')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['roleId'] = roleId
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/role/user-by-role', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_buyer_sa_register(self, mobileRegion, mobile, password):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/buyer-sa-register')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/buyer-sa-register', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_detail(self, userId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_detail_by_email(self, email):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/detail-by-email')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['email'] = email
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/detail-by-email', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_detail_by_mobile(self, mobileRegion, mobile):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/detail-by-mobile')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/detail-by-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_detail_list(self, userIds):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/detail-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userIds'] = userIds
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/detail-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_email_validate(self, userId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/email-validate')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/email-validate', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_get_account_type(self, userIds):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/get-account-type')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userIds'] = userIds
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/get-account-type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_get_head_img(self, userIds):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/get-head-img')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userIds'] = userIds
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/get-head-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_get_id_by_name(self, name):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/get-id-by-name')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['name'] = name
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/get-id-by-name', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_get_real_name(self, userIds):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/get-real-name')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userIds'] = userIds
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/get-real-name', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_get_user_by_code(self, invitationCode):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/get-user-by-code')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/get-user-by-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_im_update_auth_agent(self, userId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/im/update-auth-agent')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/im/update-auth-agent', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_send_auth_email(self, userId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/send-auth-email')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/send-auth-email', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_sso_employee_and_pwd(self, workNo, password, roleIds):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/sso/employee-and-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['workNo'] = workNo
        data['password'] = password
        data['roleIds'] = roleIds
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/sso/employee-and-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_sso_freeze_user(self, userId, reason):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/sso/freeze-user')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['reason'] = reason
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/sso/freeze-user', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_sso_mobile_and_pwd(self, mobileRegion, mobile, password):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/sso/mobile-and-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/sso/mobile-and-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_sso_user_and_pwd(self, userId, password):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/sso/user-and-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['password'] = password
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/sso/user-and-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_update(self, userId, realName, sex, mobileRegion, mobile, email, emailState, headImg, companyName, companyPosition, nationId, provinceId, cityId, countryId, address, birthday, signature):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['realName'] = realName
        data['sex'] = sex
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['email'] = email
        data['emailState'] = emailState
        data['headImg'] = headImg
        data['companyName'] = companyName
        data['companyPosition'] = companyPosition
        data['nationId'] = nationId
        data['provinceId'] = provinceId
        data['cityId'] = cityId
        data['countryId'] = countryId
        data['address'] = address
        data['birthday'] = birthday
        data['signature'] = signature
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_update_mobile(self, userId, mobileRegion, mobile):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/update-mobile')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_update_password(self, userId, mobileRegion, mobile, oldPassword, newPassword):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/update-password')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['oldPassword'] = oldPassword
        data['newPassword'] = newPassword
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/update-password', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_update_password_by_id(self, userId, newPassword):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/update-password-by-id')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['newPassword'] = newPassword
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/update-password-by-id', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_update_password_by_mobile(self, mobileRegion, mobile, newPassword):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/update-password-by-mobile')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newPassword'] = newPassword
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/update-password-by-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_update_show_auth(self, userId):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/update-show-auth')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/update-show-auth', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_validate_pwd(self, userId, mobileRegion, mobile, password):
        data = self.Uc.get('http://dev.uc.worldfarm.com').get('/api/user/validate-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        response = self.request.post(url='http://dev.uc.worldfarm.com/api/user/validate-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
